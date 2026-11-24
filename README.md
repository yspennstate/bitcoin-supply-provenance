# Bitcoin supply provenance

Yitzchak Shmalo

Every unspent satoshi of the Bitcoin chain, traced first-in-first-out through the transaction graph to the block that mined it or collected it as a fee, and the live supply reconciled against the issuance schedule. At height 396,249 (February 2016):

- 34,113,505 unspent outputs carrying 173,668,290 runs; 100.00% of the live value is assigned to a mining block.
- The live total is 110.19768818 BTC below the scheduled subsidy. 100 BTC are the coinbases of blocks 91,722 and 91,812, overwritten by the duplicate transactions of blocks 91,842 and 91,880 (BIP 30). The remaining 10.19768818 BTC is held by no live output (rewards left unclaimed by coinbase transactions are the known source of such a gap; listing it block by block needs the fee-carry rule). The genesis output is counted as live; under Bitcoin Core's convention, which leaves it out, the difference is 160.19768818 BTC.
- The full-state streaming run and an incremental pipeline (a subset run merged into a checkpoint at 381,249, the sharded store from 382,499) give the same state digest at nine heights from 381,249 to 391,249, and two separately written implementations of the transfer rule agree at every 10,000-block checkpoint to 319,999.
- The sharded store applies a stretch of 1,250 blocks writing 342 MB in 16 s, against 1,571 MB and 89 s for a whole-state rewrite, with the incremental step on one stretch using at most 0.40 GB of memory (the full-state streaming run peaks at about 5 GB at this height). The recorded results of each check are in `results/`; the engine and the store are not released.

The paper (`main.tex`, `main.pdf`) states the transfer rule, the results, the checks and the cost. No address is named and no addresses are clustered; the released tables are aggregates by block and by era.

## The overall goal

This repository is one application of a larger project: a persistent research memory that AI agents use to do mathematics and computation that can be checked.

- [Brain framework](https://github.com/yspennstate/brain-framework-public): the structure of a persistent multi-agent memory. Agents record claims, methods, failed attempts and tests, recall one another's work, coordinate who works on what, and audit each other.
- [Math Brain](https://github.com/yspennstate/math-brain-public): the same memory specialised to mathematical research, with its code and tests. The open-problem papers on this account were produced through it.
- This repository: the memory applied to Bitcoin provenance. The ledger engines, the store and the checks were written and run by AI agents working inside the framework. The plan for the next stage is to use the memory so that each change to the engine is tested against every earlier failure and every earlier check.

The next step is to carry the reconciliation from height 396,249 to the chain tip (near 976,000) with the fee-carry rule, which assigns transaction fees to the coinbase that collects them and so lists the unclaimed rewards block by block. The run count grows faster than the output count (from 396,249 to 412,499 the outputs grow 12% and the runs 19%, and the fee-carry rule has more runs again), so this needs a full node and more memory and disk than the 16 GB Apple Mac mini the work runs on now.

## Contents

- `main.tex`, `main.pdf`: the paper.
- `results/`: the state and tables at 396,249, the pipeline and implementation comparisons, the test log (`results/README.md`).
- `examples/`: outputs of the first 10,000 blocks traced to the blocks that mined their coins.
- `LICENSE`: CC BY 4.0 for the paper, the text and the tables; MIT for the two small scripts in `results/`.

## Licence

CC BY 4.0 for the paper, the text and the tables; MIT for the two scripts in `results/`.
