import secrets
import string 



class passwordGenerator:
    @staticmethod
    def passGenerator(self, filename):
        letters = string.ascii_letters
        digits = string.digits
        special_chars = string.punctuation
        alphabet = letters + digits + special_chars

        pwd = ''

        print("--- PASSWORD GENERATOR ---")
        print("Insert password length: ")
        pwd_length = int(input())

        for i in range(pwd_length):
            pwd += ''.join(secrets.choice(alphabet))

        print("Password generated: ", pwd)

        with open(filename, "w") as f:
            f.write(f"password: {pwd}")
            print("password saved on file!")


