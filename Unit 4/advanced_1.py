word_1 = input("Enter first word: ")
word_2 = input("Enter second word: ")

if len(word_1) > len(word_2):
    long_word = word_1
    short_word = word_2
else:
    long_word = word_2
    short_word = word_1
    
char_len = len(short_word)

while char_len > 1:
    sub_string = short_word[0:char_len]
    index = 0
    while index + char_len <= len(longword):
        print(sub_string, longword[index:index+char_len])
        index += 1
    char_len -= 1
    