import re

CODON_TABLE = {
    'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
    'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
    'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
    'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
    'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
    'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
    'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
    'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
    'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
    'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
    'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
    'TAC': 'Y', 'TAT': 'Y', 'TAA': '_', 'TAG': '_',  # _ = Stop codon
    'TGC': 'C', 'TGT': 'C', 'TGA': '_', 'TGG': 'W',
}


def crop_sequence(seq: str, start: int, end: int) -> str:
    """
    Crop a DNA sequence from index start to end (end not inclusive).

    Parameters:
    seq (str): DNA sequence.
    start (int): Start index.
    end (int): End index.

    Returns:
    str: Cropped DNA sequence.
    """
    return seq[start:end]


def reverse_sequence(seq: str) -> str:
    """
    Reverses the input DNA sequence.

    Args:
        seq (str): DNA sequence (string of A, T, C, G)

    Returns:
        str: Reversed DNA sequence
    """
    return seq[::-1]


def reverse_complement(seq: str) -> str:
    """
    Returns the reverse complement of a DNA sequence.

    Args:
        seq (str): DNA sequence (A, T, C, G)

    Returns:
        str: Reverse complement of the sequence
    """
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement.get(base, base) for base in reverse_sequence(seq.upper()))


def find_pattern(seq: str, pattern: str) -> list:
    """
    Find all start positions of a pattern in the DNA sequence using regex.

    Parameters:
    seq (str): DNA sequence.
    pattern (str): Regex pattern to search.

    Returns:
    list: List of starting indices where the pattern occurs.
    """
    matches = [match.start() for match in re.finditer(f'(?={pattern})', seq)]
    return matches


def translate_dna_to_protein(dna_sequence):
    """
    Translates a DNA sequence into a protein sequence.
    Non-complete codons at the end are ignored.

    Args:
        dna_sequence (str): DNA sequence (string of A, T, C, G)

    Returns:
        protein_sequence (str): Protein sequence (string of amino acids)
    """
    dna_sequence = dna_sequence.upper().replace('\n', '').replace(' ', '')
    protein_sequence = ''

    for i in range(0, len(dna_sequence) - 2, 3):  # Step in triplets
        codon = dna_sequence[i:i + 3]
        amino_acid = CODON_TABLE.get(codon, 'X')  # 'X' = unknown codon
        protein_sequence += amino_acid

    return protein_sequence


def detect_mutations(reference_seq, sample_seq):
    """
    Detects mutations between a reference and a sample DNA sequence.

    Args:
        reference_seq (str): The reference DNA sequence.
        sample_seq (str): The sample DNA sequence to compare.

    Returns:
        mutations (list): List of mutation descriptions.
    """
    reference_seq = reference_seq.upper().replace('\n', '').replace(' ', '')
    sample_seq = sample_seq.upper().replace('\n', '').replace(' ', '')

    mutations = []
    min_len = min(len(reference_seq), len(sample_seq))

    # Check for substitutions
    for i in range(min_len):
        ref_base = reference_seq[i]
        sample_base = sample_seq[i]
        if ref_base != sample_base:
            mutations.append(f"Substitution at position {i + 1}: {ref_base} -> {sample_base}")

    # Check for insertions
    if len(sample_seq) > len(reference_seq):
        inserted_seq = sample_seq[min_len:]
        mutations.append(f"Insertion at position {min_len + 1}: {inserted_seq}")

    # Check for deletions
    if len(reference_seq) > len(sample_seq):
        deleted_seq = reference_seq[min_len:]
        mutations.append(f"Deletion at position {min_len + 1}: {deleted_seq}")

    return mutations
