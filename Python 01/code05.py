import random

print("*" * 18)

answer00 = random.randint(1, 70)


def read_and_check_int():
    while True:
        try:
            guess00 = int(input("Whats you guess? "))
            break
        except ValueError:
            print("Please input integer only...")
            continue
    return (guess00)


input_num = read_and_check_int()

while input_num != answer00:
    if input_num > answer00:
        print("You guessed bigger")
        print("Guess another time.")
        input_num = read_and_check_int()
    elif input_num < answer00:
        print("Your guess is smaller")
        print("Guess another time.")
        input_num = read_and_check_int()

print("You've gussed it right, " + "it is " + str(answer00))
