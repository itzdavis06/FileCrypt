import hybrid
import AES
import RSA

if __name__=="__main__":
    print('***WELCOME FILE CRYPT***')
    print('***Press A for AES ENCRYPTION , R for RSA ENCRYPTION OR H for HYBRID ENCRYPTION ***')
    choice=input('ENTER YOUR CHOICE : ').upper()
    print()
    print()
    if choice=='A':
        AES.main()
        
    elif choice=='R':
        RSA.main()

    elif choice=='H':
        hybrid.main()

    else:
        print('invalid choice')