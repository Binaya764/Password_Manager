from cryptography.fernet import Fernet
""""
@staticmethod
def write_key():
    key = Fernet.generate_key()
    with open("key.key",'wb') as Key_file:
        Key_file.write(key)
key = write_key()
"""
@staticmethod
def load_key():
    file = open("key.key",'rb')
    key = file.read()
    file.close()
    return key
@staticmethod
def view_Mode():
    with open("password.txt",'r') as f:
        for line in f.readlines():
            #rstrip removes the extra line printed by "\n"
            data = line.rstrip()
            #splitting name and password to individual list
            name,passw = data.split("|")
            print("Name:",name + "\t" + "Password:", fer.decrypt(passw.encode()).decode())
@staticmethod
def add_Mode():
    name = input("Enter the account name: ")
    password = input("password: ")

    with open("password.txt",'a') as f:
        f.write(name + "|"+ fer.encrypt(password.encode()).decode()+ "\n")



master_Password = input("Enter the master Password:" )
key= load_key()+ master_Password.encode()
fer = Fernet(key)
mode = input("Select view or add mode(view,add): ")


if(mode == "view"):
    view_Mode()
elif(mode ==  "add"):
    add_Mode()
else:
    print("Invalid mode!")