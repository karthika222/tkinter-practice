import tkinter as tk
root=tk.Tk()
root.title("Hello Tkinter")
root.geometry("700x500")
l=tk.Label(root,text="Enter name: ")#label----> it is to display what to be shown on screen 
l.grid(row=0,column=0)# grid----> is to set the location
#l.pack()-----> will not be able to keep in desired position
e=tk.Entry(root)
e.grid(row=0,column=1)
#e.pack()
l1=tk.Label(root,text="Enter address: ")
l1.grid(row=1,column=0)
e1=tk.Entry(root)
e1.grid(row=1,column=1)
out_label=tk.Label(root, text="",fg="blue")
out_label.grid(row=3,column=3,columnspan="2")

def submit():
    name=e.get()#get() is used only for Entry method only
    ad=e1.get()
    
    #if you want to print on console
    #print("Name: ",name)
    #print("Address: ",ad); 
    
    #if want to print on the GUI screen itself
    out_label.config(text= f"Name: {name}  Address: {ad}")
    
b1=tk.Button(root,text="Submit",command=submit)
b1.grid(row=2,column=0)
root.mainloop()

