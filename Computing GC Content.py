with open('rosalind_gc.txt') as f:
    fasta = f.read()

ratio_dict = {}
keep_chars = ['A', 'T', 'G', 'C']
for string in fasta.split('>'):
    if string:
        title = str(string[0:14]).replace('\n', '')
        GC_count = string.count('C') + string.count('G')
        string = ''.join(x for x in string if x in keep_chars)
        GC_ratio = round((GC_count / len(string) * 100), 6)
        ratio_dict[title] = GC_ratio
        

max_ratio = max(ratio_dict, key = ratio_dict.get)
print(max_ratio + '\n' + str(ratio_dict.get(max_ratio)))