def prime_checker(num):
    isPrime = True
    for i in range(2,num):
        if num % i == 0:
            isPrime = False
    if isPrime:
        print(f"{num} is a Prime Number")
    else:
        print(f"{num} is not a Prime Number")

n = int(input("Enter a number: "))
if(n==1):
    print("1 is neither a prime nor a composite number")
else:
    prime_checker(n)