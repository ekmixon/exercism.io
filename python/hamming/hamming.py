def distance(s1, s2):
        s1_list = list(s1)
        s2_list = list(s2)
        return sum(s1_list[i] != s2_list[i] for i, nucleotide in enumerate(s1_list))
