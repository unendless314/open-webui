<!--
Copy this template to GUARDRAILS.md and customize for your project.
Common items to adjust:
- Paths the agent must not touch
- Required pre-PR test commands
- PR checklist items
-->
# Guardrails

## Never Touch
- /infra/**
- /secrets/**
- /migrations/manual/**
- <add project-specific paths>

## Must Run Before PR
- `npm run lint && npm run typecheck && npm test -- --ci`
- <add project-specific test commands>

## PR Checklist (Agent must verify)
- [ ] Link at least one ADR or Playbook
- [ ] Attach test or benchmark evidence
- [ ] If change exceeds 500 lines, split into multiple PRs
- [ ] <add project-specific checks>
