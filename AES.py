from cryptography.fernet import Fernet 
import os
from cryptography.fernet import InvalidToken

def gen_key():
    generated_key = Fernet.generate_key()
    with open('secret.key', 'wb') as key_file:
        key_file.write(generated_key)


def load_key():
    return open('secret.key', 'rb').read()

def encrypt(filename, key):
    f = Fernet(key)
    with open(filename, 'rb') as file:
        file_data=file.read()
    
    encrypted_file = f.encrypt(file_data)

    with open(filename, 'wb') as file:
        file.write(encrypted_file)
    
    print('file encrypted successfully')

def decrypt(filename, key):
    f = Fernet(key)
    with open(filename, 'rb') as file:
        encrypted_data=file.read()

    try:
        decrypted_file = f.decrypt(encrypted_data)
        print('file decrypted sucessfully')
    except InvalidToken:
        print('Invalid key')
        return
    

    with open(filename, 'wb') as file:
        file.write(decrypted_file)

def main():
    print('***WELCOME TO AES CRYPT***')
    print('***TO ENCODE PRESS E, TO DECODE PRESS D ***')
    choice = input("enter 'E' to encrypt OR 'D' to decrypt :  ").upper()

    if choice == 'E':
        Filename = input('Enter filename to encrypt (includeing file extension) : ')
        if os.path.exists(Filename):
            gen_key()
            key = load_key()
            encrypt(Filename, key)
           
        else:
            print('file not found')

    elif choice == 'D':
        Filename = input('Enter filename to decrypt (including file extension) : ')
        if os.path.exists(Filename):
            key = load_key()
            decrypt(Filename, key)
        else:
            print('file not found')

    else:
        print('invalid choice .Please enter e to encrypt or d to decrypt')

if __name__=='__main__':
    main()