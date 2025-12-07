from product import Product
from customer import Customer
from transaction import Transaction
from datetime import datetime

products = []
customers = []
transactions = []

def add_product():
    #user enters new product details
    new_id = input("Enter product ID: ")

    #check if product already exists
    product = find_product(new_id)

    #if product ID is not found in list
    if product is None:
        new_name = input("Enter product name: ")
        new_quantity = input("Enter quantity: ")
        new_price = input("Enter price: $")
        
        #create new product object
        try:
            new_product = Product(new_id, new_name, int(new_quantity), float(new_price))
        except ValueError:
            print("Invalid quantity or price input")
            new_product = None

        #add new product object to list of products
        if new_product is not None:
            products.append(new_product)
            print("Product added.")
    else:
        print("Product ID already exists.")

def remove_product():
    #get product ID from user
    search_id = input("Input ID for product you are searching for: ")
    product = find_product(search_id)

    #delete product if ID exists in list
    if product is not None:
        products.remove(product)
        print("Product removed.")
    else:
        print("Product not found.")

def find_product(search_id):
    #check if there are any stored products
    if len(products) > 0:
        #find product by its id
        for p in products:
            if p.product_id == search_id:
                print(f"{p.product_name} found in products list")
                return p
        print("Product not found")
        return None
    else:
        print("No products in inventory")
        return None

def print_inventory():
    count = 1
    if len(products) == 0:
        print("No products in inventory")
        return

    #print all products in inventory
    for p in products:
        print(f"\nProduct ID: {p.product_id}")
        print(f"Product name: {p.product_name}")
        print(f"Product quantity: {p.product_quantity}")
        print(f"Product price: ${p.product_price}")
        count += 1

def add_customer():
    #input customer information
    new_id = input("Enter customer ID: ")

    #check if customer already exists
    for c in customers:
        if c.id == new_id:
            print("Customer already exists.")
            return

    #create new customer object
    new_name = input("Enter customer name: ")
    new_customer = Customer(new_id, new_name)

    #add to list
    customers.append(new_customer)
    print("Customer added")

def update_product_quantity(product, quantity_sold):
    #get new quantity and update product
    new_quantity = product.product_quantity - quantity_sold
    product.update_quantity(new_quantity)
    print(f"Updated quantity for {product.product_name}: {product.product_quantity}")

def record_transaction():
    #record a customer purchase
    customer_id = input("Enter customer ID: ")
    customer = None

    #find customer in list
    for c in customers:
        if c.id == customer_id:
            customer = c
            break
    if customer is None:
        print("Customer not found.\n")
        return

    #collect purchased items
    items = []
    while True:
        product_id = input("Enter product ID (or 'done' to finish): \n")
        if product_id.lower() == "done":
            break
        product = find_product(product_id)

        #check if product exists
        if product is None or product.product_quantity == 0:
            continue

        #check product is stocked
        if product.product_quantity == 0:
            print(f"Our {product.product_name} stock is depleted\n")
            continue

        #check quantity input is valid data type
        try:
            qty = int(input(f"Enter quantity for {product.product_name}: \n"))
        except ValueError:
            print("Invalid quantity input\n")
            continue

        #check stock to match desired quantity
        if qty > product.product_quantity:
            print("Insufficient stock.\n")
            continue

        #add product to item cart
        update_product_quantity(product, qty)
        items.append((product, qty))

    if not items:
        print("No items purchased.\n")
        return

    #calculate total cost and update quantities
    total_cost = 0
    for product, qty in items:
        total_cost += product.product_price * qty

    #generate transaction ID
    transaction_id = len(transactions) + 1
    date = datetime.now().strftime("%Y-%m-%d")

    #create and store transaction
    new_transaction = Transaction(transaction_id, customer, items, total_cost, date)
    transactions.append(new_transaction)

    print(f"Transaction recorded. Total cost: ${total_cost}")

def generate_sales_report():
    #print all recorded transactions
    if len(transactions) == 0:
        print("No transactions recorded.")
        return

    total_revenue = 0
    for t in transactions:
        print(f"\nTransaction ID: {t.id}")
        print(f"Customer: {t.customer.name}")
        print(f"Date: {t.date}")
        print("Items:")
        for product, qty in t.items:
            print(f"  {product.product_name} x {qty}")
        print(f"Transaction total: ${t.total_cost}")
        total_revenue += t.total_cost

    #print summary totals
    print("\n--- Summary ---")
    print(f"Total revenue: ${total_revenue}")
    print(f"Total transactions: {len(transactions)}")
