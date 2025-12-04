from customer import Customer
from inventory_system import *
import inventory_system

def menu_choice(user_input): #evaluate user input
    if(user_input == "1"):
        inventory_system.add_product()

    elif(user_input == "2"):
        inventory_system.remove_product()

    elif(user_input == "3"):
        search_id = input("Input ID for product you are searching for ")
        inventory_system.find_product(search_id)

    elif(user_input == "4"):
        inventory_system.print_inventory()        

    elif(user_input == "5"):
        inventory_system.add_customer()
        

    elif(user_input == "6"):
        inventory_system.record_transaction()
        
    elif(user_input == "7"):
        inventory_system.generate_sales_report()


def main():
    while(True):
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
        if(int(user_input) == 8):
            print("Shutting down")
            break

        #navigate menu based on user input
        running = menu_choice(user_input)


if __name__ == "__main__":
    main()