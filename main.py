# Devin Fledermaus
# Temperature Converter

from tkinter import *

# root window
root = Tk()
root.geometry("1000x700")
root.resizable(False, False)
root.title("Temperature Converter")
convert = "none"


# Defining the functions
# activation of celsius
def act_e1():
    if e1['state'] == "normal":
        e1.config(state="disabled")
        e2.delete(0, END)
    else:
        e1.config(state="normal")
        e2.config(state="disabled")

        global convert
        convert = "CtF"

# activation of fahrenheit
def act_e2():
    if e2['state'] == "normal":
        e2.config(state="disabled")
        e1.delete(0, END)
    else:
        e2.config(state="normal")
        e1.config(state="disabled")

        global convert
        convert = "FtC"


# calculation of conversion
def calculating():
    global convert
    if convert == "CtF":
        temp = float(e1.get())
        answer = str(temp * 9 / 5 + 32)
        e3.config(state="normal")
        e3.delete(0, END)
        e3.insert(0, answer)
        e3.config(state="readonly")
    elif convert == "FtC":
        temp = float(e2.get())
        answer = str((temp - 32) * 5 / 9)
        e3.config(state="normal")
        e3.delete(0, END)
        e3.insert(0, answer)
        e3.config(state="readonly")
    else:
        answer = "Convert Correctly"
        e3.config(state="normal")
        e3.delete(0, END)
        e3.insert(0, answer)
        e3.config(state="readonly")


def clearing():
    e3.delete(0, END)
    e1.delete(0, END)
    e2.delete(0, END)


def terminating():
    import sys
    sys.exit()


# Label Frames
lb1 = LabelFrame(root, text="Celsius to Fahrenheit")
lb2 = LabelFrame(root, text="Fahrenheit to Celsius")

# LabelFrame place
lb1.place(x=150, y=50, width=300, height=150)
lb2.place(x=500, y=50, width=300, height=150)


# Entry
e1 = Entry(lb1, width=30, state="readonly")
e2 = Entry(lb2, width=30, state="readonly")
e3 = Entry(root, width=20, bg="blue", state="readonly")


# Entry packs
e1.pack(side=BOTTOM)
e2.pack(side=BOTTOM)
e3.place(x=400, y=350)


# Buttons
b1 = Button(root, text="Activate - Celsius to Fahrenheit", command=act_e1)
b2 = Button(root, text="Activate - Fahrenheit to Celsius", command=act_e2)
b3 = Button(root, text="Calculate Conversion", command=calculating)
b4 = Button(root, text="Clear", command=clearing)
b5 = Button(root, text="Exit Program", command=terminating)


# Button packs
b1.place(x=180, y=210)
b2.place(x=530, y=210)
b3.place(x=200, y=350)
b4.place(x=600, y=350)
b5.place(x=600, y=400)


# run program
root.mainloop()


