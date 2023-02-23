n= 59

i = 2
is_prime= True
while i<= n:
    if n % i == 0:
        print(f"{n} is not a prime number, it is divisible by {i}")
        is_prime = False
        break # is you exit via break, the else block will not be executed
    i += 1
if i ==n:
    # this will only be executed if the while loop is not exited via break
    print(f"{n} is a prime number")