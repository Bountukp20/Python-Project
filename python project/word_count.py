hi_hi = input("Hi there")
count_words = len(input("what's on your mind today: ").split())
if(count_words == 1):
    print("oh nice, you just told me what's on your mind in "+str(count_words)+" word.")
else:
    print("oh nice, you just told me what's on your mind in "+str(count_words)+" words.")
# print("the number of words is" + len(str(count_words.split())))

number_of_words = 0


with open(r'learning.txt','r') as file:


    data = file.read()


    lines = data.split()


    number_of_words += len(lines)

if(number_of_words == 1):
    print("And", number_of_words, "word in the file provided.")
else:
    print("And", number_of_words, "words in the file provided.")
