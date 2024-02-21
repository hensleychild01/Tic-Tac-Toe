from board import Board
from settings import win

from socket import AF_INET, SOCK_STREAM, socket

HOST, PORT = input("$ Host IP: ").strip(), int(input("$ Server port (5050 by default): ").strip())
server = socket(AF_INET, SOCK_STREAM)
server.bind((HOST, PORT))

