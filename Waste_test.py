# Accelerator pedal to apply acceleration
# Sends accelerator pedal position status as binary value

def w_i():
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
        waste_type1 = [1]
        np.save('waste_type1.npy', waste_type1[0])  # save
        w_type1 = np.load('waste_type1.npy')
        w_type2 = np.load('waste_type2.npy')
        w_type3 = np.load('waste_type3.npy')
        print("Waste values:", w_type1, w_type2, w_type3)

    def waste2():
        waste_type2 = [1]
        np.save('waste_type2.npy', waste_type2[0])  # save
        w_type1 = np.load('waste_type1.npy')
        w_type2 = np.load('waste_type2.npy')
        w_type3 = np.load('waste_type3.npy')
        print("Waste values:", w_type1, w_type2, w_type3)

    def waste3():
        waste_type3 = [1]
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

    def area6_ON():
        waste_send(6)

    def area7_ON():
        waste_send(7)

    def area8_ON():
        waste_send(8)

    def area9_ON():
        waste_send(9)

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

        button = tkinter.Button(master, text="Inject area 6", fg="green", command=area6_ON)
        button.grid(row=2, column=3)

        button = tkinter.Button(master, text="Inject area 7", fg="green", command=area7_ON)
        button.grid(row=3, column=1)

        button = tkinter.Button(master, text="Inject area 8", fg="green", command=area8_ON)
        button.grid(row=3, column=2)

        button = tkinter.Button(master, text="Inject area 9", fg="green", command=area9_ON)
        button.grid(row=3, column=3)

        master.mainloop()


if __name__ == '__main__':
    w_i()
