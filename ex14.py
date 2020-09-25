from sys import argv

script, user_name = argv
#assigning argv
prompt = ' > '
#variable allocation
print (f"Hi {user_name}, I'm the {script} script.")
print ("I'd like to ask you afew questions.")
print(f"Do you like TV {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name} ?")
lives = input(prompt)

print("What kind of ice cream do you love")
ice_cream = input(prompt)

print(f"""
Alright, so you said {likes} about liking tv.
you live in {lives}. Not sure where that is.
And you love {ice_cream} ice cream.
Nice ;) 
""")


