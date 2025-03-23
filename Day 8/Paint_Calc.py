from math import ceil

def paintCalc(height,width,coverage):
    num_cans =  (height * width) / coverage
    ans = ceil(num_cans)
    print(f"You will need {ans} cans of paint")

h = int(input("Enter height: ")) 
w = int(input("Enter width: "))
c = 5
paintCalc(height=h,width=w,coverage=c) #keyword arguments in a function call 