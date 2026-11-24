"""The era and 10,000-block tables of origin_mix.py, recomputed from a saved origin array and a srcmap.
usage: python3 tables_from_npy.py ORIGIN_NPY SRCMAP H"""
import sys
import numpy as np

tot = np.load(sys.argv[1]); H = int(sys.argv[3])
b = np.fromfile(sys.argv[2], dtype="<u8").astype(np.int64)
Hs, Ss, Ns = np.arange(len(b) - 1), b[:-1], np.diff(b)
ids = np.nonzero(tot)[0]
i = np.searchsorted(Ss, ids, side="right") - 1
mapped = (i >= 0) & (ids < Ss[np.maximum(i, 0)] + Ns[np.maximum(i, 0)])
hgt = np.where(mapped, Hs[np.maximum(i, 0)], -1)
w = tot[ids]
T = w.sum()
print("total %d sats" % T)
print("mapped to a block: %.2f%% of live sats (%d of %d sources with live sats)" % (100 * w[mapped].sum() / T, mapped.sum(), len(ids)))
for e in range(H // 210000 + 1):
    m = mapped & (hgt >= 210000 * e) & (hgt < 210000 * (e + 1))
    print("  era %d %6.2f%%  %16.8f BTC" % (e + 1, 100 * w[m].sum() / T, w[m].sum() / 1e8))
print("  not mapped %6.2f%%  %16.8f BTC" % (100 * w[~mapped].sum() / T, w[~mapped].sum() / 1e8))
for lo in range(0, H + 1, 10000):
    m = mapped & (hgt >= lo) & (hgt < lo + 10000)
    print("  %6d-%6d %6.2f%%" % (lo, min(lo + 9999, H), 100 * w[m].sum() / T))
