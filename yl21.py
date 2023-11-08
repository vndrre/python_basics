import random

lower_bound = 1
upper_bound = 100
max_attempt = 1000
secret_number = random.randint(lower_bound, upper_bound)

def get_guess():
    while True:
        try:
            guess = int(input("Arva ära õige number {lower_bound} ja {upper_bound} vahel: "))
            if lower_bound <= guess <= upper_bound:
                return guess
            else:
                print("Invalid input. Please enter a number within the specified range.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def check_guess(guess, secret_number):
    if guess == secret_number:
        return "Õige!"
    elif guess < secret_number:
        return "Liiga väike.."
    else:
        return "Liiga suur.."