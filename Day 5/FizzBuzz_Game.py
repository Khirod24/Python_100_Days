target = int(input("Enter the number: "))
for num in range(1, target+1):
    if(num % 3 == 0 and num % 5 ==0):
        print("FizzBuzz")
    else:
       if num % 3 == 0:
         print("Fizz")
       elif num % 5 == 0:
         print("Buzz")
       else:
          print(num)
    