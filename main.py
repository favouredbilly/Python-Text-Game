from room import Room
from character import Enemy, Character, Friend

kitchen = Room("Kitchen")
kitchen.set_description("This is where we cook.")

dining_hall = Room("Dining Hall")
dining_hall.set_description("We eat all the junks here.")

ballroom = Room("Ballroom")
ballroom.set_description("We hold parties here. party, party.")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

john = Enemy("john", "A terrifying face")

# Add some conversation for Dave when he is talked to
john.set_conversation("What's up, dude!")

john.set_weakness("cheese")

dining_hall.set_character(john)

# Add a new character

tom = Friend("tom", "A friendly skeleton")
tom.set_conversation("Why hello there.")
ballroom.set_character(tom)

current_room = kitchen

dead = False

while dead == False:

    print("\n")
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    command = input("> ")

    if command in ["north", "south", "east", "west"]:
        # Move in the given direction
        current_room = current_room.move(command)
    elif command == "talk":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "fight":
        # You can check whether an object is an instance of a particular
        # class with isinstance() - useful! This code means
        # "If the character is a Friend"
        if inhabitant == None or isinstance(inhabitant, Friend):
            print("There is no one to fight with here")
        else:
            # Fight with the inhabitant, if there is one
            print("What will you fight with?")
            fight_with = input()
            if inhabitant.fight(fight_with) == True:
                # What happens if you win?
                print("Hurray, you won the fight!")
                current_room.set_character(None)
            else:
                # What happens if you lose?
                print("sorry, you lost the fight.")
                print("That's the end of the game")
                dead = True
    elif command == "hug":
        if inhabitant == None:
            print("There is no one to hug here:(")
        else:
            if isinstance(inhabitant, Enemy):
                print("I wouldn't do that if I were you...")
            else:
                inhabitant.hug()


