'''Question 3: Shopping Cart Management 
A customer adds products to a shopping cart. Write a function that 
accepts a list of product names and performs the following 
operations: 
• Add a new product. 
• Remove a purchased or unwanted product. 
• Display the final cart. 
• Count the total number of products.'''

def shopping_cart(products):
    new_product = input("Enter a product to add: ")
    products.append(new_product)

    remove_product = input("Enter a product to remove: ")

    if remove_product in products:
        products.remove(remove_product)
        print(remove_product, "removed successfully.")
    else:
        print("Product not found in cart.")

    print("\nFinal Shopping Cart:", products)

    print("Total number of products:", len(products))


cart = ["Laptop", "Mouse", "Keyboard"]

shopping_cart(cart)

    