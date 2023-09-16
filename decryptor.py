#!/usr/bin/env python3

from cryptography.fernet import Fernet

class FileDecryptor:
    """
    DISCLAIMER: This code is provided for research and detection purposes only.
    It is intended to be used responsibly and legally to protect computer systems,
    data, and networks from potential threats. Any misuse of this code for malicious
    purposes is strictly prohibited and may be subject to legal consequences.
    """

    def __init__(self, secret_key_file="thekey.key", secret_phrase="McDonalds"):
        self.secret_key_file = secret_key_file
        self.secret_phrase = secret_phrase
        self.secret_key = None

    def load_secret_key(self):
        try:
            with open(self.secret_key_file, "rb") as key_file:
                self.secret_key = key_file.read()
        except FileNotFoundError:
            print(f"Secret key file '{self.secret_key_file}' not found. Make sure to provide the correct file name.")

    def decrypt_files(self, files):
        if self.secret_key:
            user_phrase = input("Enter the secret phrase to decrypt your files: ")
            if user_phrase == self.secret_phrase:
                for file in files:
                    with open(file, "rb") as thefile:
                        contents = thefile.read()
                    contents_decrypted = Fernet(self.secret_key).decrypt(contents)
                    with open(file, "wb") as thefile:
                        thefile.write(contents_decrypted)
                    print("Congratulations, your files are decrypted. Enjoy your coffee.")
            else:
                print("Sorry, wrong secret phrase. Now I want a happy meal toy.")
        else:
            print("No secret key available. Make sure to load the secret key first.")

    def run(self):
        files = self.find_eligible_files()
        if not files:
            print("No eligible files found.")
            return

        print("Eligible files:", files)

        self.load_secret_key()
        self.decrypt_files(files)

    @staticmethod
    def find_eligible_files():
        eligible_files = []
        for file in os.listdir():
            if file not in ["foodie.py", "thekey.key", "decrypt.py"] and os.path.isfile(file):
                eligible_files.append(file)
        return eligible_files

if __name__ == "__main__":
    decryptor = FileDecryptor()
    decryptor.run()
