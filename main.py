
def encode():
    user_input = input("What is your password?")
    encoded_password = ""
    for i in user_input:
        i = int(i)
        if i == 9:
            i = 0
            i += 3
            i = str(i)
            encoded_password += i
        else:
            i += 3
            i = str(i)
            encoded_password += i
    return encoded_password


def main():
    condition = True
    while condition == True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        menu_input = input("Please enter an option:")
        if menu_input == "1":
            encode()
            print("Your password has been encoded and stored!")


if __name__ == "__main__":
    main()