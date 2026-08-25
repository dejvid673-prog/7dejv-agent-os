# Tasks

This directory defines the coordination contract for work performed by multiple ChatGPT/Codex/agent instances.

## State machine

`BACKLOG -> CLAIMED -> IN_PROGRESS -> VERIFY -> PASSED -> DONE`

Any active state may move to `BLOCKED` when a material dependency, safety issue or missing evidence prevents progression.

## Ownership

1. One task has one current owner.
2. `CLAIMED` reserves the task before implementation begins.
3. Another agent must not modify the same task scope without an explicit handoff or owner release.
4. Non-trivial code/repository changes use a dedicated branch.
5. Parallel work is allowed only when scopes do not overlap or when coordination is explicitly documented.

## Required task fields

Task records must satisfy `schemas/task.schema.json` and include at least:

- id and title;
- status and owner;
- repository and branch;
- goal and bounded scope;
- acceptance criteria;
- evidence references.

## Handoff

A handoff must state:

- current status;
- branch/ref;
- files changed;
- validations/tests actually run;
- known failures and risks;
- exact next action;
- new owner when known.

Completion claims without evidence remain `VERIFY` or `HOLD`; they do not become `DONE` automatically.
