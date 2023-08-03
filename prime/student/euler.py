N = 600851475143
# N = 36
i = 2
while i*i <= N:
    if N % i == 0:
        N /= i
        print(i)
    else:
        i += 1
print(N)