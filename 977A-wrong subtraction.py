# Read input values
n, k = map(int, input().split())

# Perform Tanya's subtraction k times
for _ in range(k):
    if n % 10 == 0:
        n //= 10
    else:
        n -= 1

# Print the final result
print(n)
