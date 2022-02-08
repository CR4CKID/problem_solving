from Bio import SwissProt
from Bio import ExPASy
import re

p = re.compile(r"N[^P][S|T][^P]")


def N_find(access):
    handle = ExPASy.get_sprot_raw(access)
    seq = SwissProt.read(handle).sequence
    ans = []
    while p.search(seq):
        idx = p.search(seq).start() + 1
        ans.append(idx)
        seq = seq[idx:]
    return ans


print(N_find("P07204_TRBM_HUMAN"))

