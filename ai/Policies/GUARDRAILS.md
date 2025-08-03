# Guardrails
## Never Touch
- /infra/**
- /secrets/**
- /migrations/manual/**

## Must Run Before PR
- `npm run lint && npm run typecheck && npm test -- --ci`

## PR Checklist (Agent must verify)
- [ ] Link at least one ADR or Playbook
- [ ] Attach test or benchmark evidence
- [ ] If change exceeds 500 lines, split into multiple PRs
