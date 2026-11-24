# Traced outputs at height 9,999

`live_outputs_9999.jsonl` lists every unspent output after the first 10,000 blocks (heights 0 to 9,999), one per line:

    {"txid": ..., "vout": ..., "value": ..., "runs": [[height, coinbase_output, sats], ...]}

`value` is in satoshis. Each run is a stretch of the output's satoshis, in first-in-first-out order, with the height of
the block whose coinbase output mined them and that output's index. The runs of an output add up to its value.

The file has 9,494 outputs and 10,021 runs, the counts of the state digest `80e12550bcd736b3423665e4284dda63` in
`../results/test_first_10k.log`, and its values add up to exactly 500,000 BTC, the subsidy of the 10,000 blocks. Most
outputs are unspent coinbases with one run. The 48 outputs with more than one run are where transactions merged coins:
for example output 0 of transaction
`e6f00fa63eb6b8e812ac3c591871203cae971d480c1469fc5ce88932cd3ec26c` holds 2,400 BTC in 48 runs from 48 blocks mined
between heights 6,338 and 7,235. Two blocks do not hold exactly their subsidy: block 2,676 holds 2.01 BTC less and block
2,817 holds 2.01 BTC more. Under the fee-stopping rule a fee counts as a new coin of the block that collects it, so
2.01 BTC paid as a fee moved from one block to the other; the totals agree.

The list is by transaction output. No address is named and no addresses are clustered.

# One output traced back at height 57,043

`multihop_57043.json` follows output 0 of transaction
`a1075db55d416d3ca199f55b6084e2115b9345e16c5cf302fc80e9d5fbf5d48d`, mined at height 57,043, which pays 10,000 BTC from
131 inputs:

    {"txid": ..., "vout": 0, "height": 57043, "value": ..., "inputs": 131, "nruns": 952, "runs": [[height, sats], ...], "hops": {...}}

Its 10,000 BTC fall into 952 runs from coinbases of 211 blocks mined between heights 24,097 and 56,787. 181 runs are
whole 50 BTC coinbases, and the other 950 BTC arrive in 771 smaller pieces, many of 0.01 or 0.02 BTC. For each run,
`hops` counts the transactions its satoshis passed through after leaving the coinbase, this one included. The median run
passed through 185 transactions and the longest through 1,005: a chain of 1,005 transactions confirmed in 12 blocks
between heights 51,646 and 57,043, each spending an output of the one before. Only 122 runs went through two
transactions, a coinbase output spent once and then spent here.

The state at height 57,043 has digest `26b1f215ab44e3b0f58068bd0f62ebf2` (45,393 live outputs, 59,901 runs). The states
computed on the way at heights 19,999 to 59,999 equal the rows in `../results/rows_fifo_native_0_320043.jsonl`. The 952
runs also agree with a direct first-in-first-out walk back through the raw blocks from the 131 inputs. As above, no
address is named and no addresses are clustered.
