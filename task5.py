s = input()
x = 0
y = 0
for i in range(len(s)):
    if s[i] == 'U':
        y += 1
    if s[i] == 'D':
        y -= 1
    if s[i] == 'L':
        x -= 1
    if s[i] == 'R':
        x += 1
print(x == 0 and 0 == y)
