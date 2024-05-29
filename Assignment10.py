#1. Write a python program to sum up all the  items in a dictionary.

total = 0
dictionary  = dict(a=1, b=2, c=3, d=4)
    
for value in dictionary.values():
        total += value  
        print(f"Adding {value}, current sum: {total}")

print(f"Final sum: {total}")

# 2. Create a dictionary to store product information(name,price, quantity). Allow users to add, update and remove items from the inventory

def inventory_check(inventory):
    prodname = input("Enter product name: ")
    prodprice = float(input("Enter product price: "))  # Assuming the price can be a float
    prodquant = int(input("Enter the product quantity: "))
   
    inventory[prodname] = {'price': prodprice, 'quantity': prodquant}
    print(f"{prodname} added to inventory.")

def inventory_edit(inventory):
    while True:
        print("\nWhat would you like to do?\n1. Edit current inventory\n2. Create a new inventory\n3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            edit_current_inventory(inventory)
        elif choice == '2':
            inventory = create_new_inventory()
        elif choice == '3':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

def edit_current_inventory(inventory):
    print("\nDo you want to edit the current inventory? yes/no")
    choice = input().lower()
    if choice == 'yes':
        while True:
            print("\n1. Add product\n2. Update product\n3. Remove product\n4. Exit")
            option = input("Select an option: ")
            if option == '1':
                inventory_check(inventory)
            elif option == '2':
                update_product(inventory)
            elif option == '3':
                remove_product(inventory)
            elif option == '4':
                print("Exiting inventory edit.")
                break
            else:
                print("Invalid option. Please select again.")

def update_product(inventory):
    prodname = input("Enter the name of the product you want to update: ")
    if prodname in inventory:
        print(f"Current details of {prodname}: {inventory[prodname]}")
        prodprice = float(input("Enter updated price: "))  # Assuming the price can be a float
        prodquant = int(input("Enter updated quantity: "))
        inventory[prodname] = {'price': prodprice, 'quantity': prodquant}
        print(f"{prodname} updated in inventory.")
    else:
        print(f"Product {prodname} not found in inventory.")

def remove_product(inventory):
    prodname = input("Enter the name of the product you want to remove: ")
    if prodname in inventory:
        del inventory[prodname]
        print(f"{prodname} removed from inventory.")
    else:
        print(f"Product {prodname} not found in inventory.")

def create_new_inventory():
    inventory = {}
    print("\nCreating a new inventory:")
    while True:
        inventory_check(inventory)
        cont = input("\nDo you want to add more products to this inventory? yes/no: ").lower()
        if cont != 'yes':
            break
    return inventory

# Main program
print("Welcome to the Inventory Management System!")

inventory = create_new_inventory()
inventory_edit(inventory)

# 3.Create a dictionary where keys are departments in a company and values are nested dictionaries containing employee information (name, role).

company_info = {
    'HR': {
        'John Smith': 'HR Manager',
        'Alice Johnson': 'HR Assistant'
    },
    'Finance': {
        'Michael Brown': 'Finance Manager',
        'Emma White': 'Financial Analyst'
    },
    'IT': {
        'David Lee': 'IT Director',
        'Sarah Taylor': 'Software Engineer'
    }
}

# Print the company_info dictionary
print("Company Information:")
for department, employees in company_info.items():
    print(f"\n{department}:")
    for employee, role in employees.items():
        print(f" - {employee}: {role}")

# 4.Create a tuple to store a student’s name, age, and grade. Print the entire tuple.

# Create a tuple to store student information
student_info = ('John Doe', 18, 'Grade 12')

# Print the entire tuple
print("Student Information:", student_info)

# 5. Create a tuple to store mathematical operators (+, -, *, /) and write a program that allows users to choose an operator and perform basic calculations with two numbers

# Create a tuple to store mathematical operators
operators = ('+', '-', '*', '/')

# Function to perform calculations
def calculate(operator, num1, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Cannot divide by zero!"

# Main program
print("Welcome to the Calculator Program!")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("\nAvailable Operators:")
for op in operators:
    print(op)

operator = input("Choose an operator: ")

if operator in operators:
    result = calculate(operator, num1, num2)
    print(f"\nResult: {num1} {operator} {num2} = {result}")
else:
    print("Invalid operator! Please choose from the available operators.")
 
 