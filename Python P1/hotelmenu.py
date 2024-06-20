menu = {
"Coffee":50,
"Pizza":100,
"Burger":80,
"Pasta":90,
"Sandwich":100
}

# Greet to customer
print("Welcome to PYTHON Restaurant")
print(" Coffee:50\n Pizza:100\n Burger:80\n Pasta:90\n Sandwich:100") 

total_order = 0
#100+50 = 150

item_1 = input("Enter name of item you want to order =  ")
if item_1 in menu:
    total_order += menu[item_1]
    print("Your item has been added to your order")

else:
    print("Ordered item is not avilable yet")

another_variable = input("Do you want to add another item? (yes/no)")
if another_variable =="yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        total_order += menu[item_2]
        print("Item has been added to order")
    else:
        print("ordered item is not avilable!")
print(f"The total amount of items to pay is {total_order}")