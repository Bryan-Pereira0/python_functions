#task123
def add_item(shoppinglist):
    item = input("Enter the item you want to add: ")
    shoppinglist.append(item)
    print(f"{item} has been added to your list.")

def remove_item(shoppinglist):
    item_to_remove = input("What would you like to remove?")
    if item_to_remove in shoppinglist:
        shoppinglist.remove(item_to_remove)
        print(f"{item_to_remove} has been removed from your list.")
    else:
        print("Item isn't in list.")

def print_list(shoppinglist):
    if len(shoppinglist) == 0:
        print("The list is empty")
    else:
        if shoppinglist:
            print("Your shopping list: ")
            index = 1
            for item in shoppinglist:
                print(f"{index}. {item}")
                index += 1

def shopping_list():
    shoppinglist = []  
    while True:
        print("Hello what would you like to add or remove to your shopping list")
        print("Use A to add or R to remove, use Q at anytime to quit and S to show your list!")  
        choice = input("A, R, Q or, S?: ")
        if choice == 'A':
            add_item(shoppinglist)  
        elif choice == 'R':
            remove_item(shoppinglist)
        elif choice == 'Q':
                print("Thank you for using this list maker!")
                break
        elif choice == 'S':
                print_list(shoppinglist)
        else:
            print("You can't do that.")
            
shopping_list()
    
        