---
status: accepted
---

# Leaking bucket is implemented as a meter, not as a queue

"Leaking bucket" names two algorithms. As a queue, admitted requests wait and are released at a constant rate, which shapes traffic. As a meter, a request is admitted immediately if the bucket has room and rejected otherwise. We implement the meter only, because this engine answers a request with allow or deny; a queue would have to hold HTTP requests open, add a delay to the decision that no other algorithm uses, and make correctness depend on timing.

## Consequences

- As a meter, leaking bucket is the mirror image of token bucket: one tracks how much is in the bucket and drains over time, the other tracks how much room is left and refills over time. For equal capacity and rate the two return the same decisions. This is intended, and the conformance suite asserts it.
- The engine does not smooth the rate at which admitted requests reach the application. A caller that needs a constant outflow needs a traffic shaper in front of the application.
