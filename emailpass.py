import hashlib
import re 
import maskpass
import random
import array
import string

def register ():

    file1 = open(r"enregistrement.txt","a")

    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

    while True:
        email = input ("Please enter your email: ")
        if re.fullmatch(regex,email) :
            break
        else :
            print ("This is an invalid email, please try again!")
        


    print ("Choose password creation method : ")
    print ("1- Provide your own password. ( > 8 characters, requires uppercase and symbols.)")
    print ("2 - Generate a random password.")
        
    while True:
        choice = input("Choice : ")
        match choice :
            case '1':

        
            
                while True :
                    
                    flag = -1
                    password = maskpass.askpass(mask="")   
                    if (len(password)<=8):
                        flag = -1
                        break
                    elif not re.search("[a-z]", password):
                        flag = -1
                        break
                    elif not re.search("[A-Z]", password):
                        flag = -1
                        break
                    elif not re.search("[0-9]", password):
                        flag = -1
                        break
                    elif not re.search("[_@$]" , password):
                        flag = -1
                        break
                    else:
                        flag = 0
                        print("Password : Validated. ")
                        print ("CONGRATULATIONS! You are now registred! ")
                        break
                if flag == 0 :
        
                        print ("Your password is : " , password)
                        
                else :
                        print ("***Password doesn't much requirements (8 characters + Uppercase/Symbols)! ***")
                break
            case '2':
                

                    
                SYMB = ['@', '#', '$', '?', '.','*']

                one = random.choice(string.digits) + random.choice(string.ascii_letters) +random.choice(SYMB)
                two = random.choice(string.digits) + random.choice(string.ascii_letters) +random.choice(SYMB)
                first_password = one + two 

                # print ("Unshuffled password : ", first_password)
                gen_password = list(first_password)
                # print ("Listed_Unshuffled_Password : ", gen_password)
                random.shuffle(gen_password)
                # print ("Listed_Shuffled_Password : " ,gen_password)
                str1= ""
                password= str1.join(gen_password)
                print("Your generated password is : " , str1.join(gen_password), "Please make sure to save it somewhere safe.")

                break
            case default :
                print ("Please type 1 or 2 to make a choice! ")
                
    hashed_password= hashlib.sha256(password.encode()).hexdigest()
    file1.write(email)
    file1.write("---")
    file1.write(hashed_password)
    file1.write("\n")
    file1.close()
    print ("************************************************************")
    print ("Your credentials are now hashed and saved on the local file.")
    print ("************************************************************")
    print ("\n")


print ("Enter your credentials to log in : ")

while True:
    
    
    log = input ("Email :  ")
    pwd = input ("Password : ")
    hashed_pwd= hashlib.sha256(pwd.encode()).hexdigest()
    compare = log+"---"+hashed_pwd


    file1 = open(r"enregistrement.txt","r")
    x = 0 
    for logins in file1 :
        if (compare == logins.strip()) : 
            x = 1
        else :
            x = 0
            
            
    if x == 1 :
        print ("CONGRATULATIONS! You have successfuly signed in! ")
        break
    else :
        print ("Incorrect Email or Password, please try again!")
            
    




