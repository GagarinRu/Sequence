n = int(input())
sequence = str()
y = 1
while y != n+1:
    sequence += ''.join(map(str, [y]*y))
    y += 1
print(sequence)