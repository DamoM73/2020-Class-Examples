# sum all the even numbers between 1 and 100
total = 0

for num in range(1,101):
    if num % 2 == 0:
        total = total + num
        
print(f"The sum of even numbers between 1 and 100 is {total}")