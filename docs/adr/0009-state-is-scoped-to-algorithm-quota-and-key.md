---
status: accepted
---

# Limiter state is scoped to the algorithm, the quota and the key

State stored for a key means different things under different algorithms and quotas: a counter under one window length is not a counter under another, and a token level is not a request log. Rather than define how existing state is reinterpreted when configuration changes, state is scoped to the combination of algorithm, quota and key. Changing a key's quota or algorithm starts from empty state, and the old state is left to expire.

## Consequences

- A caller whose quota changes receives one full allowance under the new quota, whatever it had consumed under the old one. A quota reduction therefore does not take effect against already-consumed usage.
- Two limiters with different quotas can be applied to the same key independently, for example a per-second and a per-hour quota.
