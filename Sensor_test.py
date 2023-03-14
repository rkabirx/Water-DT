# Accelerator pedal to apply acceleration
# Sends accelerator pedal position status as binary value
import socket
import threading
from threading import Thread
from tkinter import *

def sensor_send():
    import tkinter

    master = tkinter.Tk()
    master.title("Sensor")
    master.geometry("350x275")

    import time
    import numpy as np

    TCP_IP = "0.0.0.0"  # IP of RPI1
    TCP_PORT = 5005

    BUFFER_SIZE = 1024

    def sensor(x):
        MESSAGE = bytearray([x])
        try:
            # Sending to TCS via socket
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((TCP_IP, TCP_PORT))
            s.send(MESSAGE)
            print("Sensing from pond")
            data = s.recv(BUFFER_SIZE)
            s.close()

        except:
            socket.error
            print("No water around")

    def area1_ON():
        sensor(1)

    def area2_ON():
        sensor(2)

    def area3_ON():
        sensor(3)

    def area4_ON():
        sensor(4)

    def area6_ON():
        sensor(6)

    def area7_ON():
        sensor(7)

    def area8_ON():
        sensor(8)

    def area9_ON():
        sensor(9)

    while True:
        button1 = tkinter.Button(master, text="")
        button1.grid(row=1, column=1)

        button2 = tkinter.Button(master, text="Sense area 1", fg="blue", command=area1_ON)
        button2.grid(row=1, column=2)

        button3 = tkinter.Button(master, text="Sense area 2", fg="blue", command=area2_ON)
        button3.grid(row=1, column=3)

        button4 = tkinter.Button(master, text="Sense area 3", fg="blue", command=area3_ON)
        button4.grid(row=2, column=1)

        button5 = tkinter.Button(master, text="Sense area 4", fg="blue", command=area4_ON)
        button5.grid(row=2, column=2)

        button6 = tkinter.Button(master, text="Sense area 6", fg="blue", command=area6_ON)
        button6.grid(row=2, column=3)

        button7 = tkinter.Button(master, text="Sense area 7", fg="blue", command=area7_ON)
        button7.grid(row=3, column=1)

        button8 = tkinter.Button(master, text="Sense area 8", fg="blue", command=area8_ON)
        button8.grid(row=3, column=2)

        button9 = tkinter.Button(master, text="Sense area 9", fg="blue", command=area9_ON)
        button9.grid(row=3, column=3)

        master.mainloop()


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
        final_info = list(packet)
        print("Received message:",final_info)

        dict2 = {0: 'Area is clean',
                 1: 'Organic waste: abnormal Turbidity',
                 2: 'Chemical waste: abnormal ph',
                 3: 'Organic and Chemical waste: abnormal Turbidity and ph',
                 4: 'Wastewater: abnormal nitrate',
                 5: 'Wastewater and Organic waste: abnormal Nitrate and Turbidity',
                 6: 'Wastewater and Chemical waste: abnormal nitrate and ph',
                 7: 'Wastewater, Chemical and Organic waste: abnormal nitrate, ph and Turbidity'}


        output = dict2[final_info[0]]


        def print_output():
            # if you want the button to disappear:
            # button.destroy() or button.pack_forget()
            label = Label(root, text=(output))
            label.config(width=74, font=("Courier", 16))
            # this creates x as a new label to the GUI
            label.pack()

        root = Tk()
        root.after(15000, lambda: root.destroy())
        button = Button(root, command=print_output)
        button.pack()

        print_output()
        root.mainloop()

        self.conn.close()
        print("Out of receiver for loop")


def sensor_recv():
    TCP_IP = "0.0.0.0"
    TCP_PORT = 5010

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
    threading.Thread(target=sensor_send).start()
    threading.Thread(target=sensor_recv).start()
