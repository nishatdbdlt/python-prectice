# students =[]
#
# def add_student():
#     name= input("enter your name")
#     marks = []
#     for i in range(1,4):
#         mark= int(input(f'enter your marks{i}'))
#         marks.append(mark)
#         students.append({'name':name,'marks':marks})
#
# def display_student():
#     print('all student')
#     for i , student  in enumerate(students,start=1):
#         print(f"{i}. {student['name']} - Marks: {student['marks']}")
#
# def calculation():
#     print("\nTotal and Average Marks:")
#     for  student in students:
#         totall= sum(student['marks'])
#         average =totall/ len(student['marks'])
#         print(f"{student['name']} → Total: {totall}, Average: {average:.2f}")
#
# def finad_topper():
#     if not students:
#         print('no student fund')
#         return
#     topper=max(students,key=lambda  s: sum(s['marks']))
#     total = sum(topper['marks'])
#     print(f"\nTopper: {topper['name']} with Total Marks: {total}")
# def fail_student():
#     print("\nFailed Students (marks < 40 in any subject):")
#     for student in students:
#         if any( m< 40 for m in student['marks']):
#             print(student['name'], "→ Marks:", student['marks'])
#
# while True:
#     print("\n--- Student Management ---")
#     print("1. Add Student")
#     print("2. Display Students")
#     print("3. Total & Average")
#     print("4. Topper")
#     print("5. Failed Students")
#     print("6. Exit")
#
#     choice = input("Enter your choice: ")
#     if choice == '1':
#         add_student()
#     elif choice =='2':
#         display_student()
#     elif choice == '3':
#         calculation()
#     elif  choice == '4':
#         finad_topper()
#     elif choice =='5':
#         fail_student()
#
inventory = []

def add_item():
    name = input("Enter item name: ")
    code = input("Enter item code: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per unit: "))

    # Check for duplicate code
    for item in inventory:
        if item['code'] == code:
            print("Item code already exists. Updating stock instead.")
            item['quantity'] += quantity
            item['price'] = price
            return

    inventory.append({
        'name': name,
        'code': code,
        'quantity': quantity,
        'price': price
    })
    print(f"Item '{name}' added successfully!")

def update_item():
    code = input("Enter item code to update: ")
    for item in inventory:
        if item['code'] == code:
            print(f"Current quantity: {item['quantity']}, Current price: {item['price']}")
            item['quantity'] = int(input("Enter new quantity: "))
            item['price'] = float(input("Enter new price per unit: "))
            print("Item updated successfully!")
            return
    print("Item not found!")

def display_inventory():
    if not inventory:
        print("Inventory is empty!")
        return
    print("\n--- Inventory ---")
    print(f"{'Code':<10} {'Name':<20} {'Quantity':<10} {'Price':<10} {'Total Value':<10}")
    for item in inventory:
        total_value = item['quantity'] * item['price']
        print(f"{item['code']:<10} {item['name']:<20} {item['quantity']:<10} {item['price']:<10.2f} {total_value:<10.2f}")

def search_item():
    code = input("Enter item code to search: ")
    for item in inventory:
        if item['code'] == code:
            print(f"Found: {item['name']} - Quantity: {item['quantity']}, Price: {item['price']}")
            return
    print("Item not found!")

def delete_item():
    code = input("Enter item code to delete: ")
    for i, item in enumerate(inventory):
        if item['code'] == code:
            del inventory[i]
            print("Item deleted successfully!")
            return
    print("Item not found!")

def low_stock():
    threshold = int(input("Enter stock threshold: "))
    print("\n--- Low Stock Items ---")
    for item in inventory:
        if item['quantity'] < threshold:
            print(f"{item['name']} - Quantity: {item['quantity']}")

def total_inventory():
    total_value = sum(item['quantity'] * item['price'] for item in inventory)
    print(f"\nTotal inventory value: {total_value:.2f}")

# Main menu
while True:
    print("\n--- Inventory Management System ---")
    print("1. Add Item")
    print("2. Update Item")
    print("3. Display Inventory")
    print("4. Search Item")
    print("5. Delete Item")
    print("6. Low Stock Report")
    print("7. Total Inventory Value")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_item()
    elif choice == '2':
        update_item()
    elif choice == '3':
        display_inventory()
    elif choice == '4':
        search_item()
    elif choice == '5':
        delete_item()
    elif choice == '6':
        low_stock()
    elif choice == '7':
        total_inventory()
    elif choice == '8':
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.")
inventory = []

def add_item():
    name = input("enter your name")
    code = input("enter your code")
    quantity= input("enter your quantity")
    price = input('enter price')

    for item in inventory:
        if item['code'] == code:
            print('already exixt')
            item [quantity] += quantity
            return
        inventory.append({
            'name': name,
            'price':price,
             'code':code,
            'quantity' : quantity
        })
        print(f"item '{name}' added ")
def update():
    code = input("enter your code")
    for item in inventory:
        if item ['code'] == code:
            print(f" currnet quantitu:{item['quantity']},current parice :{'price'}")
            item ['quantity'] = int(input('enter your quantity'))
            item['price'] = float(input('enter your parice'))
            print('uudate done')
            return

def display_inventory():
            if not inventory:
                print("Inventory is empty!")
                return
            print("\n--- Inventory ---")
            print(f"{'Code':<10} {'Name':<20} {'Quantity':<10} {'Price':<10} {'Total Value':<10}")
            for item in inventory:
                total_value = item['quantity'] * item['price']
                print(
                    f"{item['code']:<10} {item['name']:<20} {item['quantity']:<10} {item['price']:<10.2f} {total_value:<10.2f}")


def search_item():
        code = input("enter your code")
        for i, item in enumerate(inventory):
            if item ['code']== code:
                print(f"Found: {item['name']} - Quantity: {item['quantity']}, Price: {item['price']}")
                return
            print("Item not found!")
def delet_item():
    code = input("enter your code")
    for i, item in enumerate(inventory):
        if item['code'] == code:
            del inventory[i]
            print('delete done')
            return
        print('not found')
def low_stock():
    threshold = int (input("enter stock thresolhd"))

    print("low stock")
    for item in inventory:
        if item ['quantity'] > threshold:
            print(f"{item['name']} - Quantity: {item['quantity']}")


def total_inventory():
    total_value = sum(item['quantity']*item['price'] for item in inventory)

while True:
    print("\n--- Inventory Management System ---")
    print("1. Add Item")
    print("2. Update Item")
    print("3. Display Inventory")
    print("4. Search Item")
    print("5. Delete Item")
    print("6. Low Stock Report")
    print("7. Total Inventory Value")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice =='1':
        add_item()
    elif choice == '2':
        update()
    elif choice =='3':
        display_inventory()
    elif choice =='4':
        search_item()
    elif choice=='5':
        delet_item()
    elif choice =='6':
        low_stock()
    elif choice == '7':
        total_inventory()
    else:
        print(" invalide choice")


