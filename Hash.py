import hashlib
import bcrypt
import maskpass

def create_word ():
   word = maskpass.askpass ("Please enter a word to use : ",mask="*")
   f = open ("word_to_hash.txt","w")
   f.write (word)
   f.close

def sha256 ():
    f = open ("word_to_hash.txt","r")
    word = f.read()
    print (word)
    hashed_word = hashlib.sha256(word.encode()).hexdigest()
    f1 = open ("word_hashed_256.txt","w")
    f1.write(hashed_word)
    f1.close()
    
def salt_bcrypt() :
    
    f = open ("word_to_hash.txt","r")
    word = f.read().encode() 

    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(word, salt)
    f1 = open ("word_bcrypted.txt", "wb")
    f1.write (hashed)
    f1.close


def dictionary_attack():
    #abacination0 un mot dans mon password_dict
        x=0
        with open("password_dictionary.txt",'r') as dict_file:
            words = dict_file.read().splitlines()

        with open("word_hashed_256.txt", 'r') as hashed_file:
            hashed_password = hashed_file.read().strip()

        for word in words:
            hashed_word = hashlib.sha256(word.encode()).hexdigest()
            if hashed_word == hashed_password:
                print (f"Password found: {word}")
                x=1
            
        if x == 0 :
            print ("Password not found :( )")
                
            

