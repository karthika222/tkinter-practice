import tkinter as tk

root = tk.Tk()
root.geometry("400x200")

frame = tk.Frame(root, bg="lightblue")
frame.pack(padx=30, pady=30)  # space OUTSIDE the frame

label = tk.Label(frame, text="Inside Frame", bg="yellow")
label.pack(padx=20, pady=20)  # space INSIDE the frame (around label)

root.mainloop()
