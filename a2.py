def get_length(dna):
    ''' (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    '''
    return len(dna)


def is_longer(dna1, dna2):
    ''' (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    '''
    
    b = (len(dna1) > len(dna2))
    return b


def count_nucleotides(dna, nucleotide):
    ''' (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    '''
    return dna.count(nucleotide)


def contains_sequence(dna1, dna2):
    ''' (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False
    
    '''

    if (dna1.find(dna2) == -1):
        return False
    else:
        return True




def is_valid_sequence(dna):
    ''' (str) -> bool

    Return True if and only if DNA sequence is a valid DNA sequence
    else returns False.

    >>> is_valid_sequence('ATCGGCTGC')
    True
    >>> is_valid_sequence('ATCGGHIJN')
    False
    '''

    for char in dna:
        if char not in 'ATCG':
            return False

    return True


def insert_sequence(dna1,dna2,index):
    '''(str, str, int) -> str

    Return a DNA sequence by appending the DNA2 sequence in DNA1 sequence
    at the index given

    >>> insert_sequence('CCGG', 'AT',2)
    'CCATGG'
    >>> insert_sequence('CCGG', 'AT',-1)
    'CCGATG'    
    '''

    dna = dna1[:index]+dna2+dna1[index:]
    return dna


def get_complement(nucleotide):
    '''(str) -> str

    Return the complement of the nucleotide.

    >>> get_complement('A')
    'T'
    >>> get_complement('C')
    'G'
    '''

    if(nucleotide == 'A'):
        return 'T'
    elif(nucleotide == 'T'):
        return 'A'
    elif(nucleotide == 'C'):
        return 'G'
    else:
        return 'C'
    

def get_complementary_sequence(dna):
    '''(str) -> str

    Return a complementary sequence of the given DNA sequence.

    >>> get_complementary_sequence('AT')
    'TA'
    >>> get_complementary_sequence('CTGATGC')
    'GACTACG'
    '''

    com_dna=''
    
    for char in dna:
        com_dna = com_dna + get_complement(char)

    return com_dna
