# Syed Miqdad
def encode(user_input):
    encoded_password = ""
    for i in user_input:
        i = int(i)
        if 7 <= i <= 9:
            if i == 7:
                i = "0"
            if i == 8:
                i = "1"
            if i == 9:
                i = "2"
            encoded_password += i
        else:
            i += 3
            i = str(i)
            encoded_password += i
    return encoded_password

#Nafi
def decode(encodedpassword):
    decoded_password = ""
    for i in encodedpassword:
        i = int(i)
        if 0 <= i <= 2:
            if i == 0:
                i = "7"
            if i == 1:
                i = "8"
            if i == 2:
                i = "9"
            decoded_password += i
        else:
            i -= 3
            i = str(i)
            decoded_password += i
    return decoded_password

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
            user_input = input("What is your password?")
            if len(str(user_input)) == 8:
                encoded_password = encode(user_input)
                print("Your password has been encoded and stored!")
            else:
                print("Create an 8 digit password.")
        elif menu_input == "2":
            print(f"Encoded password {encoded_password} and Decoded password {decode(encoded_password)}")
        elif menu_input == "3":
            condition = False


if __name__ == "__main__":
    main()