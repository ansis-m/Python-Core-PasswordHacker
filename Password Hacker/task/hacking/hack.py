import copy
import sys
import socket
import itertools
import string
import os
import json

def next_password(file):

    passwords = (line for line in file.read().splitlines())
    for password in passwords:
        for combo in set(map(''.join, itertools.product(*zip(password.upper(), password.lower())))):
            yield combo

def next_login(file):

    logins = (line for line in file.read().splitlines())
    for login in logins:
        for combo in set(map(''.join, itertools.product(*zip(login.upper(), login.lower())))):
            yield combo

def get_login(file, new_socket):

    iter = next_login(file)
    login = "".join(next(iter))

    while True:
        dictionary = {"login" : login, "password" : " "}
        json_str = json.dumps(dictionary)

        new_socket.send(json_str.encode())
        message = new_socket.recv(1024).decode()
        if json.loads(message)["result"] != "Wrong login!":
            print(json.loads(message)["result"])
            return login
        else:
            login = "".join(next(iter))


def main():

    file = open("C:\\Users\\Ansis\\Desktop\\ChemScraper\\Password Hacker\\Password Hacker\\task\\hacking\\logins.txt", "r")
    args = sys.argv
    if len(args) != 3:
        print("wrong number of arguments")
        sys.exit(1)

    new_socket = socket.socket()
    new_socket.connect((args[1], int(args[2])))
    login = get_login(file, new_socket)
    print("login:", login)






    file.close()
    new_socket.close()
    sys.exit(1)

if __name__ == "__main__":
    main()