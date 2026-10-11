---
status: accepted
---

# Standalone Redis, with every script touching exactly one key

The engine runs and is tested against a single standalone Redis. On Redis Cluster, all keys a Lua script touches must hash to the same slot, which normally means designing key names around hash tags. We avoid that problem instead of solving it: all state for one limiter key lives in one Redis key, using a hash where an algorithm needs several values, so every script is single-key and has no slot constraint.

## Consequences

- Algorithms that are usually written with two keys, such as sliding window counter with one counter per window, keep both values in one hash.
- Nothing in the scripts rules out Cluster, but Cluster is untested and unsupported. Failover behaviour, where a replica may lag the primary and briefly allow more than the quota, is not addressed.
