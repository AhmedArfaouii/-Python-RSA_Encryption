import hashlib
import re 
import maskpass
import random
import array
import string

file1 = open(r"enregistrement.txt","a")

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

while True:
    email = input ("Write your email : ")
    if re.fullmatch(regex,email) :
        print ("Valid email! ")
        break
    


print ("Choose the method : ")
print ("1- Enter your password.")
print ("2 - Generate a random password.")
    
while True:
    choice = input("Choice : ")
    match choice :
        case '1':

    
        
            while True :
                
                flag = -1
                password = maskpass.askpass(mask="")   
                if (len(password)<=6):
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
                    print("Valid Password")
                    break
            if flag == 0 :
    
                    print ("Your password is : " , password)
                    
            else :
                    print ("*****************Invalid Password ! **************")
            break
        case '2':
             

                
            SYMB = ['@', '#', '$', '?', '.','*']

            one = random.choice(string.digits) + random.choice(string.ascii_letters) +random.choice(SYMB)
            two = random.choice(string.digits) + random.choice(string.ascii_letters) +random.choice(SYMB)
            first_password = one + two 

            print ("Unshuffled password : ", first_password)
            gen_password = list(first_password)
            print ("Listed_Unshuffled_Password : ", gen_password)
            random.shuffle(gen_password)
            print ("Listed_Shuffled_Password : " ,gen_password)
            str1= ""
            password= str1.join(gen_password)
            print("Shuffled password : " , str1.join(gen_password))

            break
hashed_password= hashlib.sha256(password.encode()).hexdigest()
file1.write(email)
file1.write("---")
file1.write(hashed_password)
file1.write("\n")
file1.close()

print("Login!")
log = input ("email: ")
pwd = input ("password: ")
hashed_pwd= hashlib.sha256(pwd.encode()).hexdigest()
compare = log+"---"+hashed_pwd


file1 = open(r"enregistrement.txt","r")
x = 0 
for logins in file1 :
    if (compare == logins.strip()) : 
        print ("I FOUND IT ")
    else :
        print ("NOT FOUND!!!!")
    




