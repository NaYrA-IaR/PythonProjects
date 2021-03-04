import random

print("******Coin Toss Simulation*******")

option="y"
no_of_head=0
no_of_tail=0
list_coin=["Head","Tail"]
input("\nPress ENTER key to start coin toss\n")

while(option.lower()=="y"):  
    outcome=random.choice(list_coin)
    if(outcome.lower()=="head"):
        print("\nThe result of coin toss was: ",outcome)
        no_of_head+=1
    else:
        print("\nThe result of coin toss was: ",outcome)
        no_of_tail+=1
    
    print("No of heads: {}, No of tails: {}".format(no_of_head,no_of_tail))
    option=input("Do you want to continue? \nEnter y for Yes else Enter n for No: ")
      
    if(option.lower()=="y" or option.lower()=="yes"):
        option="y"
    else:
        option="n"

print("THANK YOU!!")