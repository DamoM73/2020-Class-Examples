while True:
    num = 3
    for div in range(2,num):
        if num % div == 0:
            print(num, "not prime")
            break
    num += 1
