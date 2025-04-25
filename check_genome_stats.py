from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

fasta = "schMed_chr_and_mtDNA.fasta"
total_len = 0
gc_count  = 0

for rec in SeqIO.parse(fasta, "fasta"):
    seq = str(rec.seq).upper()
    total_len += len(seq)
    # count G + C
    gc_count  += seq.count("G") + seq.count("C")

gc_frac = gc_count / total_len
at_frac = 1 - gc_frac

print(f"Genome size: {total_len:,} bp")
print(f"GC content:  {gc_frac*100:.2f}%")
print(f"AT content:  {at_frac*100:.2f}%")
print(f"AT : GC ratio ≈ {at_frac/gc_frac:.2f}:1")
