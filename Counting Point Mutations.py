with open('rosalind_hamm.txt') as f:
    s1 = f.readline()
    s2 = f.readline()


def compare_strings(s1, s2):
    for i in range(min(len(s1), len(s2))):
        yield s1[i] == s2[i]

gen = compare_strings(s1, s2)
hamm_dis = 0

for result in gen:
    if not result:
        hamm_dis = hamm_dis + 1
    
print(hamm_dis)