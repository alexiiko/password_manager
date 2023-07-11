import random 
import os

def create_file_in_folder():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_directory, "passwords.txt")
    open(file_path, "a").close()

def generate_password():
    password = ""
    character = []

    length = int(input("How many characters long should the password be? "))

    for _ in range(length):
        upper_case = chr(random.randint(65,90))
        lower_case = chr(random.randint(97, 122))
        number = chr(random.randint(48, 57))
        symbols = chr(random.randint(33,38))

        character.append(upper_case)
        character.append(lower_case)
        character.append(number)
        character.append(symbols)

        password += str(random.choice(character))

    print()
    print(f"Password: {password}")
    return password

def add_password(account, password):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_directory, "passwords.txt")
    with open(file_path, "a") as file_data:
        file_data.write(f"{account} | {password}\n")
    print("Added the password successfully.")

def view_passwords():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_directory, "passwords.txt")
    with open(file_path, "r") as file_data:
        for password in file_data:
            print(password)

create_file_in_folder()

generate_add_view = input("Do you want to generate, add or view passwords? ").lower()
while True:
    if generate_add_view == "generate":
        print()
        password = generate_password()
        add_into_file = input("Do you want to add the password? Y/N ").upper()
        if add_into_file == "Y":
            account = input("For what account is the password? ")
            add_password(account, password)
            print()
            generate_add_view = input("Do you want to generate, add or view passwords? ").lower()
            continue
        elif add_into_file == "N":
            generate_add_view = input("Do you want to generate, add or view passwords? ").lower()
            continue
        else:
            print("Wrong input.")
            add_into_file = input("Do you want to add the password? Y/N ").upper()
            continue

    elif generate_add_view == "add":
        account = input("What account is the password for? ")
        password = input("What password should it be? ")
        add_password(account, password)
        print()
        generate_add_view = input("Do you want to generate, add or view passwords? ").lower()
        continue

    elif generate_add_view == "view":
        print()
        view_passwords()
        print()
        generate_add_view = input("Do you want to generate, add or view passwords? ").lower()
        continue

    else:
        print("Wrong input.")
        generate_add_view = input("Do you want to generate, add or view passwords? ").lower()
        continue