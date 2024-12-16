import random
import string

print("Welcome to the Password Generator!")

def get_valid_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 1:
                print("Please enter a number greater than 0.")
            else:
                return value
        except:
            print("Invalid input! Please enter a valid number.")


letters_input = get_valid_input("How many letters would you like in your password? ")
symbols_input = get_valid_input("How many symbols would you like in your password? ")
numbers_input = get_valid_input("How many numbers would you like in your password? ")

letters = random.choices(string.ascii_letters, k=letters_input)
symbols = random.choices(string.punctuation, k=symbols_input)
digits = random.choices(string.digits, k=numbers_input)

raw_password = letters + symbols + digits
random.shuffle(raw_password)
password = "".join(raw_password)
print(f"Your generated password is: {password}")
