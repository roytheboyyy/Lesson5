print('Welcome to the storygame of "Life choices" ')
print("you are buying orange juice.")
i = input("Original price of Orange juice:")
print("Oh no! it tasted terrible! And there are no refunds!!")
p = input("Your resell price")
if p > i :
    print("You made profit.")
else:
    print("You didnt make profit")

print("Now you are hungry. Want to go to McDonalds?")
Question = input("yes or no?")

if (Question == "yes"):
    print("You Enjoy McDonalds")
elif (Question == "no"):
    print("You decided not to get mcdonalds. Thats it for the day i guess!")
else:
    print("Pick yes or no. What you said, i didnt understand. Also Please don't use caps.")

print("That's it! Another part is coming soon, But day 1 is completed.")


