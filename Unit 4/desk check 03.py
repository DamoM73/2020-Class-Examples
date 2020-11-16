# identify the number of vowels in a word

word = ""

while not word.isalpha():
    word = input("Please enter a word: ").lower()

num_o_vowels = 0

for char in word:
    if char in ["a","e","i","o","u"]:
        num_o_vowels = num_o_vowels + 1
        
print(f"The number of vowels in {word} is {num_o_vowels}")