print("Welcome to Python Pizza!") #Welcome message

# Get pizza size from user
size = input("\nWhat size of pizza would you like?\nType 1 for Small Pizza.\nType 2 for Large Pizza.\n").strip()

# Validate pizza size input
while size not in ["1", "2"]:
    size = input("\nInvalid input. Please type 1 for Small Pizza or 2 for Large Pizza.\n").strip()

# Determine base cost based on size
if size == "1":
    base_cost = 8

elif size == "2":
    base_cost = 12

# Get number of toppings from user
available_toppings = ["Pepperoni", "Mushrooms", "Onions", "Sausage", "Bacon",
"Extra Cheese", "Black Olives", "Green Peppers", "Pineapple", "Spinach"]

# Ask user if they want to add toppings
add_topping = input("\nWould you like to add a topping? Type 'yes' or 'no'.\n").strip().lower()

# Validate add_topping input
while add_topping not in ["yes", "no"]:
    add_topping = input("\nInvalid input. Please type 'yes' or 'no'.\n").strip().lower()

# Initialize toppings count
toppings = 0

# Initialize list to keep track of added toppings
added_toppings = []

# If user wants to add toppings, display available toppings and allow selection
if add_topping == "yes":
    print("\nAvailable toppings for $1 each:")
    for topping in available_toppings:
        print(f"- {topping}")

    while True:
        selected_topping = input("\nPlease select a topping from the list above (or type 'done' to finish):\n").strip().title()
        if selected_topping == "Done":
            break
        elif selected_topping in available_toppings:
            toppings += 1
            added_toppings.append(selected_topping)
            print(f"\n{selected_topping} has been added to your pizza.")
        else:
            print("\nInvalid topping. Please select a topping from the list.")

# Get delivery or pickup option
def delivery():
    option = input("\nWould you like delivery or pickup? Type 'delivery' or 'pickup'.\n").strip().lower()
    while option not in ["delivery", "pickup"]:
        option = input("\nInvalid input. Please type 'delivery' or 'pickup'.\n").strip().lower()
    return option
delivery_option = delivery()

# Initialize distance
distance = 0
# If delivery, get distance and calculate delivery fee
if delivery_option == "delivery":
   def delivery_distance():
       while True:
           try:
               distance = float(input("\nPlease enter the delivery distance in miles:\n"))
               if distance == 0:
                   print("\nDistance cannot be zero. If you prefer pickup, please select that option.")
                   delivery_option = delivery()
               elif distance < 0:
                   print("\nDistance cannot be negative. Please enter a valid distance.")
               else:
                   return distance
           except ValueError:
               print("\nInvalid input. Please enter a numeric value for distance.")
   distance = delivery_distance()

# Calculate delivery fee based on distance
delivery_fee = 0

if distance == 0:
    delivery_fee = 0
elif 0 < distance <= 5:
    delivery_fee = 2
elif distance > 5:
    delivery_fee = 2 + (distance - 5) * 1

# Calculate total order cost
order_cost = base_cost + toppings + delivery_fee

# Display price breakdown and total cost
print(f"\nThis is your price breakdown:")
print(f"Base cost: ${base_cost:.2f}")
print(f"Toppings cost: ${toppings:.2f}")
print(f"Delivery fee: ${delivery_fee:.2f}")
print(f"\nYour total pizza order cost is: ${order_cost:.2f}")
print("\nThank you for ordering from Python Pizza!")