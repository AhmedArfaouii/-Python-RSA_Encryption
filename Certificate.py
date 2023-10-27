from OpenSSL import crypto
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend  
from cryptography import x509

def cert_gen(
    emailAddress="ahmed.arfaouii11@gmail.com",
    commonName="AhmedArfaoui",
    countryName="TN",
    organizationName="Tekup",
    serialNumber=0,
    validityStartInSeconds=0,
    validityEndInSeconds=10*365*24*60*60,
    KEY_FILE = "private.key",
    CERT_FILE="selfsigned.crt"):
    #can look at generated file using openssl:
    #openssl x509 -inform pem -in selfsigned.crt -noout -text
    
    
    k = crypto.PKey()
    k.generate_key(crypto.TYPE_RSA, 4096)
    
    
    
    cert = crypto.X509()
    cert.get_subject().C = countryName
    cert.get_subject().O = organizationName
    cert.get_subject().CN = commonName
    cert.get_subject().emailAddress = emailAddress
    cert.set_serial_number(serialNumber)
    cert.gmtime_adj_notBefore(0)
    cert.gmtime_adj_notAfter(validityEndInSeconds)
    cert.set_issuer(cert.get_subject())
    cert.set_pubkey(k)
    cert.sign(k, 'sha512')
    with open(CERT_FILE, "wt") as f:
        f.write(crypto.dump_certificate(crypto.FILETYPE_PEM, cert).decode("utf-8"))
    with open(KEY_FILE, "wt") as f:
        f.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, k).decode("utf-8"))

def encrypt_w_cert () :
    with open("selfsigned.crt","rb") as cert_file:
        certificate = x509.load_pem_x509_certificate(cert_file.read(), default_backend())
    public_key = certificate.public_key()
    
    message = b"Your message to encrypt"

    encrypted_message = public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    f =open ("encrypted_w_cert.txt","wb")
    f.write(encrypted_message)
    f.close
    
def decrypt_w_cert():

    with open("private.key", "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )

    with open("encrypted_w_cert.txt", "rb") as encrypted_file:
        encrypted_message = encrypted_file.read()

    decrypted_message = private_key.decrypt(
        encrypted_message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    print(decrypted_message.decode())
    
