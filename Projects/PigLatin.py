print("****This Program prints the Pig Latin of a Given Word****")

s = input("Enter a word: ")
n=len(s)
new_s = ""
i=0
vowel = ['a','e','i','o','u']
if (s[i] in vowel):
    new_s += s
else:    
    while(s[i] not in ['a','e','i','o','u']):
        new_s = s[i+1:n]+s[0:i+1]
        i+=1
new_s += "ay"
new_s=new_s.lower()
print("\nThe Pig Latin for {} is {}".format(s,new_s))    