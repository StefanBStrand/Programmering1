# Pakkeliste

packing_list = []
packing = True
first_iteration = True
instruction = ("To add item type Add.\nTo remove item type Remove.\nTo print list type Print.\nTo stop packing type "
               "Stop")
question = "What would you like to do?"

print(question)
print(instruction)
while packing:
    if first_iteration:
        decision = input("Make your choice: ").lower()  # Making sure input is case-insensitive.
        first_iteration = False
    else:
        decision = input("What would you like to do now?:").lower()

    if decision == "add":
        item_to_add = input("What do you want to add?: ").lower()
        packing_list.append(item_to_add)
    elif decision == "remove":
        item_to_remove = input("What would you like to remove?:").lower()
        if item_to_remove in packing_list:  # Adding check to see if item is in list.
            packing_list.remove(item_to_remove)
            print(f"{item_to_remove} was removed from packing list")
        else:
            print(f"{item_to_remove} not in packing list")
    elif decision == "print":
        print(packing_list)
    elif decision == "stop":
        packing = False
    else:
        print(f"Invalid choice. {instruction}")  # Gives instructions to user if invalid input is used.
