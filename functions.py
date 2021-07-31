# Tomasz Nowak

def read_positive_integer(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            if user_input > 0:
                return user_input
        except ValueError:
            print("Whole positive numbers only please.")


def read_non_empty_string(prompt):
    while True:
        user_input = input(prompt)
        if len(user_input) > 0 and user_input.isalpha():
            return user_input
