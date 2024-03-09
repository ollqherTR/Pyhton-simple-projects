import os
def add_new_bidder(name, bid):
  new_country = {}
  new_country["name"] = name
  new_country["bid"] = bid
  list.append(new_country)

x=1
list=[]
while x>0:

    name = input("What is your name?: ")
    bid = input("What is your bid?: $")
    add_new_bidder(name,bid)
    anotherbid = input("Is there another user who want to bid ? YES or NO ").lower()
    if anotherbid =="no":
        x -=1
    if anotherbid =="yes":
       os.system('clear')
highest_bid = list[0]["bid"]
highest_bidder = list[0]["name"]
for z in range(1, len(list)):  
    if list[z]["bid"] > highest_bid:
        highest_bidder = list[z]["name"]
        highest_bid = list[z]["bid"]

print(f"The highest bidder is {highest_bidder} bid is: {highest_bid}")

