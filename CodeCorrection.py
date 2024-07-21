place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river" :
        print("You found a boat!")
    else: 
        pass
if place == "cave":
    action = input("Chose your next move:Light a torch or proceed in the dark")
    if action == "light a torch":
        print("you found a secret path")
    elif action == "proceed in the dark": 
        print("you tripped on a rock")
    else: 
        pass
else:
    pass

    