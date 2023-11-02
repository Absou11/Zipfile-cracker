# Zip File Password Cracker

## Overview

This Python script is a basic tool for attempting to crack a password-protected ZIP file using a list of potential passwords. It reads passwords from a file and tries each password until it successfully extracts the ZIP file or exhausts the list of passwords.

## How It Works

The script works as follows:

1. It prompts the user to enter the path to the ZIP file they want to crack.
2. It prompts the user to provide the path to a text file containing a list of potential passwords.
3. It then attempts to extract the ZIP file using each password in the list.
4. If a correct password is found, it prints "password found" with the successful password and exits.
5. If none of the passwords in the list work, it prints "password not found in the list."

Please note that this is a basic password cracking tool and may not be efficient for strong or complex passwords. Additionally, it's essential to use this code responsibly and only on files and systems for which you have permission.

## How to Run

To use this script, follow these steps:

1. Clone or download this repository to your local machine.
2. Make sure you have Python 3 installed on your system.
3. Open a terminal or command prompt.
4. Navigate to the directory where you've saved the script and the password list.
5. Run the script by executing the following command:

   ```bash
   python zip_password_cracker.py
