import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(art.logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text , shift_amount):
    cipher_text=""
    if shift_amount>26:
        shift_amount= shift_amount%26
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        if new_position>=26: 
            new_position=new_position-26
        new_letter=alphabet[new_position] 
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")
def decrypt(cipher_text , shift_amount):
    plain_text=""
    if shift_amount>26:
        shift_amount= shift_amount%26
    for letter in cipher_text:
         position = alphabet.index(letter)
         new_position = position - shift_amount
         if new_position>=26: 
            new_position=new_position+26

         plain_text+=alphabet[new_position ]
    print(f"The decoded text is {plain_text}")
if direction =="encode":
  encrypt(text,shift)
else:
    decrypt(text,shift)
