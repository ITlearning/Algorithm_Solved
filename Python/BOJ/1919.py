s1 = input()
s2 = input()
cnt = 0
alphabet1 = [0] * 26
alphabet2 = [0] * 26
for i in s1 :
    alphabet1[ord(i) - 97] += 1
for i in s2 :
    alphabet2[ord(i) - 97] += 1

for i in range(26) :
    if(alphabet1[i] != alphabet2[i]) :
        cnt += abs(alphabet1[i] - alphabet2[i])

print(cnt)