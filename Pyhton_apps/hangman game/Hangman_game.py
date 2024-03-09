import random
import hangman_art
import hangman_words

chosen = random.choice(hangman_words.word_list)
print(f'solution is {chosen}.')
display =[]
for letter in chosen:
   display += "_"

end = False
life = 6 
print(hangman_art.logo)
print(f"{' '.join(display)}")
while not end and life>0:
   guess = input("Guess a letter ").lower()
   
   if guess in display:
        print(f"You've already guessed {guess}")

   for position in range(len(chosen)):
      letter = chosen[position]
    
      
      if letter == guess:
         display[position] = letter
          
   if letter != guess:
      life =life - 1
      print(f"You guessed {guess}, that's not in the word. You lose a life.")
   print(f"{' '.join(display)}")
   print(hangman_art.stages[life])
   if "_" not in display:
      end =True
      print(" you win ")
   if life <=0 :
      print(" You lose ")


