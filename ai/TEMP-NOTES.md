# TEMPORARY NOTES – May delete or merge later
**Purpose:** transient scratchpad for AI assistants to track decisions/TODOs.

## Findings
- Need CI workflow `.github/workflows/ai-governance.yml` with ADR index and Run schema checks.
- Runs must link at least one ADR or Playbook; missing links should fail CI.
- ADRs require `review_after` and `sunset_if` fields for clarity and retirement.

## TODOs
- [ ] Add base `/ai` structure (ADR, Runs, Lessons, Playbooks, Policies, Prompts, Glossary, README).
- [ ] Implement `schema.yaml` for Runs with cost, tool versions, refs, evidence.
- [ ] Create `Policies/GUARDRAILS.md` to list forbidden paths and mandatory tests.
- [ ] Draft `Prompts/common.md` and role-specific prompts using `@include` tags.
- [ ] Establish `Lessons/LESSONS.md` with tagging rules and upgrade criteria.

*This file is temporary; feel free to append, refactor, or remove once formal ADRs/Playbooks cover these points.*
