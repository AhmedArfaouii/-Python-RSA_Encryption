import hashlib
import re 
import maskpass
import random
import string
import time

def register ():

    file1 = open(r"enregistrement.txt","a")

    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

    while True:
        email = input ("Please enter your email: ")
        if re.fullmatch(regex,email) :
            break
        else :
            print ("------ This is an invalid email, please try again! ------")
        


    print ("----- Choose password creation method -----")
    print ("1 - Provide your own password. ")
    print ("2 - Generate a random password.")
    choice = input(" Please choose method 1 or 2 : ")
        
    while True:
        
        match choice :
            case '1':

        
            
                while True :
                    
                    flag = -1
                    password = maskpass.askpass(mask="*")   
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
                        delay = 2
                        for i in range(delay):
                            dashes = "-" * (i + 1)
                            print(dashes)
                            time.sleep(1)
                        
                        break
                if flag == 0 :
        
                        print ("------ CONGRATULATIONS! You are now registred! ------")
                        print ("\n")
                        time.sleep(1)
                        break                      
                else :

                        print ("*** Password doesn't match requirements (8 characters,UPPERCASE,Symbols _@$)! ***")
                
            case '2':
                

                    
                SYMB = ['@', '#', '$', '?', '.','*']

                one = random.choice(string.digits) + random.choice(string.ascii_letters) +random.choice(SYMB)
                two = random.choice(string.digits) + random.choice(string.ascii_letters) +random.choice(SYMB)
                first_password = one + two 
                gen_password = list(first_password)
                random.shuffle(gen_password)
                str1= ""
                password= str1.join(gen_password)
                print ("----- Generating your password, please wait ----- ")
                delay = 3
                for i in range(delay):
                    dashes = "-" * (i + 1)
                    print(dashes)
                    time.sleep(1)
                print(" ** Your generated password is : " , str1.join(gen_password), "Please make sure to save it somewhere safe. **")
                time.sleep(2)
                break
            
            case default :
                print ("** Please type 1 or 2 to make a choice! ** ")
                
    hashed_password= hashlib.sha256(password.encode()).hexdigest()
    file1.write(email)
    file1.write("---")
    file1.write(hashed_password)
    file1.write("\n")
    file1.close()
    print ("************************************************************")
    print ("----- Your credentials are now hashed and saved. ------")
    print ("************************************************************")
    print ("\n")
    time.sleep(2)

def login () :
    print ("----- Enter your credentials to log in! ----- ")
    print ("\n")
    

    while True:
        
        
        log = input ("Enter your Email:  ")
        pwd = maskpass.askpass(mask="*")   
        hashed_pwd= hashlib.sha256(pwd.encode()).hexdigest()
        compare = log+"---"+hashed_pwd


        file1 = open(r"enregistrement.txt","r")
        x = 0 
        for logins in file1 :
            if (compare == logins.strip()) : 
                x = 1

                
                
        if x == 1 :
            print ("----- Logging in, please wait -----")
            delay = 2
            for i in range(delay):
                dashes = "-" * (i + 1)
                print(dashes)
                time.sleep(1)
            print ("\n")
            print ("************************************************************")
            print ("CONGRATULATIONS! You have successfuly signed in! ")
            print ("************************************************************")
            print ("\n")
            time.sleep(1)

            
            break
        else :
            print ("----- Logging in, please wait -----")
            delay = 2
            for i in range(delay):
                dashes = "-" * (i + 1)
                print(dashes)
                time.sleep(1)
            print ("----- INCORRECT Email or Password, please try again!----- ")
            time.sleep(1)
            
            




