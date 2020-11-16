serial = input("Enter serial number: ")

valid = True
counter = 1

if len(serial) == 5 and serial[0] == "#":
    while counter < 4 and valid:
        if serial[counter].isdigit():
            valid = True
        else:
            valid = False
        counter += 1

if serial[4] != "#":
    valid = False

print(valid)