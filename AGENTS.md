# AGENTS Guidelines

## 0. Scope & Safety (READ FIRST)
- **Allowed repos/paths**: obey `/ai/Policies/GUARDRAILS.md` (never touch: `/infra/**`, `/secrets/**`, `/migrations/manual/**` unless ADR explicitly allows).
- **Allowed tools**: `gh`, project scripts, test runners; network ops only via approved tools.
- **Secrets/PII**: never print, store, or transmit. Redact in logs and PRs.

## 1. Start Here
- Read `/ai/README.md` for navigation and the decision flow.
- Search `/ai/ADR/0000-INDEX.md` and `/ai/Playbooks/` before coding. Prefer an existing ADR/Playbook over ad-hoc changes.

## 2. Environment & Reproducibility
- Default runtime: **Node ≥20** / **Python ≥3.10** (see Playbook `compat` for exact matrix).
- Respect lockfiles (`package-lock.json`, `poetry.lock`, etc.). Upgrading deps requires an ADR or a dedicated Playbook.
- **Run ID**: `run-YYYY-MM-DD-###` (e.g., `run-2025-08-03-001`). Each PR must reference at least one Run.

## 3. Execution Discipline
1. **Before work**  
   - Locate matching ADRs/Playbooks; **cite them** in your plan.
   - If none fits and the change looks repeatable → draft a Playbook proposal in the PR.
2. **After work**  
   - Write `/ai/Runs/<date>/<run-id>.yaml` including: `repo_sha`, `prompt_digest`, `tool_versions`, `cost`, and `refs` (`adrs`/`playbooks`/`policies`).
3. **Major decisions**  
   - Create an ADR from `ai/ADR/TEMPLATE.md` (`status: Proposed`, with `review_after` & `sunset_if`), then update `0000-INDEX.md`.
4. **Uncertain insights**  
   - Append to `Lessons/LESSONS.md` with tags. **Upgrade to ADR** after ≥2 successful Runs with evidence.
5. **Policies**  
   - Obey `/ai/Policies/GUARDRAILS.md`. **Violations invalidate Runs** and must be reverted.

## 4. Timeboxing & Escalation
- Stop and request human review when **any** occurs:
  - 2 consecutive CI failures for the same change,
  - >60 minutes wall-time without measurable progress,
  - touching guarded paths, or requiring policy exceptions.

## 5. Parallelization & Locks
- Use isolated branches (e.g., `feat/<scope>-<ticket>`). Prefer `git worktree` for multi-agent work.
- When editing the same subsystem, create a lightweight lock (e.g., label `lock:<subsystem>` or `/ai/Runs/<run-id>.lock`) and release on PR open/close.

## 6. PR Requirements
- Link **≥1** ADR or Playbook in the PR description.
- Include **tests/benchmarks** and **evidence** (links to CI, logs, screenshots if UI).
- Run locally before PR: `npm run lint && npm run typecheck && npm test -- --ci`.
- Provide **Risk** (low/med/high), **Impact**, and **Rollback plan**. Avoid drive-by refactors.
- Split PRs touching **>500 lines** or crossing module boundaries into smaller, logically scoped PRs.

## 7. Performance & Quality Budgets
- If the change affects performance/cost: state baseline, methodology, and thresholds (e.g., “p95 latency ±5%, token cost ≤ +3%”) in the PR.

## 8. Auto-Governance (CI)
- `.github/workflows/ai-governance.yml`:
  - Validates Run YAML against `ai/Runs/schema.yaml`.
  - Ensures `refs.adrs` or `refs.playbooks` is **non-empty**.
  - **Fails** if ADR index (`0000-INDEX.md`) is out of sync.
- ADR/Guardrails changes require **human approval** (CODEOWNERS + protected branches).

## 9. Common References
- **Glossary**: `/ai/GLOSSARY.md`.
- **Prompts**: `/ai/Prompts/common.md` + role-specific files (`builder.md`, `reviewer.md`, `tester.md`).
- **Playbooks**: versioned headers with compatibility matrix and changelog.

---

*Put temporary notes in /ai/TEMP-NOTES.md. Remove or refactor it after formal ADRs or playbooks have covered its content.*