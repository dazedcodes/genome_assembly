"""
    Author: Maya Murphy, 22'
    Carleton College, Layla Oesper (Professor)

    This program simulates the process of sampling reads from a longer set of
    DNA.

"""
import random

def read_single_fasta(filename):
    """
    Reads in a single fasta file (only contains one sequence) and returns
    the sequence from the file as one line.

    Input: filename (String) - the name of the fasta file to read.  The
            sequence may be on multiple lines in the fasta file.
    Output: sequence (String) - a single string representing the sequence in
            the fasta file.
    """
    sequence = ""
    with open(filename) as f:
        lines = f.readlines()
        lines = lines[1:]
        for x in lines:
            x = x.rstrip("\n")
            sequence += x
    sequence = sequence.upper()
    return sequence

def compute_N(genome_length,coverage,length):
    """
    Uses the Lander-Waterman statistics to compute the value of N.

    Input: genome_length, coverage, and length of reads (Int, Int, Int)
    Output: N (Int) - number of reads to simulate (Int)

    """
    return int((coverage*genome_length)/length)

def generate_random(number):
    """
    Takes in a number as input and returns a random number from 0 to number.

    Input: number (Int) - takes in the length of the genome.
    Output: random_num (Int) - returns the random place in genome to begin
            simulation.

    """
    random_num = random.randint(0,number-1)
    return random_num

def equal_probability(x,y,z):
    """
    Takes in three characters x, y, and z as paramters and returns one of the
    characters with an equal equal_probability.

    Input: x (String), y (String), z (String) - three characters
    Output: result (String) - one of the three characters with respect to the
            probabilty of the three.
    """
    result = ""
    prob = random.uniform(0.0, 1.0)
    if (prob > 0.0) & (prob < 0.30):
        result += x
    if (prob > 0.31) & (prob < 0.60):
        result += y
    if (prob > 0.61) & (prob < 1.0):
        result += z

    return result

def random_char(character):
    """
    Takes in a character as a parameter and returns a character not equal to the
    original from a alphabet of either A, C, T, and G.

    Input: character (String) - a character that's either an A, C, T, or G.
    Output: new_character (String) - a character that's not equal to the
            original from an alphabet of A, C, T, and G.
    """
    new_character = ""
    if character == "A":
        new_character += equal_probability("T","C","G")
    if character == "C":
        new_character += equal_probability("A","T","G")
    if character == "T":
        new_character += equal_probability("A","C","G")
    if character == "G":
        new_character += equal_probability("T","C","A")
    return new_character

def error_prob(string,error):
    """
    Takes in a string and error rate as parameters and returns the string
    where each character in the string has a error probabilty of being replaced
    with the wrong character.

    Input: string (String) - the substring to factor error into and error
           (float) - the error rate probabilty for incorrectly reading a string.
    Output: string (String) - the string with error probabilty factored into it.
    """
    new_string = ""
    for char in range(len(string)):
        num = random.uniform(0.0,1.0)
        if num < error:
            new_char = random_char(string[char])
            new_string += new_char
        else:
            new_string += string[char]
    return new_string

def simulate_reads(sequence, count, length, error, read_range):
    """
    Takes in a DNA sequence, the number of reads to complete, specified length
    for reads, error rate, range as parameters and returns a list of all of the
    reads computed.

    Input: the DNA sequence (String), the number of reads to complete (Int), the
           length for each read (Int), the error rate (float), and range to
           compute reads (Int).
    Output: list (Array) - list of the reads simulated for genome assembly.

    """
    list = []
    for read in range(1,count+1):
        start_read_index = generate_random(read_range)
        substring = sequence[start_read_index:start_read_index+length]
        error_substring = error_prob(substring, error)
        list.append(error_substring)
    return list

def print_reads(list):
    """
    Takes in a list of reads separated by commas as a parameter and returns each
    simulated read as a separate line.

    Input: list (Array) - a list of reads length L separated by commas.
    Output: Each simulated read printed out on a new line.

    """
    for read in list:
        print read

def main():

    import sys

    """Parse variables G, C, L, and error rate for DNA simulation"""
    sequence = read_single_fasta(sys.argv[1])
    G = int(len(sequence))
    C = int(sys.argv[2])
    L = int(sys.argv[3])
    error_rate = float(sys.argv[4])

    N = compute_N(G,C,L)

    read_range = (G-1) - L # range so that a read contains exactly L chars
    reads_list = simulate_reads(sequence, N, L, error_rate, read_range)
    print_reads(reads_list)

if __name__ == '__main__':
    main()
