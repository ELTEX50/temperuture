from tkinter import *


temp = 20


def temp_check(op):
    global temp
    if op == "+":
        temp += 1
        cooler_result.set(f"{temp} C")
    else:
        temp -= 1
        cooler_result.set(f"{temp} C")
    if temp >= 30:
        cooler_on.set("cooler on")
        cooler_status.config(fg="blue")
    else:
        cooler_on.set("cooler off")
        cooler_status.config(fg="red")
        if temp<=0:
            if temp <= -10:
                cooler_on.set("heater on")
                cooler_status.config(fg="blue")
            else:
                cooler_on.set("heater off")
                cooler_status.config(fg="red")



win = Tk()
win.title("cooler")

up_button = Button(text="↑", width=7, height=2, bg="#EE674A", command=lambda: temp_check("+"), font=" " "40")
up_button.grid(row=1, column=0)

down_button = Button(text="↓", width=7, height=2, bg="#566EF3", command=lambda: temp_check("_"), font=" " "40")
down_button.grid(row=4, column=0)


cooler_result = StringVar()


temperature = Label(textvariable=cooler_result, bg="#E4F5FF",font="" "40")
temperature.grid(row=2, column=0)


cooler_on = StringVar()


cooler_status = Label(textvariable=cooler_on, font="" "60", bg="#E4F5FF", fg="blue")
cooler_status.grid(row=2, column=5, padx=40)


win.config(bg="#E4F5FF")
win.mainloop()
