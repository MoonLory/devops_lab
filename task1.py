D = {}
n = int(input())
for i in range(0, n):
    s = input()
    parts = s.split()
    aver = (float(parts[1]) + float(parts[2]) + float(parts[3])) / 3.0
    D[parts[0]] = aver
s = input()
print("%.2f" % D[s])
