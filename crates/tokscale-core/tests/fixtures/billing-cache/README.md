# Frozen legacy cache fixtures

These are synthetic Linux x86_64 bincode 1.3.3 (`bincode::options()`) bytes generated from the ordered wire declarations at `bd62b8c4e07269e5314fac06c6d23262dc714633`. They are not produced with the current `UnifiedMessage`, so adding a field cannot silently update the expected layout.

Generic envelopes v4–v10 use their released message layouts. MiCode v8–v11 use the corresponding v7–v10 entry inside `Vec<(Entry, Option<Vec<MiMoRowMetadata>>)>`. Every entry contains estimated $7.25, authoritative $0 and authoritative $0.375 fictional rows. Token buckets, fractional row timestamp bits, parent linkage and retention markers verify field alignment. Optional incremental-state slots are `None`; existing cache unit tests cover populated incremental states.

Fixtures contain no real user data or credentials. The loader test reads each original without modifying it, rewrites to the current format, then reads the new file warm and compares messages and MiCode provenance.
