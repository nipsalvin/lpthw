def cheese_and_crackers (Cheese_count, cracker_boxes):
    print(f"you have {Cheese_count} cheeses!")
    print(f"You have {cracker_boxes} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket \n")
 
 
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30) 


print("OR, we can use variables from our scripts:")
cheese_amount = 10
cracker_amount = 50

cheese_and_crackers(cheese_amount,cracker_amount)


print("We can even do maths inside too")
cheese_and_crackers(20 + 10, 5 + 6)


print("And we can combine the two variables")
cheese_and_crackers(cheese_amount * 10, cracker_amount + 1000)











