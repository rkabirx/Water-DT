
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
        print("Waste_type: ", waste_type)

        print(waste_info[1:4])

        # assigning values to pond area
        i = waste_info[0]
        if area_numb == i:
            pond[areas[i]] = waste_type
        else:
            print("error")

        print("Pond = \n",pond)

        print("-----------------------------------------------------------------")

        # Lets calculate dissipation time (in seconds)
        # T is the time for the contaminant to reach the target area.
        # D is the distance to the target area (such as from area 1 to areas 2, 5, or 6).
        # V is the average flow velocity (related to the water flow rate).
        # D = 1
        # V = 0.1
        # T = D/V
        # print("Dissipation time= ", T)

        # Contaminants affecting nearby areas
        time.sleep(2)

        target = areas[area_numb]

        # find the adjacent cell area numb (including diagonal elements from the south side)
        adjacent = []
        diagonal_adjacent = []
        non_diagonal_adjacent = []

        for i in range(max(0, target[0] - 1), target[0] + 2):  # Include one row below for diagonals
            for j in range(max(0, target[1]), min(target[1] + 2, 4)):  # Start from target[1] to exclude diagonal left
                if i == target[0] and j == target[1]:
                    continue
                elif i == target[0] + 1 and j == target[1]:  # Exclude direct downward cell
                    continue
                elif abs(target[0] - i) == abs(target[1] - j):
                    diagonal_adjacent.append((i, j))
                else:
                    non_diagonal_adjacent.append((i, j))
                adjacent.append((i, j))

        # get the area numb of adjacent cells

        non_diagonal_adjacent_areas = []
        # get the area numb of adjacent cells
        adjacent_areas1 = []
        for cell in adjacent:
            adjacent_areas1.append(list(areas.keys())[list(areas.values()).index(cell)])

        for cell in non_diagonal_adjacent:
            non_diagonal_adjacent_areas.append(list(areas.keys())[list(areas.values()).index(cell)])

        non_diagonal_adjacent_areas = [i for i in non_diagonal_adjacent_areas if i not in [6, 7, 10, 11]]

        print("Adjacent cell areas1 for target", target, ":", adjacent_areas1)

        print("Non-diagonal adjacent cell areas for target", target, ":", non_diagonal_adjacent_areas)

        # i1 = waste_info[0]
        # if area_numb == i1:
        #     pond[areas[i1]] = (waste_type-(waste_type/3))
        # else:
        #     print("error")

        for i in adjacent_areas1:
            pond[areas[i]] = waste_type/3

        print("1st iteration Pond = \n", pond)
        print("-----------------------------------------------------------------")

        # 2nd time
        # Lets calculate dissipation time (in seconds)
        D = 1
        V = 0.1
        T = D / V
        print("Dissipation time= ", T)

        # Contaminants affecting nearby areas
        time.sleep(2)

        # The new targets are the adjacent areas from the first iteration
        new_targets = adjacent_areas1

        print("new target areas: ", new_targets)

        # For each new target, find its adjacent areas, excluding diagonal left and direct south
        for new_area_numb in new_targets:
            target = areas[new_area_numb]

            adjacent = []
            diagonal_adjacent = []
            non_diagonal_adjacent = []

            for i in range(max(0, target[0] - 1), target[0] + 2):
                for j in range(max(0, target[1]), min(target[1] + 2, 4)):  # Exclude diagonal left
                    if i == target[0] and j == target[1]:
                        continue
                    elif i == target[0] + 1 and j == target[1]:  # Exclude direct downward cell
                        continue
                    elif abs(target[0] - i) == abs(target[1] - j):
                        diagonal_adjacent.append((i, j))
                    else:
                        non_diagonal_adjacent.append((i, j))
                    adjacent.append((i, j))

            # Get the area numbers of all adjacent cells
            adjacent_areas2 = [list(areas.keys())[list(areas.values()).index(cell)] for cell in adjacent]
            print("Adjacent cell areas for target", target, ":", adjacent_areas2)

            # Update the pond with the new waste type for adjacent areas
            i2 = waste_info[0]
            if area_numb == i2:
                pond[areas[i2]] = (waste_type-(waste_type/3))
            else:
                print("error")


            for i in adjacent_areas2:
                pond[areas[i]] = waste_type/3

        print("2nd iteration Pond = \n", pond)

        # 3rd time
        # Lets calculate dissipation time (in seconds) again
        D = 1
        V = 0.1
        T = D / V
        print("Dissipation time for 3rd iteration = ", T)

        # Contaminants affecting nearby areas
        time.sleep(2)

        # The new targets are the adjacent areas from the second iteration
        try:
            new_targets = adjacent_areas2
        except UnboundLocalError:
            pass  # or handle it in some way

        print("3rd iteration new target areas: ", new_targets)

        # For each new target in the 3rd iteration, find its adjacent areas, excluding diagonal left and direct south
        for new_area_numb in new_targets:
            target = areas[new_area_numb]

            adjacent = []
            diagonal_adjacent = []
            non_diagonal_adjacent = []

            for i in range(max(0, target[0] - 1), target[0] + 2):
                for j in range(max(0, target[1]), min(target[1] + 2, 4)):  # Exclude diagonal left
                    if i == target[0] and j == target[1]:
                        continue
                    elif i == target[0] + 1 and j == target[1]:  # Exclude direct downward cell
                        continue
                    elif abs(target[0] - i) == abs(target[1] - j):
                        diagonal_adjacent.append((i, j))
                    else:
                        non_diagonal_adjacent.append((i, j))
                    adjacent.append((i, j))


            # Get the area numbers of all adjacent cells in 3rd iteration
            adjacent_areas3 = [list(areas.keys())[list(areas.values()).index(cell)] for cell in adjacent]
            print("Adjacent cell areas for target in 3rd iteration", target, ":", adjacent_areas3)

            # Update the pond with the new waste type for adjacent areas
            i3 = waste_info[0]
            if area_numb == i3:
                pond[areas[i3]] = waste_type / 3
            else:
                print("error")

            for i in adjacent_areas3:
                pond[areas[i]] = waste_type/3


            for i in adjacent_areas1:
                pond[areas[i]] = (waste_type-(waste_type/3))


        print("3rd iteration Pond = \n", pond)

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

