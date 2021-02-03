from re import sub
from random import randint

rand_punc = [".",",",":",";","?","!"]

def caesar_encrypt(string,key,caesar_word=""):
    for char in string:
        if (65 <= ord(char) <= 90):
            char = char.lower()
            char = chr((ord(char) + key - 97) % 26 + 97)
            caesar_word += char
        elif (97 <= ord(char) <= 122):
            char = chr((ord(char) + key - 97) % 26 + 97)
            caesar_word += char
        else:
            caesar_word += char
    return caesar_word


def reverse_word(word):    
    if len(word) <= 3:
        end_word = word[::-1]
    elif len(word) % 2 == 0:
        first_half = word[0:int((len(word)/2))]
        second_half = word[int((len(word)/2)):int(len(word))]
        first_half = first_half[::-1]
        second_half = second_half[::-1]
        end_word = first_half + second_half
    elif len(word) % 2 != 0:
        first_half = word[0:int((len(word)/2))]
        middle = word[int(len(word)/2)]
        second_half = word[int((len(word)/2) + 1): int(len(word))]
        first_half = first_half[::-1]
        second_half = second_half[::-1]
        end_word = first_half + middle + second_half
    
    end_word += rand_punc[randint(0,5)]
    return end_word


key = int(input("key: "))
message = input("message: ")
message = message = sub(r"[^\w\s]", "",message)


list_message = message.split()
output_str = ""
for word in list_message:
    encrypted_word = reverse_word(word)
    output_str += encrypted_word


final_out = caesar_encrypt(output_str, key)
print(final_out)


