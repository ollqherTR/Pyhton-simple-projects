import art
import random
print(art.logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
cardsinhand= []
cardsindealer=[]
def pickcard(sum):
    n = random.randint(0,12)
    cardsinhand.append(cards[n])
    if sum>21:
        return False
    else:
        return True

for x in range(0,2):
    n = random.randint(0,12)
    cardsinhand.append(cards[n])
    n = random.randint(0,12)
    cardsindealer.append(cards[n])
print(f"Your cards : {cardsinhand}, current score : {sum(cardsinhand)} ")
print(f"Computers First Card is : {cardsindealer[0]}")
con = True
while con:
    if sum(cardsindealer)<17:
        n = random.randint(0,12)
        cardsindealer.append(cards[n])
    else:
        con = False
i = True
while i:
    if sum(cardsinhand)<=21:
        condition = input("Type y to pick a card, Type n to pass ")
        if condition =="y":
            
            i= pickcard(sum(cardsinhand))
            print(f"Your cards : {cardsinhand}, current score : {sum(cardsinhand)} ")
            
                
        elif condition =="n":
            print(f"Computers Final Hand is : {cardsindealer}, Final Score : {sum(cardsindealer)}")
            i=False
        else:
            print(" Wrong input")
    else:
        i=False
finalcards = sum(cardsinhand)
finaldealer = sum(cardsindealer)


if finalcards>21:
    print("You Lose ")
elif finalcards>finaldealer or finalcards>21:
    print("You Win") 
elif finalcards==finaldealer:
    print("Draw")
else :
    print(" You Lose ")

