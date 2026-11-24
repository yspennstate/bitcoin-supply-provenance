# Results

All figures use the fee-stopping rule stated in the paper.

## Height 396,249 (`origin_396249/`)

- `origin_src_396249.npy`: live satoshis per source (index = source number, int64), computed from the
  state at height 396,249 (34,113,505 live outputs, 173,668,290 runs; the runs sum to the live value).
- `srcmap_0_412499.bin`: the source map for heights 0 to 412,499 (entry h is the first source number of
  block h, the last entry closes the range).
- `tables.txt`: mapped share, era shares and the 10,000-block shares. Reproduce with
  `python3 tables_from_npy.py origin_src_396249.npy srcmap_0_412499.bin 396249`.
- `subsidy_audit.txt`: the head of the block-by-block subsidy audit at this height. Under fee-stopping a block's sources also hold the fees its coinbase collected, minus fees later paid out
  of them, so the per-block differences move in both directions; only their total is the shortfall against the subsidy.

## Two pipelines, heights 381,249 to 391,249 (`pipelines_381249_391249.tsv`)

The streaming pipeline runs the engine over the whole state. The incremental pipeline extracts the outputs the next
1,250 blocks touch, runs the same engine on that subset and writes the result back: at 381,249 into a full checkpoint
(subset and merge), from 382,499 into the sharded store, which from 383,749 on was carried only from its own previous
state. Both pipelines use the same engine, so the comparison tests the extraction, the merge and the store, not the
transfer rule. The incremental step itself (subset extraction and write-back) is not part of this release; these are
recorded results.

## Two implementations, heights 9,999 to 319,999

`rows_fifo_native_0_320043.jsonl` are the rows of the second C engine on blocks 0 to 320,043 (with digests).
`reference_rows_0_319999.json` are the rows of a separate Python implementation of the same rule at the 32 shared marks,
cut to the fields both report. It reads a different input format and is not released.
`python3 compare_rows.py rows_fifo_native_0_320043.jsonl reference_rows_0_319999.json` prints
`32 rows compared, 0 field differences`.

Row fields: `live_out` live outputs, `runs` runs held by them, `nsrc` sources (coinbase outputs, zero-value ones
included), `txs` transactions, `missing` inputs that spend an output not in the live set (the zero-value outputs, which
are never stored), `value_mismatch` outputs whose runs do not add up to the value (always 0), `dup_outputs` outputs
overwritten by a duplicate transaction (the two BIP 30 coinbases), `in_runs` the runs each transaction lays end to end from its inputs, summed over transactions, `run` the distribution
of runs per live output, `live_tx` transactions with a live output.

## Test on the first 10,000 blocks (`test_first_10k.log`)

An end-to-end run on blocks 0 to 9,999, macOS (Apple M4): both C engines (and the first built against CommonCrypto)
give the same digest, the digest read back from each checkpoint agrees, the store counts the same outputs, runs and
satoshis, the live value is exactly 10,000 x 50 BTC, and 300 sampled outputs give identical lines from the engine and
the store. The traced outputs in `../examples/` are from the same state.
