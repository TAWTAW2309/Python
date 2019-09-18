S = input("Please enter a sentences")
upper = 0
lower = 0
num = 0
chracter=0

for x in S:
    if x.upper()>= 'A' and x <= 'Z':
        upper += 1

    elif x.lower() >= 'a' and x<='z':
        lower += 1

    elif x.isdigit():
        num +=1

    else:
         chracter +=1

print('Upper Case Letter:', upper)
print('Lower Case Letters:', lower)
print('Number:', num)
print('Special char:', chracter)