import tkinter as tk
import time

root = tk.Tk()
clock = tk.Label(root, font=("Arial",20,"bold"), bg="pink")
clock.pack(expand=1)

def tick():
    s = time.strftime("%H:%M:%S")
    if s != clock["text"]:
        clock["text"] = s
    clock.after(200,tick)
tick()
root.mainloop()
