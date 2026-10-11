---
status: accepted
---

# Lua scripts read time from Redis, with an override for the conformance harness only

Every algorithm computes from the current time. If each application instance passed its own clock to the script, two instances with skewed clocks would disagree about which window a request falls in. Each script therefore calls Redis `TIME`, so all instances share one clock. A script also accepts an explicit time argument, which only the conformance harness supplies: without it, scripted timelines could not be replayed against Redis except with real sleeps, and window-boundary and rounding cases cannot be hit reliably that way.

## Considered Options

- **Always `TIME`, no override.** Scripts stay free of test-only code, but Redis conformance cases need real sleeps and become slow and timing-dependent.
- **Application passes its own clock.** Deterministic in tests, but reintroduces clock skew between instances in production. It would go unnoticed in a single-host Compose setup, where all containers share the host clock.

## Consequences

- Every script carries a branch that production never takes. The public limiter interface has no time parameter, so application code cannot take that branch by accident.
- Cases that supply the time do not exercise the `TIME` branch. The concurrency tests run without a supplied time and cover it.
