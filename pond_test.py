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

        i = 3
        pond = numpy.zeros(shape=(i, i))

        dict = {tuple([0, 0, 1]): 1, tuple([0, 1, 0]): 2, tuple([0, 1, 1]): 3, tuple([1, 0, 0]): 4, tuple([1, 0, 1]): 5,
                tuple([1, 1, 0]): 6, tuple([1, 1, 1]): 7}

        area_numb = waste_info[0]
        waste_type = tuple(waste_info[1:4])

        print(waste_info[1:4])

        print(tuple(waste_info[1:4]))
        if area_numb == 1: pond[0][0] = dict[waste_type]
        elif area_numb == 2: pond[0][1] = dict[waste_type]
        elif area_numb == 3: pond[0][2] = dict[waste_type]
        elif area_numb == 4: pond[1][0] = dict[waste_type]
        elif area_numb == 6: pond[1][2] = dict[waste_type]
        elif area_numb == 7: pond[2][0] = dict[waste_type]
        elif area_numb == 8: pond[2][1] = dict[waste_type]
        elif area_numb == 9: pond[2][2] = dict[waste_type]
        else:
            print("error")

        print("pond = ",pond)
        np.save('pond.npy', pond)
        np.save('waste_info.npy', waste_info)

        print("-----------------------------------------------------------------")

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

        dict3 = {1: pond[0,0], 2: pond[0,1], 3: pond [0,2], 4: pond[1,0], 6: pond[1,2], 7: pond [2,0], 8: pond[2,1], 9: pond[2,2]}
        final_info = int(dict3[sense_area[0]])
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


























