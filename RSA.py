from cryptography.hazmat.backends import default_backend  
from cryptography.hazmat.primitives import serialization  
from cryptography.hazmat.primitives.asymmetric import rsa  
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA



def save_file(filename, content):  
   f = open(filename, "wb")  
   f.write(content)
   f.close()  
  
 
def generate_key (): 
    private_key = rsa.generate_private_key( 
        public_exponent=65537,  
        key_size=4096,  
        backend=default_backend()  
    )  


    pem = private_key.private_bytes(  
        encoding=serialization.Encoding.PEM,  
        format=serialization.PrivateFormat.PKCS8,  
        encryption_algorithm=serialization.NoEncryption()  
    )  
    save_file("private.pem", pem)  
    

    public_key = private_key.public_key()  
    pem = public_key.public_bytes(  
        encoding=serialization.Encoding.PEM,  
        format=serialization.PublicFormat.SubjectPublicKeyInfo  
    )  
    save_file("public.pem", pem)  

def message_encrypt () :
    
    input1 = input ("Please enter your message :")
    message = input1.encode()

    key = RSA.import_key(open('public.pem').read())
    cipher = PKCS1_OAEP.new(key)
    ciphertext = cipher.encrypt(message)
    f= open ("encrypted_message.txt","wb")
    f.write(ciphertext)
    f.close()

def message_decrypt () : 

    key = RSA.import_key(open('private.pem').read())
    with open("encrypted_message.txt", "rb") as file:
        ciphertext = file.read()
    cipher = PKCS1_OAEP.new(key)
    plaintext = cipher.decrypt(ciphertext)
    print (plaintext.decode("utf-8"))


