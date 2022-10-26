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

    def waste1():
        waste_type1 = bytearray([1])
        np.save('waste_type.npy', waste_type1[0])  # save

    def waste2():
        waste_type2 = bytearray([2])
        np.save('waste_type.npy', waste_type2[0])  # save

    def waste3():
        waste_type3 = bytearray([3])
        np.save('waste_type.npy', waste_type3[0])  # save

    def reset():
        waste_type1 = bytearray([0])
        np.save('waste_type1.npy', waste_type1[0])  # save
        waste_type2 = bytearray([0])
        np.save('waste_type2.npy', waste_type2[0])  # save
        waste_type3 = bytearray([0])
        np.save('waste_type3.npy', waste_type3[0])  # save
        print("reset")

    reset()
    w_type1 = np.load('waste_type1.npy')
    w_type2 = np.load('waste_type2.npy')
    w_type3 = np.load('waste_type3.npy')

    def area1_ON() :

        MESSAGE = bytearray([1, w_type1, w_type2, w_type3])
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
        w_type = np.load('waste_type.npy')
        MESSAGE = bytearray([2, w_type1, w_type2, w_type3])
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
        w_type = np.load('waste_type.npy')
        MESSAGE = bytearray([3, w_type1, w_type2, w_type3])
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
        w_type = np.load('waste_type.npy')
        MESSAGE = bytearray([4, w_type1, w_type2, w_type3])
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
        w_type = np.load('waste_type.npy')
        MESSAGE = bytearray([5, w_type1, w_type2, w_type3])
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
        w_type = np.load('waste_type.npy')
        MESSAGE = bytearray([6, w_type1, w_type2, w_type3])
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
        w_type = np.load('waste_type.npy')
        MESSAGE = bytearray([7, w_type1, w_type2, w_type3])
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
        w_type = np.load('waste_type.npy')
        MESSAGE = bytearray([8, w_type1, w_type2, w_type3])  # sending 0 to denote TCS OFF
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
        button = tkinter.Button(master, text="Wastewater", fg="blue", command=waste1)
        button.grid(row=0, column=1)
        button = tkinter.Button(master, text="Chemicals", fg="blue", command=waste2)
        button.grid(row=0, column=2)
        button = tkinter.Button(master, text="Organic waste", fg="blue", command=waste3)
        button.grid(row=0, column=3)

        button = tkinter.Button(master, text="Reset", fg="red", command=reset)
        button.grid(row=1, column=1)

        button = tkinter.Button(master, text="Inject area 1", fg="green", command=area1_ON)
        button.grid(row=1, column=2)

        button = tkinter.Button(master, text="Inject area 2", fg="green", command=area2_ON)
        button.grid(row=1, column=3)

        button = tkinter.Button(master, text="Inject area 3", fg="green", command=area3_ON)
        button.grid(row=2, column=1)

        button = tkinter.Button(master, text="Inject area 4", fg="green", command=area4_ON)
        button.grid(row=2, column=2)

        button = tkinter.Button(master, text="Inject area 5", fg="green", command=area5_ON)
        button.grid(row=2, column=3)

        button = tkinter.Button(master, text="Inject area 6", fg="green", command=area6_ON)
        button.grid(row=3, column=1)

        button = tkinter.Button(master, text="Inject area 7", fg="green", command=area7_ON)
        button.grid(row=3, column=2)

        button = tkinter.Button(master, text="Inject area 8", fg="green", command=area8_ON)
        button.grid(row=3, column=3)


        master.mainloop()


if __name__ == '__main__' :
    w_i()
