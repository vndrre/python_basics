import random

lower_bound = 0
upper_bound = 100
max_attempts = 100


secret_number = random.randint(lower_bound, upper_bound)


def get_guess():
    while True:
        try:
            guess = int(input(f"Arva ära number {lower_bound}-st {upper_bound}-ni: "))
            if lower_bound <= guess <= upper_bound:
                return guess
            else:
                print("Vale number. Palun sisesta number 0-st 100-ni.")
        except ValueError:
            print("Vale number. Palun sisesta õige number.")


def check_guess(guess, secret_number):
    if guess == secret_number:
        return "Õige"
    elif guess < secret_number:
        return "Liiga väike"
    else:
        return "Liiga suur"

def play_game():
    attempts = 0
    won = False

    while attempts < max_attempts:
        attempts += 1
        guess = get_guess()
        result = check_guess(guess, secret_number)

        if result == "Õige":
            print(f"Palju õnne! Sa arvasid õige numbri {secret_number}. Sul läks {attempts} korda ära arvamiseks.")
            won = True
            break
        else:
            print(f"{result}. Proovi uuesti.")

    if not won:
        print(f"Vabandust, teil pole enam arvamis kordi.. Õige number on {secret_number}.")

if __name__ == "__main__":
    print("Tere tulemast arvu ära arvamis mängu!")
    play_game()