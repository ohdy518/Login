from tinydb import TinyDB
import getpass, bcrypt
db = TinyDB("users.json")

print("Signup")
username = input("  Username: ")
email = input("  Email: ")
password = getpass.getpass(prompt="  Password: ").encode("utf-8")
confirmpassword = getpass.getpass(prompt="  Confirm password: ").encode("utf-8")
if password != confirmpassword:
    print("Password does not match. ")
    exit()

salt = b'$2b$12$rgCYFuE.etnPBnQdd3fiSO'
hashed = bcrypt.hashpw(password, salt)

db.insert({"Username": username, "Email": email, "Password": hashed.decode("utf-8")})
print("Signup successful")