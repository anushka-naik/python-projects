from cryptography.fernet import Fernet


def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


write_key()


# password+key+text= encrypted text
# encrypted text+password+key= original text

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


masterpwd = input("what is the master password?")
key = load_key() + masterpwd.encode() # the key is stored in bytes so we use the encode func to convert the
fer = Fernet(key)                     # masterpwd which is in str to bytes
                                      # so they both can be added wo err

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:",
                  fer.decrypt(passw.encode()).decode())
    write_key()


def add():
    name = input('Account Name: ')
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input(
        "Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue

'''here we use cryptography fernet to make a key to encrypt and decrypt - write_key() creates a key.key
 file of random letters. write key()-creates key and load key- stores adn reads key. 
 fer=fernet(key)- init for module
 fer.encrypt(password.encode()) password input is in str so we convert to byte and then encrypt it
 '''
