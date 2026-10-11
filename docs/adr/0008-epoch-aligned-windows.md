---
status: accepted
---

# Windows are aligned to the epoch, not to a caller's first request

A fixed window can start when a caller sends its first request, which is what the common `INCR` plus `EXPIRE` idiom produces, or on fixed boundaries derived from the clock. Sliding window counter needs fixed boundaries, because it weights the previous window against the current one. We use epoch-aligned boundaries for both window algorithms, so the window a request falls in is a function of the time alone and the two algorithms can be compared on identical boundaries.

## Consequences

- Fixed window allows up to twice the limit across a boundary, and with aligned windows that boundary is the same instant for every caller. This is the known weakness of the algorithm; it is demonstrated by a test rather than mitigated.
- All callers of a fixed window regain their allowance at the same instant, which can synchronise retries.
