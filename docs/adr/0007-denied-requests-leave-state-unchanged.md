---
status: accepted
---

# A denied request leaves limiter state unchanged

The shortest Redis implementations count every request, allowed or not: fixed window as a bare `INCR`, sliding window log by adding the entry before counting. With that behaviour a caller that keeps retrying while denied extends its own denial, in sliding window log indefinitely, and the reported retry-after is wrong the moment the caller retries. We record a request only when it is allowed. Each script therefore reads and decides before it writes, which costs a few more lines than the counting form.

## Consequences

- Retry-after is a promise the engine keeps: a caller that waits that long and sends one request is allowed, however many denied attempts it made in between and provided no other request for the same key arrives first.
- Denied attempts are invisible in limiter state, so the engine cannot by itself penalise callers that ignore retry-after.
