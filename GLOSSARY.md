# Rate Limit Engine

A distributed rate limiting engine: it decides, per request, whether a caller is still within its allowance, and gives the same answer no matter which application instance asks.

## Language

**Algorithm**:
One of the five rules for deciding whether a request is within its allowance: token bucket, leaking bucket, fixed window, sliding window log, sliding window counter.
_Avoid_: Strategy, policy

**Backend**:
The place where limiter state lives and where an algorithm executes: in-memory or Redis.
_Avoid_: Storage, store

**Key**:
An opaque string naming whose allowance is being counted. The engine attaches no meaning to it.
_Avoid_: Client ID, identifier, subject

**Quota**:
An allowance of a number of requests (the limit) per span of time (the window). Every algorithm is configured by a quota and nothing else.
_Avoid_: Rate, rule, policy

**Limiter**:
One algorithm applied to one quota on one backend. It evaluates a request and records it in a single step.
_Avoid_: Rate limiter instance, throttle

**Reference backend**:
The in-memory backend, in its role as the readable specification of each algorithm and the oracle the Redis backend is checked against. It is not meant to serve production traffic.
_Avoid_: Local backend, fake, mock

**Decision**:
The outcome of evaluating one request: whether it is allowed, the limit, the remaining allowance, the retry-after and the reset-after.
_Avoid_: Result, verdict, response

**Remaining**:
The number of further requests that would be allowed at this instant if no time passed.
_Avoid_: Tokens left, available, balance

**Retry-after**:
The shortest wait after which one request would be allowed, provided no other request for the same key is allowed in the meantime. Zero for an allowed request.
_Avoid_: Backoff, cooldown, wait time

**Reset-after**:
The wait after which the full quota is available again, provided no further requests arrive.
_Avoid_: Reset time, window end, expiry

**Conformance case**:
A scripted timeline of requests at stated instants, for which every backend must return identical decisions at every step.
_Avoid_: Parity test, compatibility test

**Leaking bucket**:
The meter form of the algorithm: a request is allowed immediately if the bucket has room and denied otherwise. No request is ever delayed.
_Avoid_: Leaky bucket queue, traffic shaper
