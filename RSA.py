import rsa
import os

def generate_key():
    public_key,private_key=rsa.newkeys(1024)

    with open('pubkey.pem','wb') as file:
        file.write(public_key.save_pkcs1('PEM'))

    with open('privkey.pem','wb') as file:
        file.write(private_key.save_pkcs1('PEM'))

def load_key():
    with open('pubkey.pem','rb') as file:
        public_key=rsa.PublicKey.load_pkcs1(file.read())

    with open('privkey.pem','rb') as file:
        private_key=rsa.PrivateKey.load_pkcs1(file.read())

    return public_key,private_key


def encrypt(filename,key):

    with open(filename,'rb') as file:
        file_data=file.read()

    encrypted_data=rsa.encrypt(file_data,key)
    #eccrypted_data=rsa.encrypt(file_data.encode('ascii'),key)

    with open(filename,'wb') as file:
        file.write(encrypted_data)

    print('file encrypted successfully')

def decrypt(filename,key):
    with open(filename,'rb') as file:
        cypher_text=file.read()
    try:
       # decrypted_text= rsa.decrypt(cypher_text,key).decode('ascii')
        decrypted_text= rsa.decrypt(cypher_text,key)
    except:
        return False
    
    with open(filename,'wb') as file:
        file.write(decrypted_text)

    print('file decrypted successfully')


def main():
    print('***WELCOME TO RSA ENCRYPT***')
    print('***ENTER E TO ENCRYPT AND D TO DECRYPT***')

    choice=input('enter E to encrypt or D to decrypt : ').upper()

    if choice=='E':
        filename=input('Please enter filename (including extension) : ')
        if os.path.exists(filename):
            generate_key()
            public_key,private_key=load_key()
            encrypt(filename,public_key)
        else:
            print('file not found')

    elif choice=='D':
        filename=input('please enter filename (including extension) : ')
        if os.path.exists(filename):
            public_key,private_key=load_key()
            decrypt(filename,private_key)
        else:
            print('file not found')

    else:
        print('invalid choice ,Press d for decrypt or e for encrypt')

if __name__=='__main__':
    main()