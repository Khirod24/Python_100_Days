target = int(input("Enter the number: "))
even_sum = 0
for number in range(2, target+1, 2):
    even_sum += number
print(f"Even sum upto {target} is = {even_sum}")