import time
from tkinter import *
from tkinter import StringVar
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = ttk.Window(themename="darkly")
root.title('Timer')
root.geometry('500x700')
root.resizable(width=False, height=False)


ttk.Label(root, text='Countdown timer', font='arial 30 ', bootstyle='default' ) \
    .place(relx=.5, rely=.1, anchor='center')


def clock():
    clock_time = time.strftime('%H:%M')
    current_time.config(text=clock_time)
    current_time.after(1000, clock)


current_time = ttk.Label(root, font=('arial', 35), text='', bootstyle='default')
current_time.place(relx=.5, rely=.2, anchor=CENTER)

ttk.Label(root, text='current time', font='arial 12', bootstyle='default') \
    .place(relx=.5, rely=.25, anchor='center')
clock()

hr = StringVar()
ttk.Label(root, textvariable=hr, width=2, font='arial 70', bootstyle='default') \
    .place(relx=.20, rely=.4, anchor='center')
hr.set('0')
ttk.Label(root, text='hour', font='arial 12', bootstyle='default')\
    .place(relx=.15, rely=.50, anchor='center')


mins = StringVar()
ttk.Label(root, textvariable=mins, width=2, font='arial 70', bootstyle='default') \
    .place(relx=.50, rely=.4, anchor='center')
mins.set('0')
ttk.Label(root, text='minute', font='arial 12', bootstyle='default') \
    .place(relx=.45, rely=.50, anchor='center')


sec = StringVar()
ttk.Label(root, textvariable=sec, width=2, font='arial 70', bootstyle='default') \
    .place(relx=.80, rely=.4, anchor='center')
sec.set('0')
ttk.Label(root, text='second', font='arial 12', bootstyle='default') \
    .place(relx=.75, rely=.50, anchor='center')

stop_timer = False
def reset_timer():
    global stop_timer
    stop_timer = False
    mins.set("0")
    sec.set("0")
    hr.set("0")
    slider_value.set(1)
    slider_text.config(text='0')

def timer():
    global stop_timer
    stop_timer = True
    slider_text.config(text='0')
    sec.set('0')
    hr.set('0')
    slider_value.set(0)
    times = int(hr.get()) * 3600 + int(mins.get()) * 60 + int(sec.get())
    while times > -1 and stop_timer:
        minute, second = (times // 60, times % 60)
        hour = 0
        if minute > 60:
            hour, minute = (minute // 60, minute % 60)
        convert_sec = str(second)
        convert_min = str(minute)
        convert_hr = str(hour)
        sec.set(convert_sec)
        mins.set(convert_min)
        hr.set(convert_hr)

        root.update()
        time.sleep(1)
        times -= 1

        if times != 0:
            continue
        sec.set('0')
        mins.set('0')
        hr.set('0')
        print('time is up')

    stop_timer = False

def slider_values():
    mins.set(str(slider_value.get()))

def scale(e):
    slider_text.config(text=f'{slider_value.get()}')

slider_value = IntVar()
slider = ttk.Scale(root, from_=0, to=240, orient='horizontal', variable=slider_value, length=200, command=scale)\
    .place(relx=.5, rely=.6, anchor='center')

slider_text = ttk.Label(root, font='arial 12', text='0')
slider_text.place(relx=.5, rely=.65, anchor='center')

start_button = Button(root, text="Start", bg='#2399d9', bd=0, font='arial 14', fg='#000', width=10, 
    command=lambda: [slider_values(), timer()])\
        .place(relx=.35, rely=.75, anchor='center')

stop_button = Button(root, text="Reset", bg='#2399d9', bd=0, font='arial 14', fg='#000', width=10,
    command=reset_timer)\
        .place(relx=.65, rely=.75, anchor='center')

root.mainloop()
