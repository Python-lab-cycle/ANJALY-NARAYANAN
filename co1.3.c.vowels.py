#list of vowels
word=input("Enter your sentence")
for letter in word:
    if letter in 'aeiou':
        print(letter,end='')
