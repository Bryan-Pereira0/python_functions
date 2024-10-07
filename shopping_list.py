#task123
def shopping_list():
    shoppinglist = []
    print("Hello what would you like to add or remove to your shopping list")
    print("Use A to add or R to remove, use Q at anytime to quit and S to show your list!")
    
    
    while True:
        choice = input("A, R, Q or, S?: ")
        if choice == 'A':
            item = input("Enter the item you want to add: ")
            shoppinglist.append(item)
            print(f"{item} has been added to your list.")
        elif choice == 'R':
            item_to_remove = input("What would you like to remove?")
            if item_to_remove in shoppinglist:
                shoppinglist.remove(item_to_remove)
                print(f"{item_to_remove} has been removed from your list.")
            else:
                print("Item isn't in list.")
        elif choice == 'Q':
            print("Thank you for using this list maker!")
            break
        elif choice == 'S':
            if len(shoppinglist) == 0:
                print("The list is empty")
            else:
                if shoppinglist:
                    print("Your shopping list: ")
                    index = 1
                    for item in shoppinglist:
                        print(f"{index}. {item}")
                        index += 1
        else:
            print("You can't do that.")
            
shopping_list()
    
        