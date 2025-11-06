START

PRINT "Welcome to Python Pizza!"

// Get pizza size from user
PROMPT "What size of pizza would you like? Type 1 for Small Pizza, 2 for Large Pizza"
READ size
REMOVE whitespace from size

// Validate pizza size input
WHILE size is not "1" AND size is not "2"
    PROMPT "Invalid input. Please type 1 for Small Pizza or 2 for Large Pizza."
    READ size
    REMOVE whitespace

// Determine base cost
IF size = "1" THEN
    base_cost = 8
ELSE IF size = "2" THEN
    base_cost = 12
END IF

// Define available toppings
available_toppings = ["Pepperoni", "Mushrooms", "Onions", "Sausage", "Bacon",
                      "Extra Cheese", "Black Olives", "Green Peppers", "Pineapple", "Spinach"]

// Ask if user wants toppings
PROMPT "Would you like to add a topping? Type 'yes' or 'no'"
READ add_topping
CONVERT add_topping to lowercase
REMOVE whitespace

// Validate add_topping input
WHILE add_topping is not "yes" AND add_topping is not "no"
    PROMPT "Invalid input. Please type 'yes' or 'no'"
    READ add_topping
    CONVERT to lowercase
    REMOVE whitespace

// Initialize toppings count and list
toppings = 0
added_toppings = []

// If user wants toppings
IF add_topping = "yes" THEN
    PRINT "Available toppings for $1 each:"
    FOR each topping in available_toppings
        PRINT topping
    END FOR

    WHILE TRUE
        PROMPT "Select a topping from the list (or type 'done' to finish)"
        READ selected_topping
        CONVERT first letter of each word in selected_topping to uppercase

        IF selected_topping = "Done" THEN
            BREAK
        ELSE IF selected_topping is in available_toppings THEN
            toppings = toppings + 1
            ADD selected_topping to added_toppings
            PRINT selected_topping + " has been added to your pizza."
        ELSE
            PRINT "Invalid topping. Please select from the list."
        END IF
    END WHILE
END IF

// Ask for delivery or pickup
DEFINE FUNCTION get_delivery_option
    PROMPT "Would you like delivery or pickup? Type 'delivery' or 'pickup'"
    READ option
    CONVERT option to lowercase
    REMOVE whitespace
    WHILE option is not "delivery" AND option is not "pickup"
        PROMPT "Invalid input. Please type 'delivery' or 'pickup'"
        READ option
        CONVERT to lowercase
        REMOVE whitespace
    END WHILE
    RETURN option
END FUNCTION

delivery_option = CALL get_delivery_option()

// Initialize distance
distance = 0

// If delivery, get distance
IF delivery_option = "delivery" THEN
    DEFINE FUNCTION get_delivery_distance
        WHILE TRUE
            PROMPT "Enter delivery distance in miles"
            READ distance
            IF distance is numeric THEN
                CONVERT distance to number
                IF distance = 0 THEN
                    PRINT "Distance cannot be zero. Choose pickup instead."
                    delivery_option = CALL get_delivery_option()
                ELSE IF distance < 0 THEN
                    PRINT "Distance cannot be negative. Enter a valid distance."
                ELSE
                    RETURN distance
                END IF
            ELSE
                PRINT "Invalid input. Enter a numeric value."
            END IF
        END WHILE
    END FUNCTION

    distance = CALL get_delivery_distance()
END IF

// Calculate delivery fee
IF distance = 0 THEN
    delivery_fee = 0
ELSE IF distance <= 5 THEN
    delivery_fee = 2
ELSE
    delivery_fee = 2 + (distance - 5) * 1
END IF

// Calculate total order cost
order_cost = base_cost + toppings + delivery_fee

// Display breakdown
PRINT "Price breakdown:"
PRINT "Base cost: $" + base_cost
PRINT "Toppings cost: $" + toppings
PRINT "Delivery fee: $" + delivery_fee
PRINT "Total pizza order cost: $" + order_cost

PRINT "Thank you for ordering from Python Pizza!"

END