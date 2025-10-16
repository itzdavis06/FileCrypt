import AES
import os
import RSA

def main():
    print('***WELCOME TO HYBRID ENCRYPT')

    #to encrypt data
    choice=input('PRESS E TO Encrypt OR D to decrypt : ').upper()

    if choice=='E':
        AES.gen_key()
        AES_key=AES.load_key()
        filename=input('Enter file to be encrypted (including file extension : )')
        if os.path.exists(filename):
            try:
                AES.encrypt(filename,AES_key)
            except:
                print('File does not exist')
        
        
        RSA.generate_key()
        RSA_publicKey,RSA_privateKey=RSA.load_key()
        filename2=input('Enter your symmetric secret key (including file extension) : ')
        if os.path.exists(filename2):
            try:
                RSA.encrypt(filename2,RSA_publicKey)
            except:
                print('secret key does not exist')

    elif choice=='D':
         RSA_publicKey,RSA_privateKey=RSA.load_key()
         filename=input('Enter your encrypted secret key (including file extension) : ')
         if os.path.exists(filename):
             try:
                 RSA.decrypt(filename,RSA_privateKey)
             except:
                print('encrypted secret key not found')

         AES_key=AES.load_key()
         filename2=input('Enter encrypted file (including file extension) : ')
         if os.path.exists(filename2):
             try:
                 AES.decrypt(filename2,AES_key)
             except:
                print('Encrypted file not found') 

    else:
        print('invalid choice,press E to encrypt OR  D to decrypt')   

if __name__=='__main__':
    main()


    
