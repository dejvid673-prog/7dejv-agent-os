# 7DEJV Project State Policy

Status: canonical

## Purpose

Every multi-stage project must have a persistent state artifact in the project repository. Conversation state is not sufficient.

## Required state

The project state must record:

- project goal;
- current stage;
- scope IN/OUT;
- acceptance criteria summary;
- feature matrix progress;
- active blockers;
- known regressions;
- latest verified baseline commit/ref;
- evidence references;
- next executable step;
- completion status.

## Update rule

Update project state after every stage, material implementation batch, failed verification, blocker, scope decision and completion gate.

## Resume rule

Before continuing an existing project, read repository state first. Do not reconstruct project progress only from chat history.

## Completion rule

Project state may declare `DONE` only when the global Definition of Done passes.
