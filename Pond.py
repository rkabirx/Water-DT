# Working on Vehicle speed line 36 -> goal is to get vehicle speed in data section as per CANBus similarity -> This will just replace numpy line of ABS_process_copy.py -> Next step is to do calculation of slip rate in the same thread and then send pressure in sender socket
# Not able to decide which port number to write in line 119 as this code is stuck at receiving connection from its sender

# Pond main program
import threading
import time
from threading import Thread
import socket
from tkinter import *
import numpy as np

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
        datalist = list(packet)


        if datalist[0] == 1:

            x = np.load('pond.npy')
            if all(v == 0 for v in x):
                print("Water is clean")
            elif x[0] == 1:
                print("Water is contaminated")
            else:
                print("Error")
            print("-----------------------------------------------------")

        elif datalist[0] == 2:

            x = np.load('pond.npy')
            if all(v == 0 for v in x):
                print("Water is clean")
            elif x[1] == 1:
                print("Water is contaminated")
            else:
                print("Error")
            print("-----------------------------------------------------")

        else:
            print("Error")
        print("-----------------------------------------------------------------")

        self.conn.close()
        print("Out of receiver for loop")

# sender socket starts
        print("Inside sender function")
        TCP_IP = "0.0.0.0"

        TCP_PORT = 5010  # To connect to Hydraulic_modulator.py  # Port of HCU
        payload = bytearray(x)

        BUFFER_SIZE = 1024
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TCP_IP, TCP_PORT))
        s.send(payload)
        data1 = s.recv(BUFFER_SIZE)
        s.close()
        time.sleep(2)

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
        datalist = list(packet)


        if datalist[0] == 0:
            pH = 6.5
            turbidity = 0.3
            nitrate = 50
            print("pH :", pH)
            print("Turbidity :", turbidity)
            print("Nitrate: ", nitrate)
            print("Water is clean")
            np.save('pond.npy', [0,0,0,0,0,0,0,0,0])
        elif datalist[0] == 1:
            pH = 9
            turbidity = 0.4
            nitrate = 60
            print("pH :", pH)
            print("Turbidity :", turbidity)
            print("Nitrate: ", nitrate)
            print("Area 1 is contaminated")
            time.sleep(5)
            print("Area 2 and 4 are contaminated")

            def print_output():
                # if you want the button to disappear:
                # button.destroy() or button.pack_forget()
                label = Label(root, text=("Area 1, 2 and 4 are contaminated"))
                label.config(width=32, font=("Courier", 16))
                # this creates x as a new label to the GUI
                label.pack()

            root = Tk()
            root.after(15000, lambda: root.destroy())
            button = Button(root, command=print_output)
            button.pack()

            print_output()
            root.mainloop()
            np.save('pond.npy', [1,1,0,1,0,0,0,0,0])
        elif datalist[0] == 2:
            pH = 9
            turbidity = 0.4
            nitrate = 60
            print("pH :", pH)
            print("Turbidity :", turbidity)
            print("Nitrate: ", nitrate)
            print("Area 2 is contaminated")
            time.sleep(5)
            print("Area 1, 3 and 5 are contaminated")
            np.save('pond.npy', [1,0,1,0,1,0,0,0,0])

        else:
            print("Error")
        print("-----------------------------------------------------------------")

        self.conn.close()
        print("Out of receiver for loop")



def pond_sensor():
    TCP_IP = "0.0.0.0"
    TCP_PORT = 5005

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((TCP_IP,TCP_PORT))
    # log.info('Created a socket')
    print(f"Connecting receiver socket with port {TCP_PORT}")
    s.listen(1)
    print("Receiver is waiting for a connection...")

    while True:  # Check if this is right -> This is to make receiver from one socket and sender to other socket in 1 loop

        conn,addr = s.accept()
        conn.setblocking(0)

        thread = sensor_thread(conn)
        thread.start()

def pond_waste():
    TCP_IP = "0.0.0.0"
    TCP_PORT = 5003

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
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


























