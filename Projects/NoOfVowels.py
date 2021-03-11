print("******Count Number Of Vowels In A String******\n")

sentence = input("Enter a String:")
noOfVow = 0
vow = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
for i in range(0,len(sentence)):
    if (sentence[i].lower()) in ['a','e','i','o','u']:
        noOfVow += 1
        vow[sentence[i].lower()] += 1
print("\nThe No of Vowels are: ",noOfVow)
print("\n",vow) 
