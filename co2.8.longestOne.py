lis=input("Enter a list with some string (space separated):")
words_list=lis.split()
word_len=[]
for n in words_list:
    word_len.append((len(n),n))
word_len.sort()
print(word_len)
print("Longest Word:",word_len[-1][1], "and length=",word_len[-1][0])
