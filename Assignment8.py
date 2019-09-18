p1 = input("What do you want to choose paper, rock or scissors:")
p2 = input("What do you want to choose paper, rock or scissors:")

def compare(p1, p2):

    if p1 == p2:
        return("it's the same")

    elif p1 == 'paper':
        if p2 == 'rock':
            return("paper beats rock")
        else:
            return("Try again")

    elif p1 == 'scissors':
        if p2 == 'paper':
            return("scissors beats paper")
        else:
            return("Try again")

    elif p1 == 'rock':
        if p2 == 'scissors':
            return("rock beats scissors")
        else:
            return("Try again")

    else:
        return("Not Available.Try again")

print(compare(p1, p2))





