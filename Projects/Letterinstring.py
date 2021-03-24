print("Program To count no of words in string")

sent = input("Enter a string: ")
no_letter = dict()
for word in sent.split(" "):
    for let in word:
        if let.lower() not in list(no_letter.keys()):
            no_letter[let.lower()] = 1
        else:
            no_letter[let.lower()] += 1
print(no_letter)