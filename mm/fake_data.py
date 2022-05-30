#!/usr/bin/env python3

# This Script simulates the sensor in our System
# This is basically the client of our system

# Imports
import json
import random
import time
import socket

# Constants
MAC = 'B8:27:EB:4D:B5:F0'
CHANNEL = 3
MSG_DELAY = 5


# function used to create fake data sets
def create_fake_data():

    info = {
        'breaking': 100,
        'steering': 100,
        'acceleration': 100,
        'speed': 100,
        'overall': 100
    }

    data = json.dumps(info)
    return data

# main function
# connects to open socket
# sends one data set every MSG_DELAY seconds to the server
def main():
    s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
    s.connect((MAC, CHANNEL))
    print('transmitting Data')

    while True:
        s.sendall(bytes(create_fake_data(), 'UTF-8'))
        time.sleep(MSG_DELAY)
  


if __name__ == "__main__":
    main()