def reverse_word(word):    
    if len(word) %2 == 0:
        even = True
        first_half = word[0:int((len(word)/2))]
        second_half = word[int((len(word)/2)):int(len(word))]
        print(f"{first_half}, {second_half}")
    else:
        even = False
        first_half = word[0:int((len(word)/2))]
        middle = word[int((len(word)/2) + 1)]
        second_half = word[int((len(word)/2) + 1): int(len(word))]
        print(f"{first_half}, {middle}, {second_half}")
    
