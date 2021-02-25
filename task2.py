D = {}
keys = input()
values = input()
k = keys.split()
val = values.split()
for i in range(len(k)):
    if i < len(val):
        D[int(k[i])] = int(val[i])
    else:
        D[int(k[i])] = None
print(D)
