def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You dont have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxers of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanet. \n")


print("We can just give functin numbers directly:")
cheese_and_crackers(20, 30)


print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 5

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
cheese_and_crackers(10 + 20 , 5 + 6)


print("And now we cancombine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)






