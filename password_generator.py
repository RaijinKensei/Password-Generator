import secrets
import string  # fornisce costanti che possiamo definire come alfabeto



class passwordGenerator:
    @staticmethod
    def passGenerator(self, filename):
        letters = string.ascii_letters
        digits = string.digits
        special_chars = string.punctuation
        alphabet = letters + digits + special_chars

        pwd = ''

        print("--- PASSWORD GENERATOR ---")
        print("inserisci lunghezza della password: ")
        pwd_length = int(input())

        for i in range(pwd_length):
            pwd += ''.join(secrets.choice(alphabet))

        print("Password generata: ", pwd)

        with open(filename, "w") as f:
            f.write(f"password: {pwd}")
            print("password salvata su file!")


