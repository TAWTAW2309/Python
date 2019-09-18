Digit1 = int(input("Enter a number:"))
Digit2 = int(input("Enter a number"))

def hcf(y,x):
    while(x):

        y, x=x, y % x
        return y

print("The hcf of", Digit1, "and", Digit2, "is", hcf(Digit1, Digit2))




