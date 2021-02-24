s = input()
x = 0
y = 0
for i in range(0, len(s)):
    if s[i] == 'U':
        y += 1
    if s[i] == 'D':
        y -= 1
    if s[i] == 'L':
        x -= 1
    if s[i] == 'R':
        x += 1
if x == 0 and 0 == y:
    print(True)
else:
    print(False)
