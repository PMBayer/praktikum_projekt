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


# create data set, that is meant to immitate the real driving data, 
# but for convinience sake we are using randomized values
# returns set of values in JSON format
def create_data_set():
    breaking = create_rnd_value()
    steering = create_rnd_value()
    acceleration = create_rnd_value()
    speed = create_rnd_value()

    factors = [breaking, steering, acceleration, speed]
    factors.sort()
    smallest_value = factors[:1]  # list is sorted asc; so first value is lowest
    overall = smallest_value[0]

    info = {
        'breaking': breaking,
        'steering': steering,
        'acceleration': acceleration,
        'speed': speed,
        'overall': overall
    }

    data = json.dumps(info)

    return data


# function to generate a pseudo-random value for filling drive data
def create_rnd_value():
    return random.randrange(1, 101)


# main function
# connects to open socket
# sends one data set every MSG_DELAY seconds to the server
def main():
    s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
    s.connect((MAC, CHANNEL))
    print('transmitting Data')

    while True:
        s.sendall(bytes(create_data_set(), 'UTF-8'))
        time.sleep(MSG_DELAY)
  


if __name__ == "__main__":
    main()