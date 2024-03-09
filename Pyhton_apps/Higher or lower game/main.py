import art,game_data,random,os

print(art.logo)
score = 0
def formatdata(account_a):
    account_name = account_a["name"]
    account_desc = account_a["description"]
    account_country = account_a["country"]
    return(f"{account_name}, a {account_desc}, from {account_country}")

def checkanswer(guess,a_follower,b_follower):
    follow=0
    if (guess=="a" and a_follower>b_follower) or (guess=="b" and b_follower>a_follower):
       return True
    else:
        return False

def game(score):
    account_a = random.choice(game_data.data)
    account_b = random.choice(game_data.data)
    if account_a ==account_b:
        account_b = random.choice(game_data.data)

    print(f"Compare A: {formatdata(account_a)}")
    print(art.vs)
    print(f"Compare b: {formatdata(account_b)}")
    guess = input("Who has more follower Type 'A' or 'B' : ").lower()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = checkanswer(guess,a_follower_count,b_follower_count)
    if is_correct:
        score+=1
        os.system('clear')
        print(f"You'r right ! Current score is : {score}")
        game(score)
        
    else: 
        os.system('clear')
        print(f"Sorry you'r Wong your final score is : {score}")
game(score) # I created loop with using fuctions 

