---
status: accepted
---

# Every algorithm is configured by the same quota: a limit and a window

Token bucket and leaking bucket are conventionally configured by a capacity and a rate, the window algorithms by a limit and a window. We configure all five by one quota, a limit per window: for the bucket algorithms the capacity is the limit and the rate is limit per window. This makes the algorithms interchangeable under one configuration, lets one set of conformance timelines apply to all of them, and makes their behaviour directly comparable for the same quota.

## Consequences

- The burst size of a bucket cannot be set independently of its sustained rate. A quota of 100 per minute always permits a burst of 100.
- Every request costs one unit. Weighted requests are not supported.
