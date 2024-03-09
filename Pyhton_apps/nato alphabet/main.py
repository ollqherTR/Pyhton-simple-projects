import pandas
data = pandas.read_csv("phyton_dersler/nato alphabet/nato_phonetic_alphabet.csv")

dicti = {row.letter:row.code for(index,row) in data.iterrows()}

word = input("Enter a word : ").upper()
output = [dicti[letter] for letter in word]
print(output)