import hashlib
import bcrypt
import re 
import maskpass
import random
import string

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
    f1 = open ("word_hashed_256","wb")
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
    
