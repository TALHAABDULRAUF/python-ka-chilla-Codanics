fruit_basket="Orange"
print(type(fruit_basket))
#INPUT VARIABLES
name=input("What is your name?")
age=input("How old are you?")   
print("Hello!",name, ",You are still young")

# Advance Version of input variables
name = input("What is your name? ")
age_input = input("How old are you? ")

# Check if the input is a number
if age_input.isdigit():
    age = int(age_input)

    print("\n--- Result ---")
    if 13 <= age <= 19:
        print(f"Hello {name}! You're a teenager, full of energy and dreams.")
        print("✨ Keep learning, exploring, and believing in yourself. The future is yours!")
    elif 20 <= age < 30:
        print(f"Hello {name}! You are still young and your journey has just begun.")
        print("🌟 Dream big, work hard, and don’t be afraid to fail. This is your time to shine!")
    elif age >= 30:
        print(f"Hello {name}! You are not young, but you have reached a beautiful level of maturity.")
        print("💡 Use your experience to focus on what truly matters. It’s never too late to grow and inspire others.")
    else:
        print(f"Hello {name}! You're very young, enjoy your childhood and keep smiling! 😊")
else:
    print("Please enter a valid age in numbers.")
