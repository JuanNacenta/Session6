n = 59

for i in range(2, n):
    if n % i == 0:
        print(f"{n} is not  aprime number, it is divisible by {i}")
        break
else:
    print(f"{n} is a prime number")