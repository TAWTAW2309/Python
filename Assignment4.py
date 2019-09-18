def lcm(x,y):
    if x > y:
        z = x
    else:
         z = y

    while (True):
        if ((z % x==0) and (z % y == 0)):
            lcm = z
            break

digit1 = int(input("Enter a number"))
digit2 = int(input("Enter a number"))
print("The LCM of", digit1, "and", digit2, "is", lcm(digit1, digit2))


