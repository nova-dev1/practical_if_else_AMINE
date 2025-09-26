cached_firstName = "first_name"
cached_lastName = "last_name"

first_name = input("please entre your First Name: ")
last_name = input("please entre your Last Name: ")

if first_name == cached_firstName and last_name == cached_lastName:
    print(f"welcome, {first_name} {last_name}")
else:
    print("ERROR: Both first name and last name must be provided.")


cachedUsername = "admin"
cachedPassword = "password123"

username = input("Please entre your Username: ")
password = input("Please entre your Password: ")

if username == cachedUsername and password == cachedPassword:
    print("Login Successful")
elif username != cachedUsername and password == cachedPassword:
    print("Error: invalid username! ")
elif username == cachedUsername and password != cachedPassword:
    print("Error: invalid password")
else:
    print("Error: invalid username & password!")
