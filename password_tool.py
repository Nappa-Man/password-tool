import secrets
import string

#checking the user password
option = input("Wanna generate or check a password? ")

if option.lower() == "check":
    password = input("Enter your password: ")



    bad_passwords = ["password", "12345", "taco", "00987"]

    if password.lower() in bad_passwords:
        print("password is too basic!!")
    else:
        score = 0

        if len(password) >= 12:
            score = score + 1

        if any(char.isdigit() for char in password):
            score = score + 1

        if any(char.isupper() for char in password):
            score = score + 1

        if any(char in string.punctuation for char in password):
            score = score + 1

        if score == 4:
            print("You pass!!")
        elif score >= 2:
            print("Mediocre password. Try to make it stronger.")
        else:
            print("WEAK PASSWORD!!")

elif option.lower() == "generate":
    all_chars = string.ascii_letters + string.digits + string.punctuation
    new_password = "".join(secrets.choice(all_chars) for _ in range(14)) 
    print("New password is:", new_password) 





