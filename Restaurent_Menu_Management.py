def add_item(initial_menu,item):
    if item in initial_menu:
        return f"{item} is already available"
    initial_menu.append(item)
    return f"{item} added successfully"

def remove_item(initial_menu,item):
    if item in initial_menu == False:
        return f"Item not found in the menu"
    else:
        initial_menu.remove(item)
    return f"{item} deleted successfully"

def check_item(initial_menu,item):
    if item in initial_menu:
        return f"{item} is available"
    else:
        return f"{item} not available"


initial_menu = ["Pizza", "Burger", "Pasta", "Tacos"]
while True:
    print("1. Check Item")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Exit")
    choice = int(input("Enter choice : "))
    if(choice == 1):
        item = input("Enter the food item to check : ")
        print(check_item(initial_menu,item))
    elif choice == 2:
        item = input("Enter the food item to add : ")
        print(add_item(initial_menu,item))
    elif choice == 3:
        item = input("Enter the food item to remove : ")
        print(remove_item(initial_menu,item))
    elif choice == 4:
        exit(1)
    else:
        print("Enter valid option")
