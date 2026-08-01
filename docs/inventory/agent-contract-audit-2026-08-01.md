# Agent Contract Audit - 2026-08-01

## Verdict

HOLD. No candidate contains all required contract fields: role/purpose, input and output. No source agent was promoted to the active agents/ catalog.

## Counts

- candidates: 39
- high confidence: 0
- probable: 11
- low: 28

## Required before promotion

- explicit purpose or role;
- structured input;
- structured output;
- handoff constraints and failure behavior for multi-agent use.

## Evidence

| confidence | name | source repo | branch | source path | role | input | output | source blob SHA |
| --- | --- | --- | --- | --- | --- | --- | --- |
| niska | 7dejv-agent-quality-auditor | 7dejv-skills-prompts | main | 03_agents/quality/7dejv-agent-quality-auditor.md | True | False | False | 10aacfe2ba7e6958d8ce6a4aebf36e2fcc758ea1 |
| niska | 7dejv-agent-security-auditor | 7dejv-skills-prompts | main | 03_agents/security/7dejv-agent-security-auditor.md | True | False | False | 7992b353f51679c2eca7ba448b52568aab46f3fb |
| niska | 7dejv-competitor-product-analyzer | 7dejv-skills-prompts | main | 03_agents/staw-expert-product-pipeline/7dejv-competitor-product-analyzer.md | True | False | False | c7825584626b37f2218635318de26b48637b455b |
| niska | 7dejv-composition-evidence-agent | 7dejv-skills-prompts | main | 03_agents/staw-expert-product-pipeline/7dejv-composition-evidence-agent.md | True | False | False | acf178be4de112b9e2e4f59e06758f0e8c0c4727 |
| niska | 7dejv-documentation-consistency-agent | 7dejv-skills-prompts | main | 03_agents/quality/7dejv-documentation-consistency-agent.md | True | False | False | 6d161606ae09db90b6be11c655bc0c3fdaae8ce6 |
| niska | 7dejv-dosage-test-planner | 7dejv-skills-prompts | main | 03_agents/staw-expert-product-pipeline/7dejv-dosage-test-planner.md | True | False | False | 492252fe23ef68b9d83628ed60b919d7c5214fc9 |
| niska | 7dejv-formulation-brief-builder | 7dejv-skills-prompts | main | 03_agents/staw-expert-product-pipeline/7dejv-formulation-brief-builder.md | True | False | False | 6c7c3ad6bfeb2ea8b563204bebc98867cab29dd4 |
| niska | 7dejv-label-a6-mono-builder | 7dejv-skills-prompts | main | 03_agents/staw-expert-product-pipeline/7dejv-label-a6-mono-builder.md | True | False | False | 0c6a34cf7d51f02f83904ed89e001beed5b1431e |
| niska | 7dejv-label-front-builder | 7dejv-skills-prompts | main | 03_agents/staw-expert-product-pipeline/7dejv-label-front-builder.md | True | False | False | 76e4b5e97a4b717dae922be3f625fa5c04cf05ba |
| niska | 7dejv-market-opportunity-scout | 7dejv-skills-prompts | main | 03_agents/staw-expert-product-pipeline/7dejv-market-opportunity-scout.md | True | False | False | 9150440fd0e0dea35cb4dbc0bdcaeb82dd5963c5 |
| niska | 7dejv-product-copy-builder | 7dejv-skills-prompts | main | 03_agents/staw-expert-product-pipeline/7dejv-product-copy-builder.md | True | False | False | 73c6f4c6e40e4cccd796709db24ee8e88b4cecc8 |
| niska | 7dejv-product-naming-agent | 7dejv-skills-prompts | main | 03_agents/staw-expert-product-pipeline/7dejv-product-naming-agent.md | True | False | False | 69b38291a35bfe00ffaa34574990d71807afba23 |
| niska | 7dejv-product-release-gate | 7dejv-skills-prompts | main | 03_agents/staw-expert-product-pipeline/7dejv-product-release-gate.md | True | False | False | 4542549eb2c8e7404688c5005cc2314969679228 |
| niska | 7dejv-repository-quality-auditor | 7dejv-skills-prompts | main | 03_agents/quality/7dejv-repository-quality-auditor.md | True | False | False | 5e4f38313c681f53a443a1d51645973b9df47aa4 |
| niska | 7dejv-schema-architect | 7dejv-skills-prompts | main | 03_agents/quality/7dejv-schema-architect.md | True | False | False | aa45e3da80d0016d719169e7987bba05e72d5be2 |
| niska | 7dejv-skill-evaluation-agent | 7dejv-skills-prompts | main | 03_agents/quality/7dejv-skill-evaluation-agent.md | True | False | False | a9fb71f23eaa7d1a23fe7baa888a8306bca12032 |
| niska | 7dejv-skill-factory | 7dejv-skills-prompts | main | 03_agents/staw-expert-product-pipeline/7dejv-skill-factory.md | True | False | False | ec6d5da7f89dec94d0bf1b2c7de67a441b2f84b0 |
| niska | 7dejv-skill-quality-auditor | 7dejv-skills-prompts | main | 03_agents/quality/7dejv-skill-quality-auditor.md | True | False | False | 3f1ab50fc203ab3b60cde12bbc03103e625abdf1 |
| niska | 7dejv-staw-knowledge-prototype-agent | 7dejv-skills-prompts | feature/staw-knowledge-prototype-agent | 7dejv/agents/7dejv-staw-knowledge-prototype-agent.md | True | False | False | 720b7433724c969a1444812156899988e2023f09 |
| niska | AGENT | airtable-agent | feat/airtable-product-workbook-agent-v0.1.0 | agent/AGENT.md | True | False | False | bdbc3b3f47ab35a1ec1b13024ddeabd289d806ca |
| niska | AGENTS_auditor | 7dejv-ai-command-center | main | agents/AGENTS_auditor.md | True | False | False | f89bd9435a44a255f4027b33723e96e242a485b8 |
| niska | AGENTS_codex_coordinator | 7dejv-ai-command-center | main | agents/AGENTS_codex_coordinator.md | True | False | False | aaf5fe77ad178069f4939c3d83bf1bf97dfcb52a |
| niska | AGENTS_docs_reporter | 7dejv-ai-command-center | main | agents/AGENTS_docs_reporter.md | True | False | False | e1e3c931131e55eeb8792961463f6aef0b435e9f |
| niska | AGENTS_dpdshipmvp | 7dejv-ai-command-center | main | agents/AGENTS_dpdshipmvp.md | True | False | False | 9e7e09978f2a10c51166ea4bc240759dbd5b4167 |
| niska | AGENTS_orderpanelmvp | 7dejv-ai-command-center | main | agents/AGENTS_orderpanelmvp.md | True | False | False | 45f0a6018c300e80d9c313a269c771ef002e1c6c |
| niska | AGENTS_prestashop | 7dejv-ai-command-center | main | agents/AGENTS_prestashop.md | True | False | False | f7c2d3f839c8fc910f7159ff400bed534ca60b25 |
| niska | AGENTS_security_guard | 7dejv-ai-command-center | main | agents/AGENTS_security_guard.md | True | False | False | 1286b88e5afd3d5d75e950fd9a24df3854ab821c |
| niska | external-tools-registry | 7dejv-skills-prompts | main | 03_agents/staw-expert-product-pipeline/external-tools-registry.md | False | False | False | ba01dcd07e0977a13fa522eda6a0e0c249b0b45a |
| prawdopodobna | 7dejv-allegro-offer-manager | 7dejv-skills-prompts | main | 7dejv/agents/7dejv-allegro-offer-manager.md | True | False | True | 2533e5a43c1fc2a6eb2fe235c176a151a9cca12d |
| prawdopodobna | 7dejv-baselinker-operator | 7dejv-skills-prompts | main | 7dejv/agents/7dejv-baselinker-operator.md | True | False | True | cdba0c60548626a1cb459160465d8755043e3153 |
| prawdopodobna | 7dejv-customer-service-agent | 7dejv-skills-prompts | main | 7dejv/agents/7dejv-customer-service-agent.md | True | False | True | a7b9fd773a38051ac1714af059dd9fa3ce101564 |
| prawdopodobna | 7dejv-pond-product-expert | 7dejv-skills-prompts | main | 7dejv/agents/7dejv-pond-product-expert.md | True | False | True | c58d0b7b996752b4e5222a018d5335d8ec07df81 |
| prawdopodobna | 7dejv-prestashop-developer | 7dejv-skills-prompts | main | 7dejv/agents/7dejv-prestashop-developer.md | True | False | True | d84498257af9f2c64e8879bc2787dbb5626809df |
| prawdopodobna | 7dejv-prestashop-performance-agent | 7dejv-skills-prompts | main | 7dejv/agents/7dejv-prestashop-performance-agent.md | True | False | True | 178dce24da972a8bd415629f4355397382f4f2b0 |
| prawdopodobna | 7dejv-procurement-agent | 7dejv-skills-prompts | main | 7dejv/agents/7dejv-procurement-agent.md | True | False | True | 4be9d0f63868f5d82d87e082861a6a8158e81ff3 |
| prawdopodobna | 7dejv-product-margin-analyst | 7dejv-skills-prompts | main | 7dejv/agents/7dejv-product-margin-analyst.md | True | False | True | 68ea704c1f5597e4dd8a588e01c3b0df505deb7a |
| prawdopodobna | 7dejv-seo-growth-agent | 7dejv-skills-prompts | main | 7dejv/agents/7dejv-seo-growth-agent.md | True | False | True | 2d7171214d2c16a1068af527d0ed8435fae87a82 |
| prawdopodobna | 7dejv-shipping-cost-auditor | 7dejv-skills-prompts | main | 7dejv/agents/7dejv-shipping-cost-auditor.md | True | False | True | 3ea5f0bbc57aae98670ba891172fd83b71cc5606 |
| prawdopodobna | 7dejv-sql-vat-reporter | 7dejv-skills-prompts | main | 7dejv/agents/7dejv-sql-vat-reporter.md | True | False | True | a6b23424aa94c5da53279f9ca1e15fa698da6a35 |