import random
# loop
# Ask: roll the dice?
# if user enter y 
#   generate  two ramdom numbers
#   print numbers
# if user enter n
#   print thank you message
#    terminate
# else
#   print invalid choice
count = 0   # for count
total = 0   # for sum
lst=[]
while True:
    choice = input("Roll the Dice? (Y/N)").lower()
    if choice == "y":
        die1=random.randint(1,6)
        die2=random.randint(1,6)
        total = die1+die2   # sum of dice
        lst.append(total)   # append in lst 
        print(f"({die1},{die2})")
        print("Total number of dice",total)
        count +=1
    elif choice == "n":
        print("Total count dice = ",count)
        if count > 0:
            print("Highest sum of dice = ",max(lst))
            print("Lowest sum of dice = ",min(lst))
            print("Average of dice = ",sum(lst)/len(lst))
        else:
            print("No dice Rolled")
            
        print("Thank you for playing!")
        break
    else:
        print("Invalid Choice")
   