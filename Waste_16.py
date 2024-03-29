# Updated
from tkinter import Label


def w_i():
    import tkinter

    master = tkinter.Tk()
    master.title("Waste input")
    master.geometry("355x300")
    import socket
    import time
    import numpy as np

    TCP_IP = "0.0.0.0"  # IP of RPI1
    TCP_PORT = 5003

    BUFFER_SIZE = 1024

    def waste_amount_light():
        w_a = [3]
        np.save('w_a.npy', w_a[0])  # save
    def waste_amount_medium():
        w_a = [6]
        np.save('w_a.npy', w_a[0])  # save
    def waste_amount_heavy():
        w_a = [9]
        np.save('w_a.npy', w_a[0])  # save

    def waste1():
        w_a = np.load('w_a.npy')
        waste_type1 = [w_a]
        np.save('waste_type1.npy', waste_type1[0])  # save
        w_type1 = np.load('waste_type1.npy')
        w_type2 = np.load('waste_type2.npy')
        w_type3 = np.load('waste_type3.npy')
        print("Waste values:", w_type1, w_type2, w_type3)

    def waste2():
        w_a = np.load('w_a.npy')
        waste_type2 = [w_a]
        np.save('waste_type2.npy', waste_type2[0])  # save
        w_type1 = np.load('waste_type1.npy')
        w_type2 = np.load('waste_type2.npy')
        w_type3 = np.load('waste_type3.npy')
        print("Waste values:", w_type1, w_type2, w_type3)

    def waste3():
        w_a = np.load('w_a.npy')
        waste_type3 = [w_a]
        np.save('waste_type3.npy', waste_type3[0])  # save
        w_type1 = np.load('waste_type1.npy')
        w_type2 = np.load('waste_type2.npy')
        w_type3 = np.load('waste_type3.npy')
        print("Waste values:", w_type1, w_type2, w_type3)

    def reset():
        waste_type1 = [0]
        np.save('waste_type1.npy', waste_type1[0])  # save
        waste_type2 = [0]
        np.save('waste_type2.npy', waste_type2[0])  # save
        waste_type3 = [0]
        np.save('waste_type3.npy', waste_type3[0])  # save
        print("reset")
        w_type1 = np.load('waste_type1.npy')
        w_type2 = np.load('waste_type2.npy')
        w_type3 = np.load('waste_type3.npy')
        print("reset values:", w_type1, w_type2, w_type3)

    # reset()

    def waste_send(x):
        w_type1 = np.load('waste_type1.npy')
        w_type2 = np.load('waste_type2.npy')
        w_type3 = np.load('waste_type3.npy')
        MESSAGE = bytearray([x, w_type1, w_type2, w_type3])
        try:
            # Sending to TCS via socket
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((TCP_IP, TCP_PORT))
            s.send(MESSAGE)
            print("Sending waste signal: ", list(MESSAGE))
            data = s.recv(BUFFER_SIZE)
            s.close()

        except:
            socket.error
            print("No water around")

    def area1_ON():
        waste_send(1)

    def area2_ON():
        waste_send(2)

    def area3_ON():
        waste_send(3)

    def area4_ON():
        waste_send(4)

    def area5_ON():
        waste_send(5)

    # def area6_ON():
    #     waste_send(6)
    #
    # def area7_ON():
    #     waste_send(7)

    def area8_ON():
        waste_send(8)

    def area9_ON():
        waste_send(9)

    # def area10_ON():
    #     waste_send(10)
    #
    # def area11_ON():
    #     waste_send(11)

    def area12_ON():
        waste_send(12)

    def area13_ON():
        waste_send(13)

    def area14_ON():
        waste_send(14)

    def area15_ON():
        waste_send(15)

    def area16_ON():
        waste_send(16)

    while True:
        Text_Baud = Label(master, text="Please select the waste amount")
        Text_Baud.grid(row=0, column=0, columnspan=3, sticky="we")

        button = tkinter.Button(master, text="Light", fg="black", command=waste_amount_light)
        button.grid(row=1, column=0)

        button = tkinter.Button(master, text="Medium", fg="black", command=waste_amount_medium)
        button.grid(row=1, column=1)

        button = tkinter.Button(master, text="Heavy", fg="black", command=waste_amount_heavy)
        button.grid(row=1, column=2)

        Text_Baud = Label(master, text="Please select the type of wastes")
        Text_Baud.grid(row=2, column=0, columnspan=3, sticky="we")

        button = tkinter.Button(master, text="Wastewater", fg="blue", command=waste1)
        button.grid(row=3, column=0)
        button = tkinter.Button(master, text="Chemicals", fg="blue", command=waste2)
        button.grid(row=3, column=1)
        button = tkinter.Button(master, text="Organic waste", fg="blue", command=waste3)
        button.grid(row=3, column=2)

        button = tkinter.Button(master, text="Reset", fg="red", command=reset)
        button.grid(row=4, column=1)

        Text_Baud = Label(master, text="Inject into selected areas")
        Text_Baud.grid(row=5, column=0, columnspan=3, sticky="we")


        button = tkinter.Button(master, text="Inject area 1", fg="green", command=area1_ON)
        button.grid(row=6, column=0)

        button = tkinter.Button(master, text="Inject area 2", fg="green", command=area2_ON)
        button.grid(row=6, column=1)

        button = tkinter.Button(master, text="Inject area 3", fg="green", command=area3_ON)
        button.grid(row=6, column=2)

        button = tkinter.Button(master, text="Inject area 4", fg="green", command=area4_ON)
        button.grid(row=7, column=0)

        button = tkinter.Button(master, text="Inject area 5", fg="green", command=area5_ON)
        button.grid(row=7, column=1)

        button = tkinter.Button(master, text="Inject area 8", fg="green", command=area8_ON)
        button.grid(row=7, column=2)

        button = tkinter.Button(master, text="Inject area 9", fg="green", command=area9_ON)
        button.grid(row=8, column=0)

        button = tkinter.Button(master, text="Inject area 12", fg="green", command=area12_ON)
        button.grid(row=8, column=1)

        button = tkinter.Button(master, text="Inject area 13", fg="green", command=area13_ON)
        button.grid(row=8, column=2)

        button = tkinter.Button(master, text="Inject area 14", fg="green", command=area14_ON)
        button.grid(row=9, column=0)

        button = tkinter.Button(master, text="Inject area 15", fg="green", command=area15_ON)
        button.grid(row=9, column=1)

        button = tkinter.Button(master, text="Inject area 16", fg="green", command=area16_ON)
        button.grid(row=9, column=2)


        master.mainloop()


if __name__ == '__main__':
    w_i()
