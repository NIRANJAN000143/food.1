#TODO: Define the menu 
menu = "Biryani, Dose, Butter Chicken, Dal Makhani, Bread, Samosa."
#TODO: print the welcome message and ask for the user's name and phone number, address 
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! WELCOME TO OUR RESTAURANT !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
name = input("ENTER YOUR NAME: ")
phone = input("ENTER YOUR PHONE NUMBER: ")
address = input("ENTER YOUR address: ")

print(f"Hello Sir, my name is Priya, and I will be your server in our restaurant. Thank you, Ma'am, my name is {name}.")
print(f"I can see the menu for you. Sure sir, this is our menu:\n\n\n{menu}")
print("Please select your order from the menu:\n")

#TODO:Function to take and process orders
def take_order():
    order = input("Enter the item you want to order: ")
    if order == "Biryani":
        print("Biryani is ready to serve you, please wait for 20 minutes.")
    elif order == "Dose":
        print("Dose is ready to serve you, please wait for 10 minutes.")
    elif order == "Butter Chicken":
        print("Butter Chicken is ready to serve you, please wait for 15 minutes.")
    elif order == "Dal Makhani":
        print("Dal Makhani is ready to serve you, please wait for 25 minutes.")
    elif order.strip() == "Bread":  #TODO: Use strip to handle unwanted spaces
        print("Bread is ready to serve you, please wait for 2 minutes.")
    elif order == "Samosa":
        print("Samosa is ready to serve you, please wait for 12 minutes.")
    else:
        print("Sorry, we don't have this item in our menu.")

    return order

#TODO:Initial order
take_order()

#TODO:Ask if the user wants to order more
while True:
    new_order = input("Do you want to order anything else? (y/n): ")
    if new_order.lower() == "y":
        take_order()
    elif new_order.lower() == "n":
        print("Thank you for visiting our restaurant, we hope to see you again!")
        break
    else:
        print("Invalid input, please enter 'y' or 'n'.")

        


