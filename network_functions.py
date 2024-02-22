from socket import socket

def send_move(server: socket, r: int, c: int, player: int) -> None: 
    msg = f"{r}, {c}, {player}"
    server.send(msg.encode("ascii"))

def receive_move(server: socket) -> tuple:
    msg = server.recv(1024)
    msg = msg.split(", ")
    coords: tuple = int(msg[0]), int(msg[1])
    player = int(msg[2])
    return coords, player