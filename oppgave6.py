# Pakkeliste - bruk liste som du skal iterere gjennom, eller  objekt?


packing_list = []
packing = True
question = "What would you like to do?"

print(question)
print("To add item type Add.\nTo remove item type Remove.\nTo print list type Print.\nTo stop packing type Stop")
while packing:
    decision = input("Make your choice: ")
    if decision == "Add":
        item_to_add = input("What do you want to add?: ") # Noe skal legges til i packing_list
        packing_list.append(item_to_add)
    elif decision == "Remove":
        item_to_remove = input("What would you like to remove?:")
        packing_list.remove(item_to_remove)
    elif decision == "Print":
        print(packing_list)
    elif decision == "Stop":
        packing = False
    else:
        print("invalid choice")




# må legge til if checker for å bestemme hva som skal skje basert på bruker input
