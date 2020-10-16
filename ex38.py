ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 thngs in the list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee","corn", "Banana" ,"Girl", "Boy"]


while len(stuff) != 12:
    next_one = more_stuff.pop()
    print("Adding: ",next_one)
    stuff.append(next_one)
    print(f"there are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff")

print(stuff[1])
print(stuff[-1]) #whoa! fancy
print(stuff.pop())
print(' '.join(stuff)) #What? cool!
print('#'.join(stuff[3:5])) #super stellar!
