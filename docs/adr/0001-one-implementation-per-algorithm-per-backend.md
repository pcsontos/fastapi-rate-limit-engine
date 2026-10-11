---
status: accepted
---

# One implementation per algorithm per backend, with no storage abstraction

A rate limit decision is read, decide, write. On Redis those three steps must run as one atomic Lua script, otherwise two application instances can both read the same state and both allow a request. Once the whole decision runs inside the script, there is no algorithm left on the Python side, so a generic storage interface (`get`, `incr`, `expire`) that Python algorithm classes compose with cannot be made correct. We therefore write each of the five algorithms twice, once in Python for the in-memory backend and once in Lua for the Redis backend, behind a single limiter interface. The source tree is grouped by backend (`backends/memory/`, `backends/redis/`) so the layout states this.

## Considered Options

- **Storage abstraction with Python algorithms.** Five algorithm classes over two interchangeable stores. Rejected: the gap between separate Redis commands is the race this project exists to remove.
- **Distributed lock around the Python algorithm.** Rejected: extra round trips per request, plus lock expiry and crash handling.
- **`WATCH`/`MULTI`/`EXEC`.** Rejected: it retries on conflict, and a rate limiter sees the most conflicts exactly when it is under load.
- **Group the tree by algorithm.** Rejected: code is shared within a backend (connection handling, script loading, reply parsing), not between the Python and Lua versions of one algorithm.

## Consequences

- The logic of every algorithm exists in two languages and nothing in the type system keeps the copies in agreement. A conformance suite replays the same scripted timelines against both backends and requires the full decision (allowed, limit, remaining, retry-after, reset-after) to be identical at every step, not only the allow/deny outcome. Remaining, retry-after and reset-after reach clients as headers, so a difference there is an observable difference.
- Exact equality forces identical arithmetic and rounding in Python and Lua.
- The in-memory backend is the reference: the readable specification and the test oracle. It has no idle-key expiry and no memory bound, and is not recommended for serving traffic.
