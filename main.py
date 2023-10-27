from Hash import create_word
from Hash import sha256
from Hash import salt_bcrypt
from Hash import dictionary_attack
from emailpass import register
from emailpass import login
import RSA
import Certificate


def big_menu():
    print("Welcome to the functionalities menu !")
    print ("Please choose which function to try !")
    print("1 - Hash")
    print("2 - RSA")
    print("3 - Certificate")
    print("0 - Exit")
    
def main_menu():
    print("Main Menu")
    print("1 - Sign up")
    print("2 - Login")
    print("0 - Exit")

def sign_up_menu():
    print("Sign Up Menu")
    print("a - Register")
    print("0 - Back to Main Menu")

def login_menu():
    print("Login Menu")
    print("a - Enter credentials")
    print("0 - Back to Main Menu")

def hash_menu():
    print("Hash Menu")
    print("1 - Give word to hash")
    print("2 - Hash it with 256")
    print("3 - Hash it with salt")
    print("4-  Dictionary attack on your word")
    print("0 - Back to Login Menu")

def rsa_menu():
    print("RSA Menu")
    print("1 - Generate key")
    print("0 - Back to Login Menu")

def main():
    while True:
        main_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            while True:
                sign_up_menu()
                signup_choice = input("Enter your choice: ")

                if signup_choice == 'a':
                    register()
        

                elif signup_choice == '0':
                    break

                else:
                    print("Invalid choice. Please try again.")

        elif choice == '2':
            while True:
                login()
                big_menu()
                login_choice = input("Enter your choice: ")

                if login_choice == '1':
                    while True:
                        hash_menu()
                        hash_choice = input("Enter your choice: ")

                        if hash_choice == '1':
                            create_word()
                            

                        elif hash_choice == '2':
                            sha256()

                        elif hash_choice == '3':
                            
                            salt_bcrypt()
                            
                        elif hash_choice == '4':
                            
                            dictionary_attack()

                        elif hash_choice == '0':
                            break

                        else:
                            print("Invalid choice. Please try again.")

                elif login_choice == '2':
                    while True:
                        rsa_menu()
                        rsa_choice = input("Enter your choice: ")

                        if rsa_choice == '1':
                            # Call your function for generating RSA key
                            print("Generate RSA key function")

                        elif rsa_choice == '0':
                            break

                        else:
                            print("Invalid choice. Please try again.")
                            
                elif login_choice == '3':
                    
                    while True:
                         
                        certif_choice = input("Enter your choice: ")

                        if certif_choice == '1':
                            # Call your function for generating RSA key
                            break

                        elif certif_choice == '0':
                            break

                        else:
                            print("Invalid choice. Please try again.")
                        

                elif login_choice == '0':
                    break

                else:
                    print("Invalid choice. Please try again.")

        elif choice == '0':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()


