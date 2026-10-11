---
status: accepted
---

# All limiter arithmetic is integer, with time in microseconds

The conformance suite requires the in-memory and Redis backends to return identical decisions, and Lua numbers are IEEE doubles while Python separates integers from floats. Floating-point arithmetic is not guaranteed to round the same way in both, so both backends compute only with integers: time is a whole number of microseconds (the resolution of Redis `TIME`), and state that would be fractional, such as a partially refilled token, is stored scaled by the window so that no fraction arises. A decision reports retry-after in microseconds; rounding up to whole seconds happens once, where the HTTP header is written.

## Consequences

- A double represents integers exactly only below 2^53. A quota whose limit multiplied by its window in microseconds reaches that bound is rejected when the limiter is constructed.
- The Python reference is written in the scaled-integer form the Lua script must follow, which is less direct than the textbook floating-point formulation of token bucket and sliding window counter.
