from Bio import SeqIO

records = SeqIO.parse("sample.fasta", "fasta")
data = [str(record.seq) for record in records]


def substring(long, short):
    l = len(short) // 2

    def combine(a, b):
        return a[: a.index(b[:l])] + b

    if short[:l] in long:
        return combine(long, short)
    elif long[:l] in short:
        return combine(short, long)


ans = data.pop()
while data:
    for seq1 in data:
        if substring(ans, seq1):
            ans = substring(ans, seq1)
            data.remove(seq1)
            break
print(ans)
