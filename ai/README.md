# AI Folder Guide

## Quick Paths
| Goal | Read First | Then | Output |
|---|---|---|---|
| Solve one-off task | /ai/Playbooks | follow steps | /ai/Runs/<run>.yaml |
| Establish long-term rule | /ai/ADR/0000-INDEX.md | draft new ADR | ADR PR |
| Unsure if worth ADR | /ai/Lessons/LESSONS.md | record lesson | evaluate later |

```mermaid
flowchart TD
A[Start Task] --> B{Playbook exists?}
B -- Yes --> C[Follow Playbook]
B -- No --> D{Long-term decision?}
D -- Yes --> E[Draft ADR (Proposed)]
D -- No --> F[Log Lesson]
C --> G[Create Run YAML]
E --> G
F --> G
G --> H{Result stable?}
H -- Yes --> I[Promote to Playbook or Accept ADR]
H -- No --> J[Keep in Lessons / observe]
```
