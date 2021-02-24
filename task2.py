D = {}
keys = input()
values = input()
k = keys.split()
val = values.split()
for i in range(0, len(k)):
    if i < len(val):
        D[k[i]] = val[i]
    else:
        D[k[i]] = "None"
print(D)
