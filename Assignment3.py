number1 = int(input("Enter a number: "))

reverse = 0
while(number1>0):
    digit = number1%10
    reverse = reverse*10 +digit
    number1 = number1//10

    print("Reverse of the number:", reverse)