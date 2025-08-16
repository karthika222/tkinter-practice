import tkinter as tk

root = tk.Tk()
root.geometry("400x200")

btn1 = tk.Button(root, text="Normal Button")
btn1.pack(pady=5)

btn2 = tk.Button(root, text="Bigger with ipadx=20, ipady=10")
btn2.pack(pady=5, ipadx=20, ipady=10)
#ipadx & ipady ---> is for size of button
#padx and pady---> spaces between next

btn3 = tk.Button(root, text="Bigger with width=20, height=3")
btn3.pack(pady=10)

root.mainloop()
