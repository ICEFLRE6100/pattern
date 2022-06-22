n = int(input(" Enter the number: "))

#original order
for i in range(1, n+1):
    print(i * "(:")
# reverse order
for i in range(n, 0, -1):
    print(i * "(:")
