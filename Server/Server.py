from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

"""VARIABLES"""
clients = []
addresses = []
rooms = []

""" Constants """
HOST = ''
PORT = 33000
BUFSIZE = 1024
ADDRESS = (HOST, PORT)
SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDRESS)


def accept_connection():
    while True:
        client, client_address = SERVER.accept()
        print(f"{client_address} has joined")
        client.send(bytes("Hello fellow traveler!Pls enter your name", "utf8"))
        addresses.append(client_address)
        Thread(target=process_client, args=(client,)).start()


def process_client(client):

    name = client.recv(BUFSIZE).decode("utf8")
    room_number = select_chat_room(client)
    welcome = f"Welcome {name}! if you want to quit type (QUIT)"
    client.send(bytes(welcome, "utf8"))
    msg = f"{name} has joined the chat"
    broadcast(bytes(msg, "utf8"), room_number)

    while True:
        msg = client.recv(BUFSIZE)
        if msg != bytes("(QUIT)", "utf8"):
            broadcast(msg, room_number, f"{name}: ")
        else:
            client.send(bytes("(QUIT)", "utf8"))
            client.close()
            remove_client_from_room(client, room_number)
            broadcast(bytes(f"{name} left the chat", "utf8"), room_number)
            break

def select_chat_room(client):
    client.send(bytes("select chat room", "utf8"))
    room_number = int(client.recv(BUFSIZE).decode("utf8"))
    add_client_to_chat_room(client, room_number)
    return room_number

def add_client_to_chat_room(client, room_number):
    room = get_room(room_number)
    room.append(client)

def remove_client_from_room(client, room_number):
      room = get_room(room_number) 
      room.remove(client)

def get_room(room_number):
    if len(rooms) > room_number:
        return rooms[room_number]
    else:
        return create_room_and_return_it(room_number)

def create_room_and_return_it(room_number):
    while room_number >= len(rooms):
        rooms.append([])
        if len(rooms) == 50:
            break
    return rooms[-1]

def broadcast(msg, room_number, prefix=""):
    for client in rooms[room_number]:
        client.send(bytes(prefix, "utf8") + msg)
            

if __name__ == "__main__":
    SERVER.listen(5)
    print("Server started! Waiting for connections")
    ACCEPT_THREAD = Thread(target=accept_connection())
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()
