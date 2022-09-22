# Accelerator pedal to apply acceleration
# Sends accelerator pedal position status as binary value

def w_i() :
    import tkinter

    master = tkinter.Tk()
    master.title("Waste input")
    master.geometry("350x275")
    import socket
    import time
    import numpy as np

    TCP_IP = "0.0.0.0"  # IP of RPI1
    TCP_PORT = 5003

    BUFFER_SIZE = 1024

    def waste_OFF():

        MESSAGE = bytearray([0])  # sending 0 to denote TCS OFF
        try:
            # Sending to TCS via socket
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect((TCP_IP,TCP_PORT))
            s.send(MESSAGE)
            print("Sending No waste")
            data = s.recv(BUFFER_SIZE)
            s.close()

        except:
            socket.error
            print("No water around")
    #
    # waste_OFF()

    def area1_ON() :
        MESSAGE = bytearray([1])  # sending 0 to denote TCS OFF
        try:
            # Sending to TCS via socket
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect((TCP_IP,TCP_PORT))
            s.send(MESSAGE)
            print("Sending waste signal")
            data = s.recv(BUFFER_SIZE)
            s.close()

        except:
            socket.error
            print("No water around")

    def area2_ON() :
        MESSAGE = bytearray([2])  # sending 0 to denote TCS OFF
        try:
            # Sending to TCS via socket
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect((TCP_IP,TCP_PORT))
            s.send(MESSAGE)
            print("Sending waste signal")
            data = s.recv(BUFFER_SIZE)
            s.close()

        except:
            socket.error
            print("No water around")

    def area3_ON() :
        MESSAGE = bytearray([3])  # sending 0 to denote TCS OFF
        try:
            # Sending to TCS via socket
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect((TCP_IP,TCP_PORT))
            s.send(MESSAGE)
            print("Sending waste signal")
            data = s.recv(BUFFER_SIZE)
            s.close()

        except:
            socket.error
            print("No water around")

    def area4_ON() :
        MESSAGE = bytearray([4])  # sending 0 to denote TCS OFF
        try:
            # Sending to TCS via socket
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect((TCP_IP,TCP_PORT))
            s.send(MESSAGE)
            print("Sending waste signal")
            data = s.recv(BUFFER_SIZE)
            s.close()

        except:
            socket.error
            print("No water around")

    def area5_ON() :
        MESSAGE = bytearray([5])  # sending 0 to denote TCS OFF
        try:
            # Sending to TCS via socket
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect((TCP_IP,TCP_PORT))
            s.send(MESSAGE)
            print("Sending waste signal")
            data = s.recv(BUFFER_SIZE)
            s.close()

        except:
            socket.error
            print("No water around")

    def area6_ON() :
        MESSAGE = bytearray([6])  # sending 0 to denote TCS OFF
        try:
            # Sending to TCS via socket
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect((TCP_IP,TCP_PORT))
            s.send(MESSAGE)
            print("Sending waste signal")
            data = s.recv(BUFFER_SIZE)
            s.close()

        except:
            socket.error
            print("No water around")

    def area7_ON() :
        MESSAGE = bytearray([7])  # sending 0 to denote TCS OFF
        try:
            # Sending to TCS via socket
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect((TCP_IP,TCP_PORT))
            s.send(MESSAGE)
            print("Sending waste signal")
            data = s.recv(BUFFER_SIZE)
            s.close()

        except:
            socket.error
            print("No water around")

    def area8_ON() :
        MESSAGE = bytearray([8])  # sending 0 to denote TCS OFF
        try:
            # Sending to TCS via socket
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect((TCP_IP,TCP_PORT))
            s.send(MESSAGE)
            print("Sending waste signal")
            data = s.recv(BUFFER_SIZE)
            s.close()

        except:
            socket.error
            print("No water around")


    while True:


        button1 = tkinter.Button(master, text="No waste", fg="red", command=waste_OFF)
        button1.grid(row=1, column=1)

        button2 = tkinter.Button(master, text="Inject area 1", fg="green", command=area1_ON)
        button2.grid(row=1, column=2)

        button3 = tkinter.Button(master, text="Inject area 2", fg="green", command=area2_ON)
        button3.grid(row=1, column=3)

        button4 = tkinter.Button(master, text="Inject area 3", fg="green", command=area3_ON)
        button4.grid(row=2, column=1)

        button5 = tkinter.Button(master, text="Inject area 4", fg="green", command=area4_ON)
        button5.grid(row=2, column=2)

        button6 = tkinter.Button(master, text="Inject area 5", fg="green", command=area5_ON)
        button6.grid(row=2, column=3)

        button7 = tkinter.Button(master, text="Inject area 6", fg="green", command=area6_ON)
        button7.grid(row=3, column=1)

        button8 = tkinter.Button(master, text="Inject area 7", fg="green", command=area7_ON)
        button8.grid(row=3, column=2)

        button9 = tkinter.Button(master, text="Inject area 8", fg="green", command=area8_ON)
        button9.grid(row=3, column=3)


        master.mainloop()


if __name__ == '__main__' :
    w_i()
