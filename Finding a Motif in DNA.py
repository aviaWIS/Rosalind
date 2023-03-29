with open('rosalind_subs.txt') as f:
    s = f.readline().replace('\n', '')
    t = f.readline().replace('\n', '')

n = len(t)
t_pos = ''

for i in range(len(s)):
    if s[i:i+n] == t:
        t_pos = t_pos + str(i+1) + ' '
        
print(t_pos)