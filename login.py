from tinydb import TinyDB, Query
import getpass, bcrypt
db = TinyDB("users.json")
print("Login")
username = input("  Username: ")
searchun = Query()
unres = db.search(searchun.Username == username)
if unres == []:
    print("\033[1;31;40m  Account not found. \033[0;37;40m")
    exit()
password = getpass.getpass(prompt="  Password: ").encode("utf-8")
salt = b'$2b$12$rgCYFuE.etnPBnQdd3fiSO'
hashed = bcrypt.hashpw(password, salt).decode("utf-8")
pwres = db.search(searchun.Password == hashed)
if pwres != []:
    print(f"\n\033[1;32;40mLogged in as: {username}\033[0;37;40m")
