# Playbook: Managing Role Prompts

status: Draft
version: 0.1.0
compatibility:
  node: ">=20"
  python: ">=3.10"
changelog:
  - version: 0.1.0
    date: 2025-08-03
    notes: Initial draft for adding role prompt files.

## Purpose
Guide contributors on creating role-specific prompt files in `/ai/Prompts`.

## Steps
1. Create `<role>.md` under `/ai/Prompts`.
2. Begin with a `## System` heading describing the role.
3. Include shared guidance via `@include: ./common.md`.
4. Add role-specific instructions.
5. Update `AGENTS.md` or relevant README to document the new role files.
6. Execute `npm run lint && npm run typecheck && npm test -- --ci`.
7. Record the change in `/ai/Runs/<date>/run-<date>-<seq>.yaml` referencing this Playbook.
