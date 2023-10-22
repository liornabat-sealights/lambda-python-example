import hashlib

def calculate_md5(file_path):
    hasher = hashlib.md5()
    with open(file_path, 'rb') as file:
        while chunk := file.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()

# Specify the file path
file_path = './app.py'

# Calculate and print the MD5 hash of the file
md5_hash = calculate_md5(file_path)
print(f'MD5 hash of the file: {md5_hash}')