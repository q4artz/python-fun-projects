import password
import random

# Declears a User class
class User():
    # Declear password variable to the Password Function with 2 arguement
    password = password.Password(method='md5',hash_encoding='base64')

# Declear a user name John to the class and assign the password
John=User()
John.password= 'JoebidenPassword123'

print("\n");
print("John's password hash is > "+ John.hash)


def ReadFile(FileName):
    File = open(FileName,'r')
    print("\n");
    print("[+] Comparing Each Password...");
    
    # Variable To count the attempts tried
    INTcount = 0

    # Grabs EachLine Inside the File
    for EachLine in File:
        INTcount = INTcount + 1

        # Strips the Whitespaces to prevent error
        EachLine = EachLine.rstrip();

        # Comparing the Password to EachLine of the txt file
        if(John.password == EachLine):
            print("\n");
            print("[+] Found Matched Password");
            print("The Password is > " +EachLine);
            print("\n");
        else:
            continue

    # Concatnate the int variable to string
    print(str(INTcount)+ " Attempt Tried");
    print("[-] Exiting Program...")
    print("\n");

FileName = "rockme.txt"
ReadFile(FileName)