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
