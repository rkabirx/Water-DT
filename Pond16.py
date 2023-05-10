# Working on Vehicle speed line 36 -> goal is to get vehicle speed in data section as per CANBus similarity -> This will just replace numpy line of ABS_process_copy.py -> Next step is to do calculation of slip rate in the same thread and then send pressure in sender socket
# Not able to decide which port number to write in line 119 as this code is stuck at receiving connection from its sender

# Pond main program
import threading
import time
from threading import Thread
import socket
from tkinter import *
import numpy as np


class listener_thread(Thread):

    def __init__(self,conn):
        Thread.__init__(self)
        self.conn = conn

    def run(self):
        global myarray

        BUFFER_SIZE1 = 1024  # Normally 1024, but we want fast response

        print("-----------------------------------------------------------------")
        print('Starting a new connection')

        packet = self.conn.recv(BUFFER_SIZE1)
        waste_info = list(packet)

        # define pond
        import numpy

        i = 4
        pond = numpy.zeros(shape=(i, i))

        areas = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (0, 3),
                 5: (1, 0), 6: (1, 1), 7: (1, 2), 8: (1, 3),
                 9: (2, 0), 10: (2, 1), 11: (2, 2), 12: (2, 3),
                 13: (3, 0), 14: (3, 1), 15: (3, 2), 16: (3, 3)}

        area_numb = waste_info[0]

        arr = waste_info[1:4]
        waste_type = int("".join(map(str, arr)))

        print(waste_info[1:4])

        # assigning values to pond area
        i = waste_info[0]
        if area_numb == i:
            pond[areas[i]] = waste_type
        else:
            print("error")

        print("pond = ",pond)
        np.save('pond.npy', pond)
        np.save('waste_info.npy', waste_info)

        print("-----------------------------------------------------------------")

        # Lets calculate dissipation time (in seconds)
        residence_time = 6
        print("Residence time= ", residence_time)
        depth = 3
        diffusion_coefficient = 1
        mixing_time = depth**2 / diffusion_coefficient
        print("Mixing time= ", mixing_time)

        dissipation_time = residence_time + mixing_time
        print("Dissipation time= ", dissipation_time)

        # Contaminants affecting nearby areas
        time.sleep(dissipation_time)

        target = areas[area_numb]
        # find the adjacent values (including diagonal elements)
        adjacent = []
        for i in range(max(0, target[0] - 1), min(target[0] + 2, 4)):
            for j in range(max(0, target[1] - 1), min(target[1] + 2, 4)):
                if i == target[0] and j == target[1]:
                    continue
                adjacent.append((i, j))

        # get the area numb of adjacent cells
        adjacent_areas = []
        for cell in adjacent:
            adjacent_areas.append(list(areas.keys())[list(areas.values()).index(cell)])

        print("Adjacent cell areas for target", target, ":", adjacent_areas)

        for i in adjacent_areas:
            pond[areas[i]] = waste_type
        else:
            print("error")

        print("pond = ", pond)

        self.conn.close()
        print("Out of receiver for loop")

class sensor_thread(Thread):

    def __init__(self,conn):
        Thread.__init__(self)
        self.conn = conn

    def run(self):
        global myarray

        BUFFER_SIZE1 = 1024  # Normally 1024, but we want fast response

        print("-----------------------------------------------------------------")
        print('Starting a new connection')

        packet = self.conn.recv(BUFFER_SIZE1)
        sense_area = list(packet)
        pond = np.load('pond.npy')
        areas = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (0, 3),
                 5: (1, 0), 6: (1, 1), 7: (1, 2), 8: (1, 3),
                 9: (2, 0), 10: (2, 1), 11: (2, 2), 12: (2, 3),
                 13: (3, 0), 14: (3, 1), 15: (3, 2), 16: (3, 3)}
        final_info =  pond[areas[sense_area]]

        print("final info=", final_info)
        MESSAGE = bytearray([final_info])
        try:
            # Sending to TCS via socket
            TCP_IP = "0.0.0.0"
            TCP_PORT = 5010
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect((TCP_IP,TCP_PORT))
            s.send(MESSAGE)
            print("Sending waste signal: ", final_info)
            data = s.recv(1024)
            s.close()

        except:
            socket.error
            print("Sending information to sensor failed")


def pond_sensor():
    TCP_IP = "0.0.0.0"
    TCP_PORT = 5005

    s2 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s2.bind((TCP_IP,TCP_PORT))
    # log.info('Created a socket')
    print(f"Connecting receiver socket with port {TCP_PORT}")
    s2.listen(1)
    print("Receiver is waiting for a connection...")

    while True:  # Check if this is right -> This is to make receiver from one socket and sender to other socket in 1 loop

        conn,addr = s2.accept()
        conn.setblocking(0)

        thread = sensor_thread(conn)
        thread.start()

def pond_waste():
    TCP_IP = "0.0.0.0"
    TCP_PORT = 5003

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((TCP_IP,TCP_PORT))
    # log.info('Created a socket')
    print(f"Connecting receiver socket with port {TCP_PORT}")
    s.listen(1)
    print("Receiver is waiting for a connection...")

    while True:  # Check if this is right -> This is to make receiver from one socket and sender to other socket in 1 loop

        conn,addr = s.accept()
        conn.setblocking(0)

        thread = listener_thread(conn)
        thread.start()


if __name__ == '__main__':
    threading.Thread(target=pond_waste).start()
    threading.Thread(target=pond_sensor).start()


























