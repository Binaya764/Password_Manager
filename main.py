@staticmethod
def view_Mode():
    with open("password.txt",'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            name,passw = data.split("|")
            print("Name:",name + "\t" + "Password:", passw)
@staticmethod
def add_Mode():
    name = input("Enter the account name: ")
    password = input("password: ")

    with open("password.txt",'a') as f:
        f.write(name + "|"+ password + "\n")



master_Password = input("Enter the master Password:" )
mode = input("Select view or add mode(view,add): ")


if(mode == "view"):
    view_Mode()
elif(mode ==  "add"):
    add_Mode()
else:
    print("Invalid mode!")