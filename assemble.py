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

    Input: list (Array) - an array of reads. k_length (Int) - the length of the k-mer.
    Output: k_mers (Array) - the list of all possible k-mers for each read in
            the input array.
    """
    k_mers = []
    for read in range(len(list)):
        for i in range(len(list[read]) - k_length):
            k_mer = list[read][i:i+k_length]
            k_mers.append(k_mer)
    return k_mers

def build_de_bruijn_graph(k_mer_list, k_length):
    """
    Takes a k-mer list and length of k-mers as parameters and returns the number
    of verticies and edges for the constructed graph.

    Input: k_mer_list (Array) - list of all possible k-mers from a list of reads.
           k_length (Int) - the length of the k-mer.
    Output: result (Array) - a list which represents [# of verticies, # of edges]
            for the De Bruijn Graph.
    """
    result = []

    V = compute_k_mers(k_mer_list, k_length - 1)
    
    return result
def main():

    import sys

    """Parse the reads and k-mer length parameters"""
    reads = read_single_fasta(sys.argv[1])
    k = int(sys.argv[2])

    k_mer_list = compute_k_mers(reads, k)
    print "k-mers list:", k_mer_list
    de_bruijn_graph = build_de_bruijn_graph(k_mer_list,k)

    # print "Number of verticies in graph: ", de_bruijn_graph[0]
    # print "Number of edges in graph: ", de_bruijn_graph[1]


if __name__ == '__main__':
    main()
