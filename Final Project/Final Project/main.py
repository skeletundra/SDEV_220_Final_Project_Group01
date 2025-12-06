from inventory_system import *

def menu_choice(user_input): #evaluate user input
    if user_input == "1":
        add_product()

    elif user_input == "2":
        remove_product()

    elif user_input == "3":
        search_id = input("Input ID for product you are searching for: ")
        find_product(search_id)

    elif user_input == "4":
        print_inventory()        

    elif user_input == "5":
        add_customer()
        
    elif user_input == "6":
        record_transaction()
        
    elif user_input == "7":
        generate_sales_report()


def main():
    while True:
        #collect user input
        user_input = input("\nInput number to navigate: \n \
        1. Add Product \n \
        2. Remove Product \n \
        3. Find Product \n \
        4. Print Inventory  \n \
        5. Add Customer  \n \
        6. Record Transaction  \n \
        7. Generate Sales Report  \n \
        8. Quit \n")
        
        #check if user wants to quit
        if int(user_input) == 8:
            print("Shutting down")
            break

        #navigate menu based on user input
        menu_choice(user_input)


if __name__ == "__main__":
    main()
