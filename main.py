rna = ['A', 'U', 'G', 'C']
def chunk(input_list, chunk_size):
    return [input_list[i:i + chunk_size] for i in range(0, len(input_list), chunk_size)]
codons = [nt1 + nt2 + nt3 for nt1 in rna for nt2 in rna for nt3 in rna]
Tree = {
    'a': {
        'a': {('a', 'g'): "lysine", ('c', 'u'): "asparagine"},
        'u': {'g': 'methionine', ('a', 'u', 'c'): "isoleucine"},
        'c': {('u', 'a', 'c', 'g'): 'threonine'},
        'g': {('g', 'a'): 'arginine', ('c', 'u'): 'serine'},
    },
    'u': {
        'u': {('u', 'c'): 'phenylalanine', ('a', 'g'): 'leucine'},
        'a': {('u', 'c'): 'tyrosine', ('a', 'g'): 'stop'},
        'c': {('u', 'a', 'c', 'g'): 'serine'},
        'g': {('u', 'c'): 'cysteine', 'a': 'stop', 'g': 'tryptophan'},
    },
    'c': {
        'u': {('u', 'a', 'c', 'g'): 'leucine'},
        'c': {('u', 'a', 'c', 'g'): 'proline'},
        'a': {('u', 'c'): 'histidine', ('a', 'g'): 'glutamine'},
        'g': {('u', 'a', 'c', 'g'): 'arginine'},
    },
    'g': {
        'g': {('u', 'a', 'c', 'g'): 'glycine'},
        'a': {('a', 'g'): 'glutamic acid', ('u', 'c'): 'aspartic acid'},
        'c': {('u', 'a', 'c', 'g'): 'alanine'},
        'u': {('u', 'a', 'c', 'g'): 'valine'},
    },
}
selCodon = input('Please input a valid mRNA codon sequence: ').lower()
l1i, l2i, l3i = selCodon[0], selCodon[1], selCodon[2]
if l1i in Tree and l2i in Tree[l1i]:
    for key, value in Tree[l1i][l2i].items():
        if isinstance(key, tuple) and l3i in key:
            print(value)
            break
        elif key == l3i:
            print(value)
            break
