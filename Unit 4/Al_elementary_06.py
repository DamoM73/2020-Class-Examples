n = int(input("Enter the value of n: "))
mode = input("Sum or Product?: ")

total = 0

for num in range(1,n+1):
    if mode == "sum":
        total = total + num
    elif mode == "product":
        total = total * num

print(total)