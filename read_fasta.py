import sys

def read_fasta(filename):
    """
    Read sequence data from FASTA file. Filename as command line arg
    """
    seq =''
    f = open(filename)
    for line in f:
        line = line.strip() # remove new line char ( lines read for file always have)
        if len(line)>0 and line[0] != '>': # check for empty line
            seq = seq + line  # concatenates line to seq
    f.close()
    return seq

if len(sys.argv) <2 :
	print('Usage:', sys.argv[0], 'sequence.fa')
	exit(1)

print(read_fasta(sys.argv[1]))

