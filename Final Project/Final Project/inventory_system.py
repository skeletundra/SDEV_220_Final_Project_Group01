from product import Product

products = []
customers = []
transactions = []

def add_product():
    #user enters new product details
    new_id = input("Enter product ID: ")

    #check if product already exists
    product = find_product(new_id)

    #if product ID is not found in list
    if product == None:
        new_name = input("Enter product name: ")
        new_quantity = input("Enter quantity: ")
        new_price = input("Enter price: $")
        
        #create new product object
        new_product = Product(new_id, new_name, new_quantity, new_price)

        #add new product object to list of products
        products.append(new_product)


def remove_product():
    search_id = input("Input ID for product you are searching for ")
    product = find_product(search_id)

    #delete product if ID exists in list
    if product != None:
        products.remove(product)

def find_product(search_id):
    #check if there are any stored products
    if len(products) > 0:
        #find product by its id
        for p in products:
            if p.product_id == search_id:
                print(f"{p._name} found in products list")
                return p
        print("Product not found")
        return None
    else:
        print("No products in inventory")
        return None

def add_customer():
    #input customer information
    #create new customer object
    #check if customer already exists
    #add to list
    print("customer added")

def record_transaction():
    print("transaction recorded")

def generate_sales_report():
    print("printing sales report")

def update_product_quantity():
    #get product id
    #find_product()
    #get product index in products
    #set new quantity
    print("quantity updated")

def print_inventory():
    count = 1
    if len(products) == 0:
        print("No products in inventory")
    for p in products:
        print(f"\nProduct ID: {p._id}")
        print(f"Product name: {p._name}")
        print(f"Product quantity: {p._quantity}")
        print(f"Product price: {p._price}")
        count+=1