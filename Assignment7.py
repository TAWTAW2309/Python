Stock_list = ["medicine1", "medicine2", "medicine3", "medicine4", "medicine5", "medicine6", "medicine5"]
menu = int(input("1-Add an item, 2-Remove item, 3-Insert an item.Please enter 1, 2, or 3: "))

if menu == 1:
    print("This option allows you to add items.")
    print(Stock_list)
    pharmacy = input("what items do you want to add?")
    Stock_list.append(pharmacy)
    print(Stock_list)

elif menu == 3:
    print("This menu allows to insert items")
    print(Stock_list)
    pharmacy = input("which item do you want to insert")
    position = int(input("where would you like to insert it in the list?"))

    if position < len(Stock_list):
        Stock_list.insert(position,pharmacy)
        print(Stock_list)
    else:
        print("position not available")

elif menu == 2:
    print("This menu allows you to remove item in the list")
    print(Stock_list)
    pharmacy_remove = input("which item do you want to remove?")
    if pharmacy_remove in Stock_list:
        Stock_list.remove(pharmacy_remove)
        print(Stock_list)

    else:
        print("This item do not found in the list.")






