import random
a = 100
b = 0
pc_guessed = random.randint(1, 99)
print(pc_guessed)

user_feedback = str(input())

while user_feedback != "d":
    if user_feedback == "k": # the number pc guessed is bigger than what user has in mind.
        a = pc_guessed
        if a <= 0:
            a = 100
        c = a
        d = b
        if (c-1) == (d+1) or b > a or a == b:
            a = 100
            b = 0
        pc_guessed = random.randint(b+1, a-1)
        print(pc_guessed)
        user_feedback = str(input())

    elif user_feedback == "b":
        b = pc_guessed
        if b >= 100:
            b = 0
        c = a
        d = b
        if (c-1) == (d+1) or b > a or a == b:
            a = 100
            b = 0
        pc_guessed = random.randint(b+1, a-1)
        print(pc_guessed)
        user_feedback = str(input())
