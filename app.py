from tkinter import *


def OpenServer():
    print("Server is listening...")


# Show main window
window = Tk()
window.title("Tkinter GUI Example")
window.geometry("300x150")  # Change the window size: width and heigth

# Insert a label
ipLabel = Label(window, text="IP:").grid(row=0, column=0, padx=50, pady=20)
ipGet = StringVar()
ipEntry = Entry(window, textvariable=ipGet).grid(row=0, column=1)

portLabel = Label(window, text="Port").grid(row=1, column=0)
portGet = StringVar()
portEntry = Entry(window, textvariable=portGet).grid(row=1, column=1)

btnConnect = Button(window, text="Connect", command=OpenServer).grid(
    row=2, column=1, pady=10)


window.mainloop()
