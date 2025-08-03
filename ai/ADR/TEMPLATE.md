---
id: ADR-<auto or manual>
title: <short title>
status: Proposed  # Proposed | Accepted | Deprecated | Superseded
date: YYYY-MM-DD
review_after: YYYY-MM-DD      # review date
sunset_if:                    # sunset conditions
  - "Node LTS > 22 or perf regression > 10%"
evidence_strength: pilot|limited|strong
tags: [domain:<sub>, risk:<low|med|high>, scope:<code|infra|process>]
related_runs: []             # /ai/Runs/...yaml
related_playbooks: []        # /ai/Playbooks/...md
related_policies: []         # /ai/Policies/...md
owner: human|agent:<name>
---

## Context
<background, constraints, related modules or tickets>

## Decision
<chosen approach: actionable and verifiable>

## Consequences
<positive/negative effects, risks, rollback plan, monitoring metrics>

## Evidence
- PR/Commit: <links>
- Bench/Tests: <numbers>

## How to Apply
<implementation steps, corresponding Playbook>

## Alternatives Considered
<other options and reasons not chosen>
