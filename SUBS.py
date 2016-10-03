
from Bio import motifs
from Bio.Seq import Seq
import Bio.Alphabet

f = open("rosalind_subs.txt", 'r')
raw_seq = f.readline().rstrip()
motif = f.readline().rstrip()
f.close()

# motif instances must be in a list
instances = [Seq(motif)]
m = motifs.create(instances)

seq = Seq(raw_seq, Bio.Alphabet.IUPAC.unambiguous_dna)

# only output locations
locations = []
for pos in m.instances.search(seq):
    locations.append(pos[0]+1) # changes default from \n

o = open("SUBS.txt", 'w')
o.write(" ".join(map(str, locations)))
o.close()

