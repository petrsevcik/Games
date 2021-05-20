import hashlib
import json


# part 1
def find_password_from_file(file, hash):
    """Taking file path and md5 hash, returning the decrypted word if in the file """
    with open(file, "r") as passwd_file:
        for password in passwd_file.readlines():
            password = password.strip()
            passwd_hash = hashlib.md5(password.encode())
            if passwd_hash.hexdigest() == hash:
                return password
        return "password not found"


# test part 1 - print(find_password_from_file("sample-words.txt", "de5949721e6352f01dfef317c3e898a8"))

class Decrypter():
    """Class responsible for decoding all of the various entries"""

    def __init__(self, file):
        self.file = file
        self.passwords = {}
        self.decrypted_database = []

    def load_words(self):
        with open(self.file, "r") as passwd_file:
            for password in passwd_file.readlines():
                password = password.strip()
                passwd_hash = hashlib.md5(password.encode())
                self.passwords[password] = passwd_hash.hexdigest()
            return self.passwords

    def decrypt_hash(self, hash):
        for password in self.passwords.keys():
            if self.passwords[password] == hash:
                return password
        return "password not found"

    def decrypt_db(self, json_file):
        with open(json_file, "r") as f:
            json_data = json.load(f)
        for user in json_data:
            if user["password"] in self.passwords.values():
                password = self.decrypt_hash(user["password"])
                credentials = user["username"], password
                self.decrypted_database.append(credentials)
        return self.decrypted_database


# TEST part 2
# test = Decrypter("sample-words.txt")
# print(test.load_words())
# print(test.decrypt_hash('de5949721e6352f01dfef317c3e898a7'))
# print(test.decrypt_db("db.json"))

def terminal():
    """Interface for loading words and decrypting hashes"""
    print("Hello hacker!")
    start = True
    while start:
        print("""Please choose from following options: 
    1: 'help'
    2: 'input new words'
    3: 'add words'
    4: 'decrypt hash'
    5: 'q' 'quit'
    """)
        choice = input("Type here number or option:")
        if choice in ["1", "help"]:
            print("Choose option by typing number or option or type q for quit")

        if choice in ["2", "input new words"]:
            file = input("Please name the file: ")
            words = input("Insert words separated by space: ")
            list_of_words = words.split(" ")
            with open(file, "w") as f:
                for word in list_of_words:
                    f.write(f"{word}\n")
                    print(f"file {file} was created")
                    return

        if choice in ["3", "add words"]:
            file = input("Name of the file: ")
            words = input("Insert new words separated by space: ")
            list_of_words = words.split(" ")
            with open(file, "w") as f:
                for word in list_of_words:
                    f.write(f"{word}\n")
                print("words added")
                return

        if choice in ["4", "decrypt hash"]:
            hash_input = input("Inset MD5-hash: ")
            db = Decrypter("sample-words.txt")  # HERE YOU NEED TO PUT YOUR FILE OR ADJUST TO USER FILE
            db.load_words()
            if db.decrypt_hash(hash_input):
                print(f"The password is {db.decrypt_hash(hash_input)}")
                return

        if choice in ["5", "q", "quit"]:
            print("Bye, bye!")
            return

        else:
            print("Invalid input! Please try again, press h for help or quit")

if __name__ == "__main__":
    terminal()
