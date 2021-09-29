ef print_vowel(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    output = "" 
   
    for letter in word.lower():
        if letter in vowels:
            output += letter + ""
    print("Vowels:", ', '.join(dict.fromkeys(output)))
print_vowel("Umuzi")

