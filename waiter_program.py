# Waiter Program

starters = ("Green salad", "Garlic bread", "Minestrone soup")
mains = ("Lasagne", "Spaghetti Bolognese", "Margherita pizza")
dessert = ("Tiramisu", "Panna Cotta", "Lemon cake")

print("Welcome to the restaurant!")
print("Here is our menu for you to order from.")
print( "Starters to choose from: " + str(starters))
starter_order= input()
print( "Great choice! Now for the main course we have: " + str(mains))
main_order = input()
print("Excellent choice. Now for the best part here are our dessert options" + str(dessert))
dessert_order = input()
print("Fantastic choices all around so to summarise you have ordered " + starter_order.capitalize() + " as your starter," + main_order.capitalize() + " for your main course and for dessert you have decided on " + dessert_order.capitalize() )
print("I will be back shortly with your starter")
