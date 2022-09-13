import sys
import socket



def main():
    args = sys.argv
    if len(args) != 4:
        print("wrong number of arguments")
        sys.exit(1)

    new_socket = socket.socket()
    new_socket.connect((args[1], int(args[2])))
    new_socket.send(args[3].encode())
    message = new_socket.recv(1024).decode()
    print(message)
    new_socket.close()

if __name__ == "__main__":
    main()