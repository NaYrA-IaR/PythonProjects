print("Program to check if a given string is palindrome ")

def check_palindrome(word):
    rev_word = ""
    for i in range(len(word),0,-1):
        rev_word += word[i-1]
    return rev_word

word = input("Enter Word to check if palindrome: ")
if check_palindrome(word.lower()) == word.lower():
    print("\nGiven word is a palindrome")
else:
    print("Not a palindrome")