import hashlib
import pyfiglet

ascii_banner = pyfiglet.figlet_format("SIMPLE HASH CRACKER")
print(ascii_banner)

wordlist_location = str(input('Enter wordlist file location: '))
hash_input = str(input('Enter hash to be cracked: '))
hash_type = str(input('Enter hash type (md5, sha1, sha256, sha512): ')).lower()

hash_functions = {
    'md5': hashlib.md5,
    'sha1': hashlib.sha1,
    'sha256': hashlib.sha256,
    'sha512': hashlib.sha512
}

if hash_type not in hash_functions:
    print('Invalid hash type selected.')
    exit(1)

hash_function = hash_functions[hash_type]

with open(wordlist_location, 'r') as file:
    for line in file.readlines():
        hash_ob = hash_function(line.strip().encode())
        hashed_pass = hash_ob.hexdigest()
        if hashed_pass == hash_input:
            print('Found cleartext password! ' + line.strip())
            exit(0)

print('Password not found in wordlist.')