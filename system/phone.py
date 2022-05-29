#!/usr/bin/env python3

# This Script simulates the phone in our System
# This is basically the server of our system

# Imports
import socket
import datetime

# Constants
MAC = 'B8:27:EB:4D:B5:F0'
CHANNEL = 3
BACKLOG = 5
SIZE = 1024

#function to create a timestamp at the moment of function call
def create_time_stamp():
    timestamp = 'Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
    timestamp += ' '
    return timestamp

# main function
# open a socket and listens to establish connection
# decodes and prints the received data
def main():
    s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
    s.bind((MAC, CHANNEL))
    s.listen(BACKLOG)

    try:
        print('Waiting for connection...')
        client, address = s.accept()
        print(f'Successfully connected to {address}')

        while True:
            data = client.recv(SIZE)
            if data:
                print(create_time_stamp() + data.decode('utf-8'))

    finally:
        s.close()


if __name__ == "__main__":
    main()