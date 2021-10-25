"""
    Author: Maya Murphy, 22'
    Carleton College, Layla Oesper (Professor)

    This program constructs a Debruijn Graph for a set of reads.
"""

def read_single_fasta(filename):
    """
    Reads in a single fasta file (only contains one sequence) and returns
    the sequence from the file as one line.

    Input: filename (String) - the name of the fasta file to read.  The
            sequence may be on multiple lines in the fasta file.
    Output: sequence (String) - a single string representing the sequence in
            the fasta file.
    """
    reads = []
    with open(filename) as f:
        lines = f.readlines()
        for x in lines:
            x = x.rstrip("\n")
            reads.append(x)
    return reads



def compute_k_mers(list, k_length):
    """
    Takes a list and length of k-mer as parameters and returns a list of k-mers
    from the list.

    Input: list (Array) - an array of reads. k-mer (Int) - the length of the k-mer.
    Output: k_mers (Array) - the list of all possible k-mers for each read in
            the input array.
    """
    k_mers = []

    print "list of reads: ", list
    print "k length: ", k_length
    print ""

    for read in range(len(list)):
        print "read: ", read
        print "list[read]: ", list[read]
        for i in range(len(list[read]) - k_length):
            print "list[read][i:i+k_length]: ", list[read][i:i+k_length]
            k_mer = list[read][i:i+k_length]
            k_mers.append(k_mer)
        print ""
    print "length of input list: ", len(list)
    return k_mers


def main():

    import sys

    """Parse the reads and k-mer length parameters"""
    reads = read_single_fasta(sys.argv[1])
    k = int(sys.argv[2])

    print "k-mers list:", compute_k_mers(reads, k)


if __name__ == '__main__':
    main()
