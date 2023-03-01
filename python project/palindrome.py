def find_palindrome(word, palindrome):
    n1 = len(word)
    n2 = len(palindrome)
    if n1 != n2:
        return 0
    word = sorted(word)
    palindrome = sorted(palindrome)
    for i in range(0, n1):
        if word[i] != palindrome[i]:
            return 0
    return 1
input("Please provide five words each. One word for one input.")
word = input("Provide a word: ")
palindrome = input("Provide another word: ")
count = 0
count += 1

while word == palindrome or word != palindrome:
    if find_palindrome(word, palindrome):
        print("These strings are palindrome of each other")
        count += 1
        if(count <= 6):
            word = input("Provide a word: ")
            palindrome = input("Provide another word: ")
    else:
        if(word != palindrome):
            print("These strings are not palindrome of each other");
            count += 1
        if(count <= 6):
            word = input("Provide a word: ")
            palindrome = input("Provide another word: ")
            break
if find_palindrome(word, palindrome):
    print("These strings are palindrome of each other")
if(word != palindrome):
    print("These strings are not palindrome of each other");
print("Five words are enough")
print("Thank you")

