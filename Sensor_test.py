
import socket
import threading
from threading import Thread
from tkinter import *

def sensor_send():
    import tkinter

    master = tkinter.Tk()
    master.title("Sensor")
    master.geometry("490x180")

    import time
    import numpy as np

    TCP_IP = "0.0.0.0"  # IP of RPI1
    TCP_PORT = 5005

    BUFFER_SIZE = 1024

    def sensor(x):
        MESSAGE = bytearray([x])
        try:
            # Sending via socket
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

    def area5_ON():
        sensor(5)

    def area6_ON():
        sensor(6)

    def area7_ON():
        sensor(7)

    def area8_ON():
        sensor(8)

    def area9_ON():
        sensor(9)

    def area10_ON():
        sensor(10)

    def area11_ON():
        sensor(11)


    def area12_ON():
        sensor(12)

    def area13_ON():
        sensor(13)

    def area14_ON():
        sensor(14)

    def area15_ON():
        sensor(15)

    def area16_ON():
        sensor(16)

    button1 = tkinter.Button(master, text="Sense area 1", fg="blue", command=area1_ON)
    button1.grid(row=1, column=1)

    button2 = tkinter.Button(master, text="Sense area 2", fg="blue", command=area2_ON)
    button2.grid(row=1, column=2)

    button3 = tkinter.Button(master, text="Sense area 3", fg="blue", command=area3_ON)
    button3.grid(row=1, column=3)

    button4 = tkinter.Button(master, text="Sense area 4", fg="blue", command=area4_ON)
    button4.grid(row=1, column=4)

    button5 = tkinter.Button(master, text="Sense area 5", fg="blue", command=area5_ON)
    button5.grid(row=2, column=1)

    button6 = tkinter.Button(master, text="Sense area 6", fg="blue", command=area6_ON)
    button6.grid(row=2, column=2)

    button7 = tkinter.Button(master, text="Sense area 7", fg="blue", command=area7_ON)
    button7.grid(row=2, column=3)

    button8 = tkinter.Button(master, text="Sense area 8", fg="blue", command=area8_ON)
    button8.grid(row=2, column=4)

    button9 = tkinter.Button(master, text="Sense area 9", fg="blue", command=area9_ON)
    button9.grid(row=3, column=1)

    button10 = tkinter.Button(master, text="Sense area 10", fg="blue", command=area10_ON)
    button10.grid(row=3, column=2)

    button11 = tkinter.Button(master, text="Sense area 11", fg="blue", command=area11_ON)
    button11.grid(row=3, column=3)

    button12 = tkinter.Button(master, text="Sense area 12", fg="blue", command=area12_ON)
    button12.grid(row=3, column=4)

    button13 = tkinter.Button(master, text="Sense area 13", fg="blue", command=area13_ON)
    button13.grid(row=4, column=1)

    button14 = tkinter.Button(master, text="Sense area 14", fg="blue", command=area14_ON)
    button14.grid(row=4, column=2)

    button15 = tkinter.Button(master, text="Sense area 15", fg="blue", command=area15_ON)
    button15.grid(row=4, column=3)

    button16 = tkinter.Button(master, text="Sense area 16", fg="blue", command=area16_ON)
    button16.grid(row=4, column=4)

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
        single_digit = list(packet)
        print("Received message:", single_digit)

        array = [int(char) for char in str(single_digit)]

        if len(array) == 1:
            print("Area is clean")
            output = "Area is clean"
        else:

            wastewater = ""
            chemicals = ""
            organic_waste = ""

            if array[0] == 0:
                wastewater = "No wastewater"
            elif array[0] == 1:
                wastewater = "Light amount of wastewater: abnormal nitrate"
            elif array[0] == 2:
                wastewater = "Medium amount of wastewater: abnormal nitrate"
            elif array[0] == 3:
                wastewater = "Heavy amount of wastewater: abnormal nitrate"

            if array[1] == 0:
                chemicals = "No chemicals"
            elif array[1] == 1:
                chemicals = "Light amount of chemicals: abnormal ph"
            elif array[1] == 2:
                chemicals = "Medium amount of chemicals: abnormal ph"
            elif array[1] == 3:
                chemicals = "Heavy amount of chemicals: abnormal ph"

            if array[2] == 0:
                organic_waste = "No organic waste"
            elif array[2] == 1:
                organic_waste = "Light amount of organic waste: abnormal Turbidity"
            elif array[2] == 2:
                organic_waste = "Medium amount of organic waste: abnormal Turbidity"
            elif array[2] == 3:
                organic_waste = "Heavy amount of organic waste: abnormal Turbidity"

            output = f"{wastewater}\n{chemicals}\n{organic_waste}"
            print(output)

        def print_output():
            # if you want the button to disappear:
            # button.destroy() or button.pack_forget()
            label = Label(root, text=(output))
            label.config(width=84, font=("Courier", 18))
            # this creates x as a new label to the GUI
            label.pack()

        root = Tk()
        # root.after(5000, lambda: root.destroy())
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


    while True:
        conn,addr = s.accept()
        conn.setblocking(0)

        thread = listener_thread(conn)
        thread.start()



if __name__ == '__main__':
    threading.Thread(target=sensor_send).start()
    threading.Thread(target=sensor_recv).start()
