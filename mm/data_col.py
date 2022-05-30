#!/usr/bin/env python3

# This is the Script used by the attacker to steal data sets and view them
# simmulates the phone/server on the attackers device

# Imports
import socket
import datetime
import time

# Constants 
MAC = ''
BACKLOG = 5
SIZE = 2048
CHANNEL = 3

#function to create a timestamp at the moment of function call
def create_time_stamp():
    timestamp = 'Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())


def establish_connection():
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
    

# because we do not know which channel is used for the connection, we are brute forcing our way in
# function which tries connection until it manages to establish a connection to the client
# for the time being this function is not used; but theoretically works
def trying_possible_connections():
    s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM. socket.BTPROTO_RFCOMM)
    for i in range(600):
        s.bind((MAC, i+1)) # 1 is a placeholder until a method is established to get the port which is used for the connection
        s.listen(BACKLOG)
        time.sleep(5)
        
        if s.accept():
            CHANNEL = i+1
            break
        else:
            s.close()


def main():
    print('Data Collector')
    establish_connection()

if __name__ == "__main__":
    main()  