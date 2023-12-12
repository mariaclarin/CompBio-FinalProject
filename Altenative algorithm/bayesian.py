def calculate_likelihood(dna_sequence, probability_table):
    likelihood = 1.0
    for nucleotide in dna_sequence:
        likelihood *= probability_table[nucleotide]
    return likelihood

def paternity_test(child_dna, father_dna):
    probability_table = {
        'A': 0.25,
        'T': 0.25,
        'C': 0.25,
        'G': 0.25
    }

    likelihood_true_father = calculate_likelihood(child_dna, probability_table)
    likelihood_not_true_father = calculate_likelihood(father_dna, probability_table)

    prior_probability = 0.5
    posterior_true_father = (likelihood_true_father * prior_probability) / \
                            ((likelihood_true_father * prior_probability) + (likelihood_not_true_father * (1 - prior_probability)))

    return posterior_true_father

child_dna = "GATCACAGGTCTATCACCCTATTAACCACTCACGGGAGCTCTCCATGCATTTGGTATTTTCGTCTGGGGGGTGTGCACGCGATAGCATTGCGAGACGCTGGAGCCGGAGCACCCTATGTCGCAGTATCTGTCTTTGATTCCTGCCTCATCCTATTATTTATCGCACCTACGTTCAATATTACAGGCGAACATACTTACTAAAGTGTGTTAATTAATTAATGCTTGTAGGACATAATAATAACAATTGAATGTCTGCACAGCCGCTTTCCACACAGACATCATAACAAAAAATTTCCACCAAACCCCCCCCTCCCCCCGCTTCTGGCCACAGCACTTAAACACATCTCTGCCAAACCCCAAAAACAAAGAACCCTAACACCAGCCT"
father_dna = "CCAATGATATGAAAAACCATCGTTGTATTTCAACTACAAGAACACCAATGACCCCAATACGCAAAATTAACCCCCTAATAAAACTAATTAACCACTCATTCATCGACCTCCCCACCCCATCCAACATCTCCGCATGATGAAACTTCGGCTCACTCCTTGGCGCCTGCCTGATCCTCCAAATCACCACAGGACTATTCCTAGCCATGCACTACTCACCAGACGCCTCAACCGCCTTTTCATCAATCGCCCACATCACTCGAGACGTAAATTATGGCTGAATCATCCGCTACCTTCACGCCAATGGCGCCTCAATATTCTTTATCTGCCTCTTCCTACACATCGGACGAGGCCTATATTACGGATCATTTCTCTACTCAGAAACCTGAA"

posterior_probability = paternity_test(child_dna, father_dna)

print("Posterior Probability of being the true father:", posterior_probability)
