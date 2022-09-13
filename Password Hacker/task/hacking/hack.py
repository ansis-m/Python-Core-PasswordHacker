import copy
import sys
import socket
import itertools
import string
import os

def next_password(file):

    passwords = (line for line in file.read().splitlines())

    for password in passwords:
        for i in range(2**len(password)):
            temp = list(copy.deepcopy(password))

            # print(temp)
            yield temp



def main():

    file = open("C:\\Users\\Ansis\\Desktop\\ChemScraper\\Password Hacker\\Password Hacker\\task\\hacking\\passwords.txt", "r")
    args = sys.argv
    if len(args) != 3:
        print("wrong number of arguments")
        sys.exit(1)

    new_socket = socket.socket()
    new_socket.connect((args[1], int(args[2])))


    iter = next_password(file)

    while True:
        password = "".join(next(iter))
        print(password)
        new_socket.send(password.encode())
        message = new_socket.recv(1024)
        if message.decode() == "Connection success!":
            print(password)
            break
        if message.decode() == "Too many attempts":
            print(message.decode())
            break

    file.close()
    new_socket.close()

if __name__ == "__main__":
    main()