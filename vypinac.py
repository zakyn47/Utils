import os
import tkinter as tk
from tkinter import messagebox

def shutdown():
    timer = e1.get()
    if timer.isdigit():
        os.system(f"shutdown /s /t {int(timer)*60}")
        messagebox.showinfo("Shutdown", f"Your PC will shutdown in {timer} minutes.")
    else:
        messagebox.showerror("Error", "Please enter a valid number.")

def cancel_shutdown():
    os.system("shutdown /a")
    messagebox.showinfo("Shutdown", "Shutdown has been cancelled.")

root = tk.Tk()
root.title("Shutdown Timer")
root.geometry("300x100")

tk.Label(root, text="Enter time in minutes:").grid(row=0)
e1 = tk.Entry(root)
e1.grid(row=0, column=1)

tk.Button(root, text="Set Timer", command=shutdown).grid(row=3, column=1, sticky=tk.W, pady=4)
tk.Button(root, text="Cancel Shutdown", command=cancel_shutdown).grid(row=4, column=1, sticky=tk.W, pady=4)

root.mainloop()