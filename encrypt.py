from test import reverse_word

plaintext = input("Enter plaintext: ")
plaintext = plaintext.split()
for i in range(len(plaintext)):
    length = len(plaintext[i])
    for j in plaintext[i]:
        print(f"{plaintext[i]}, {plaintext[i][::-1]}")

def find_halves(word):
    if word %2 == 0:
        even = True
        first_half = ""
        second_half = ""
    else:
        even = False
        first_half = ""
        middle = plaintext[len(plaintext)/2 + 1]
        second_half = ""