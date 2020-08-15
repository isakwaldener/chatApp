from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

"""VARIABLES"""
clients = []
addresses = []

""" Constants """
HOST = ''
PORT = 33000
BUFSIZE = 1024
ADDR = (HOST, PORT)
SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)


def accept_connection():
    while True:
        client, client_address = SERVER.accept()
        print(f"{client_address} has joined")
        client.send(bytes("Hello fellow traveler!Pls enter your name", "utf8"))
        addresses.append(client_address)
        Thread(target=process_client, args=(client,)).start()


def process_client(client):

    name = client.recv(BUFSIZE).decode("utf8")
    welcome = f"Welcome {name}! if you want to quit type (QUIT)"
    client.send(bytes(welcome, "utf8"))
    msg = f"{name} has joined the chat"
    broadcast(bytes(msg, "utf8"))
    clients.append(client)  # maybe need to save name as well

    while True:
        msg = client.recv(BUFSIZE)
        if msg != bytes("(QUIT)", "utf8"):
            broadcast(msg, f"{name}: ")
        else:
            client.send(bytes("(QUIT)", "utf8"))
            client.close()
            clients.remove(client)
            broadcast(bytes(f"{name} left the chat", "utf8"))
            break


def broadcast(msg, prefix=""):
    for client in clients:
        client.send(bytes(prefix, "utf8") + msg)


if __name__ == "__main__":
    SERVER.listen(5)
    print("waiting for connections")
    ACCEPT_THREAD = Thread(target=accept_connection())
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()
