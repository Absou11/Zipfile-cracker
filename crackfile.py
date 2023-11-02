import zipfile

def extract_zip(password_list,zip_file):
    with open(password_list) as f :
        for password in f :
            password = password
            try:
                zip_file.extractall(pwd=bytes (password, 'utf-8'))
                print("password found",password)
                return True
            except:
                continue
    return False

zip_file = input("enter the zip file you to crack: ")
password_list = input("privide the list of passwords: ")

with zipfile.ZipFile(zip_file) as zf:
    if not extract_zip(password_list,zf):
        print("password not found in the list ")

