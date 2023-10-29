from Hash import create_word
from Hash import sha256
from Hash import salt_bcrypt
from Hash import dictionary_attack
from emailpass import register
from emailpass import login
from RSA import generate_key
from RSA import message_encrypt
from RSA import message_decrypt
from RSA import sign_message
from RSA import verify_signature
from Certificate import cert_gen
from Certificate import encrypt_w_cert
from Certificate import decrypt_w_cert
import time


def big_menu():
    print("******* Welcome to the functionalities menu ! *******")
    print("******* Please choose which function to try ! *******")
    print("******* 1 - Hash *******")
    print("******* 2 - RSA *******")
    print("******* 3 - Certificate *******")
    print("******* 0 - Previous Menu *******")
    
def main_menu():
    print("******* Main Menu *******")
    print("******* 1 - Sign up *******")
    print("******* 2 - Login *******")
    print("******* 0 - Exit *******")

def hash_menu():
    print("******* Hash Menu *******")
    print("******* 1 - Give word to hash *******")
    print("******* 2 - Hash it with 256 *******")
    print("******* 3 - Hash it with salt *******")
    print("******* 4-  Dictionary attack on your word *******")
    print("******* 0 - Back to Previous Menu *******")

def rsa_menu():
    print("******* RSA Menu *******")
    print("******* 1 - Generate key *******")
    print("******* 2 - Encrypt a message with RSA *******")
    print("******* 3 - Decrypt your message *******")
    print("******* 4- Sign a message with RSA *******")
    print("******* 5- Verify the message signature *******")
    print("******* 0 - Back to Previous Menu *******")
    
def certif_menu():
    print("******* Ceritificate Menu *******")
    print("******* 1 - Generate Autosigned Certificate with RSA *******")
    print("******* 2 - Encrypt a message with your Certificate *******")
    print("******* 3 - Decrypt the message *******")
    print("******* 0 - Back to Previous Menu *******")

def main():
    while True:
        main_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            while True:
                delay = 1
                for i in range(delay):
                    dashes = "-" * (i + 1)
                    print(dashes)
                    time.sleep(1)
                register()
                
                break
                
        

        elif choice == '2':
            while True:
                delay = 1
                for i in range(delay):
                    dashes = "-" * (i + 1)
                    print(dashes)
                    time.sleep(1)
                    
                login()
                big_menu()
                login_choice = input("Enter your choice: ")

                if login_choice == '1':
                    
                    while True:
                        
                        delay = 1
                        for i in range(delay):
                            dashes = "-" * (i + 1)
                            print(dashes)
                            time.sleep(1)
                        
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
                            print("----- Invalid choice. Please try again. -----")

                elif login_choice == '2':
                    
                    while True:
                        delay = 1
                        for i in range(delay):
                            dashes = "-" * (i + 1)
                            print(dashes)
                            time.sleep(1)
                        
                        rsa_menu()
                        
                        rsa_choice = input("Enter your choice: ")

                        if rsa_choice == '1':
                            generate_key()
                        elif rsa_choice == '2':
                            message_encrypt()
                        elif rsa_choice == '3':
                            message_decrypt()
                        elif rsa_choice == '4':
                            sign_message()
                        elif rsa_choice == '5':
                            verify_signature()
                        elif rsa_choice == '0':
                            
                            break

                        else:
                            print("----- Invalid choice. Please try again. -----")
                            
                elif login_choice == '3':
                    
                    while True:
                        delay = 1
                        for i in range(delay):
                            dashes = "-" * (i + 1)
                            print(dashes)
                            time.sleep(1)
                        certif_menu()
                        certif_choice = input("Enter your choice: ")

                        if certif_choice == '1':
                            cert_gen()
                        elif certif_choice == '2':
                            encrypt_w_cert()
                        elif certif_choice == '3':
                            decrypt_w_cert()

                        elif certif_choice == '0':
                            break

                        else:
                            print("----- Invalid choice. Please try again. -----")
                        

                elif login_choice == '0':
                    break

                else:
                    print("----- Invalid choice. Please try again. ------")

        elif choice == '0':
            print("----- Exiting the program. Goodbye! ----- ")
            delay = 3
            for i in range(delay):
                dashes = "-" * (i + 1)
                print(dashes)
                time.sleep(1)
            break

        else:
            print("----- Invalid choice. Please try again. -----")

if __name__ == '__main__':
    main()


