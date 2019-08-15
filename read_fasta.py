def read_fasta(filename):
    """
    Read sequence data from FASTA file in filename
    """
    seq =''
    f = open(filename)
    for line in f:
        line = line.strip() # remove new line char ( lines read for file always have)
        if len(line)>0 and line[0] != '>': # check for empty line
            seq = seq + line  # concatenates line to seq
    f.close()
    return seq
print(read_fasta('ae.fa'))
