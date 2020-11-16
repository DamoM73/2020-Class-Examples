# sum all the even numbers between 1 and 20
total = 0

for num in range(1,21):
    if num % 2 == 0:
        total = total + num
        
print(f"The sum of even numbers between 1 and 100 is {total}")