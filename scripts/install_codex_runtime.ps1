[CmdletBinding()]
param(
    [switch]$Apply,
    [switch]$AllCanonicalSkills,
    [switch]$Force,
    [string[]]$Pack = @(),
    [string]$ProjectRoot = "",
    [string]$CodexHome = $(if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $HOME ".codex" }),
    [string]$SkillsHome = $(Join-Path (Join-Path $HOME ".agents") "skills")
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$RepoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$RuntimeRoot = Join-Path $RepoRoot "runtime/codex"
$RegistryPath = Join-Path $RepoRoot "registry/skills.json"
$PackManifestPath = Join-Path $RuntimeRoot "packs/skill-packs.json"
$Timestamp = Get-Date -Format "yyyyMMdd-HHmmss"
$BackupRoot = Join-Path $CodexHome "backups/7dejv-$Timestamp"

$BaselineSkills = @(
    "repository-inventory-skill",
    "7dejv-repository-quality-audit-skill",
    "7dejv-secret-scanner",
    "7dejv-external-dependency-auditor",
    "7dejv-prompt-injection-defense",
    "7dejv-eval-generator",
    "7dejv-eval-grader",
    "7dejv-readiness-status-calculator",
    "7dejv-skill-linter",
    "7dejv-skill-factory",
    "7dejv-expert-router"
)

$Results = New-Object System.Collections.Generic.List[object]
$HadHold = $false
$HadError = $false
$ResolvedProjectRoot = $null
$ProjectSkillsHome = $null
$SelectedPacks = New-Object System.Collections.Generic.List[string]

function Add-Result {
    param(
        [string]$State,
        [string]$Artifact,
        [string]$Destination,
        [string]$Message
    )
    $script:Results.Add([pscustomobject]@{
        state = $State
        artifact = $Artifact
        destination = $Destination
        message = $Message
    })
    if ($State -eq "HOLD") { $script:HadHold = $true }
    if ($State -eq "BLOCKED") { $script:HadError = $true }
}

function Ensure-Directory {
    param([string]$Path)
    if (-not (Test-Path -LiteralPath $Path) -and $Apply) {
        New-Item -ItemType Directory -Force -Path $Path | Out-Null
    }
}

function Get-FileFingerprint {
    param([string]$Path)
    if (-not (Test-Path -LiteralPath $Path -PathType Leaf)) { return $null }
    return (Get-FileHash -Algorithm SHA256 -LiteralPath $Path).Hash
}

function Get-TreeFingerprint {
    param([string]$Path)
    if (-not (Test-Path -LiteralPath $Path -PathType Container)) { return $null }
    $root = (Resolve-Path -LiteralPath $Path).Path
    $parts = Get-ChildItem -LiteralPath $root -Recurse -File | ForEach-Object {
        $relative = $_.FullName.Substring($root.Length).TrimStart([char]'\', [char]'/').Replace('\','/')
        "$relative`:$((Get-FileHash -Algorithm SHA256 -LiteralPath $_.FullName).Hash)"
    } | Sort-Object
    return ($parts -join "|")
}

function Backup-Existing {
    param(
        [string]$Path,
        [string]$Label
    )
    if (-not $Apply) { return }
    Ensure-Directory -Path $BackupRoot
    $safe = ($Label -replace '[^A-Za-z0-9_.-]', '_')
    $target = Join-Path $BackupRoot $safe
    if (Test-Path -LiteralPath $Path -PathType Container) {
        Copy-Item -LiteralPath $Path -Destination $target -Recurse -Force
    } else {
        Copy-Item -LiteralPath $Path -Destination $target -Force
    }
}

function Copy-FileSafe {
    param(
        [string]$Source,
        [string]$Destination,
        [string]$Label
    )
    if (-not (Test-Path -LiteralPath $Source -PathType Leaf)) {
        Add-Result -State "BLOCKED" -Artifact $Label -Destination $Destination -Message "Source file is missing: $Source"
        return
    }

    if (Test-Path -LiteralPath $Destination) {
        if ((Get-FileFingerprint $Source) -eq (Get-FileFingerprint $Destination)) {
            Add-Result -State "PASS" -Artifact $Label -Destination $Destination -Message "Already current."
            return
        }
        if (-not $Force) {
            Add-Result -State "HOLD" -Artifact $Label -Destination $Destination -Message "Existing file differs; rerun with -Force only after reviewing the conflict."
            return
        }
        if ($Apply) {
            Backup-Existing -Path $Destination -Label $Label
            Copy-Item -LiteralPath $Source -Destination $Destination -Force
            Add-Result -State "PASS" -Artifact $Label -Destination $Destination -Message "Updated after backup."
        } else {
            Add-Result -State "DRY_RUN" -Artifact $Label -Destination $Destination -Message "Would replace differing file after backup because -Force is set."
        }
        return
    }

    if ($Apply) {
        Ensure-Directory -Path (Split-Path -Parent $Destination)
        Copy-Item -LiteralPath $Source -Destination $Destination
        Add-Result -State "PASS" -Artifact $Label -Destination $Destination -Message "Installed."
    } else {
        Add-Result -State "DRY_RUN" -Artifact $Label -Destination $Destination -Message "Would install."
    }
}

function Copy-DirectorySafe {
    param(
        [string]$Source,
        [string]$Destination,
        [string]$Label
    )
    if (-not (Test-Path -LiteralPath $Source -PathType Container)) {
        Add-Result -State "BLOCKED" -Artifact $Label -Destination $Destination -Message "Source directory is missing: $Source"
        return
    }

    if (Test-Path -LiteralPath $Destination) {
        if ((Get-TreeFingerprint $Source) -eq (Get-TreeFingerprint $Destination)) {
            Add-Result -State "PASS" -Artifact $Label -Destination $Destination -Message "Already current."
            return
        }
        if (-not $Force) {
            Add-Result -State "HOLD" -Artifact $Label -Destination $Destination -Message "Existing directory differs; rerun with -Force only after reviewing the conflict."
            return
        }
        if ($Apply) {
            Backup-Existing -Path $Destination -Label $Label
            Remove-Item -LiteralPath $Destination -Recurse -Force
            Ensure-Directory -Path (Split-Path -Parent $Destination)
            Copy-Item -LiteralPath $Source -Destination $Destination -Recurse
            Add-Result -State "PASS" -Artifact $Label -Destination $Destination -Message "Updated after backup."
        } else {
            Add-Result -State "DRY_RUN" -Artifact $Label -Destination $Destination -Message "Would replace differing directory after backup because -Force is set."
        }
        return
    }

    if ($Apply) {
        Ensure-Directory -Path (Split-Path -Parent $Destination)
        Copy-Item -LiteralPath $Source -Destination $Destination -Recurse
        Add-Result -State "PASS" -Artifact $Label -Destination $Destination -Message "Installed."
    } else {
        Add-Result -State "DRY_RUN" -Artifact $Label -Destination $Destination -Message "Would install."
    }
}

function Install-SkillSet {
    param(
        [string[]]$SkillNames,
        [string]$DestinationRoot,
        [string]$ScopeLabel,
        [string[]]$CanonicalNames
    )
    foreach ($SkillName in ($SkillNames | Sort-Object -Unique)) {
        $destination = Join-Path $DestinationRoot $SkillName
        if ($SkillName -notin $CanonicalNames) {
            Add-Result -State "BLOCKED" -Artifact ("skill-" + $SkillName) -Destination $destination -Message "Skill is not canonical in registry/skills.json."
            continue
        }
        Copy-DirectorySafe -Source (Join-Path (Join-Path $RepoRoot "skills") $SkillName) -Destination $destination -Label ("$ScopeLabel-skill-" + $SkillName)
    }
}

try {
    if (-not (Test-Path -LiteralPath $RuntimeRoot -PathType Container)) {
        throw "Runtime directory missing: $RuntimeRoot"
    }
    if (-not (Test-Path -LiteralPath $RegistryPath -PathType Leaf)) {
        throw "Skill registry missing: $RegistryPath"
    }
    if (-not (Test-Path -LiteralPath $PackManifestPath -PathType Leaf)) {
        throw "Skill-pack manifest missing: $PackManifestPath"
    }

    Copy-FileSafe -Source (Join-Path $RuntimeRoot "global/AGENTS.md") -Destination (Join-Path $CodexHome "AGENTS.md") -Label "global-AGENTS"
    Copy-FileSafe -Source (Join-Path $RuntimeRoot "config/7dejv.config.toml") -Destination (Join-Path $CodexHome "7dejv.config.toml") -Label "7dejv-profile"

    Get-ChildItem -LiteralPath (Join-Path $RuntimeRoot "agents") -Filter "*.toml" -File | Sort-Object Name | ForEach-Object {
        Copy-FileSafe -Source $_.FullName -Destination (Join-Path (Join-Path $CodexHome "agents") $_.Name) -Label ("agent-" + $_.BaseName)
    }

    $Registry = Get-Content -LiteralPath $RegistryPath -Raw | ConvertFrom-Json
    $CanonicalNames = @($Registry.skills | Where-Object { $_.status -eq "canonical" } | ForEach-Object { $_.name })
    $GlobalSkillNames = if ($AllCanonicalSkills) { $CanonicalNames } else { $BaselineSkills }
    Install-SkillSet -SkillNames $GlobalSkillNames -DestinationRoot $SkillsHome -ScopeLabel "global" -CanonicalNames $CanonicalNames

    if ($Pack.Count -gt 0) {
        if ([string]::IsNullOrWhiteSpace($ProjectRoot)) {
            Add-Result -State "BLOCKED" -Artifact "expert-packs" -Destination "<project>/.agents/skills" -Message "-Pack requires -ProjectRoot so domain packs remain project-scoped."
        } elseif (-not (Test-Path -LiteralPath $ProjectRoot -PathType Container)) {
            Add-Result -State "BLOCKED" -Artifact "expert-packs" -Destination $ProjectRoot -Message "ProjectRoot does not exist or is not a directory."
        } else {
            $ResolvedProjectRoot = (Resolve-Path -LiteralPath $ProjectRoot).Path
            $ProjectSkillsHome = Join-Path (Join-Path $ResolvedProjectRoot ".agents") "skills"
            $PackManifest = Get-Content -LiteralPath $PackManifestPath -Raw | ConvertFrom-Json
            $ProjectSkillNames = New-Object System.Collections.Generic.List[string]

            foreach ($PackName in ($Pack | Sort-Object -Unique)) {
                $PackEntry = @($PackManifest.packs | Where-Object { $_.name -eq $PackName })
                if ($PackEntry.Count -ne 1) {
                    Add-Result -State "BLOCKED" -Artifact ("pack-" + $PackName) -Destination $ProjectSkillsHome -Message "Unknown or duplicate expert pack name."
                    continue
                }
                $SelectedPacks.Add($PackName)
                foreach ($SkillName in @($PackEntry[0].skills)) {
                    $ProjectSkillNames.Add([string]$SkillName)
                }
            }

            if ($ProjectSkillNames.Count -gt 0) {
                Install-SkillSet -SkillNames @($ProjectSkillNames) -DestinationRoot $ProjectSkillsHome -ScopeLabel "project" -CanonicalNames $CanonicalNames
            }
        }
    }
} catch {
    Add-Result -State "BLOCKED" -Artifact "installer" -Destination $CodexHome -Message $_.Exception.Message
}

$Status = if ($HadError) {
    "BLOCKED"
} elseif ($HadHold) {
    "HOLD"
} elseif (-not $Apply) {
    "DRY_RUN"
} else {
    "PASS"
}

[pscustomobject]@{
    status = $Status
    applied = [bool]$Apply
    force = [bool]$Force
    all_canonical_skills = [bool]$AllCanonicalSkills
    packs = @($SelectedPacks)
    codex_home = $CodexHome
    global_skills_home = $SkillsHome
    project_root = $ResolvedProjectRoot
    project_skills_home = $ProjectSkillsHome
    backup_root = if ($Apply -and $Force) { $BackupRoot } else { $null }
    results = $Results
} | ConvertTo-Json -Depth 6

if ($HadError) { exit 2 }
if ($HadHold) { exit 1 }
exit 0
