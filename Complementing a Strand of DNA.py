with open('rosalind_revc.txt') as f:
    s = f.read()
    s = s.replace('\n', '')

complement ={'A' : 'T',
             'T' : 'A',
             'C' : 'G',
             'G' : 'C',
}

comp_strand = ""
for base in s:
    comp_strand += complement[base]

print(comp_strand[::-1])
