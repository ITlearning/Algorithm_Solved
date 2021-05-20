t = input()

for i in range(2) :
    a = input()
    if a == 'E' :
        t = t.replace(t[0], "")
print(t)