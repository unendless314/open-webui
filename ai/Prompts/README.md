# Role Prompts

This directory stores prompt templates for each agent role.

## Naming Convention
- Use lowercase kebab-case filenames: `<role>.md`.
- Common guidance lives in `common.md` and can be shared via `@include: ./common.md`.
- Add new role files by following the [Managing Role Prompts Playbook](../Playbooks/role-prompts.md).

## Roles
| File | Purpose |
|------|---------|
| `builder.md` | Guides the Builder when creating or modifying code. |
| `reviewer.md` | Guides the Reviewer to evaluate changes against ADRs, Playbooks, and policies. |
| `tester.md` | Guides the Tester to run project checks and report failures. |

## Example Structure
```markdown
## System
You are the <Role>. Briefly describe the responsibilities.
@include: ./common.md
```

Shared fields or formats should mirror the playbook and can reference `common.md` for reusable guidance.
