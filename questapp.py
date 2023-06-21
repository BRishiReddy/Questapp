from tkinter import * 


def addbutton():
    name=entry.get()
    nbutton =Button(tk, text=name,command=lambda:delete(nbutton,name),width=10)
    nbutton.pack()
    addfile("1.txt",name)
    entry.delete(0,END)
def delete(button,peru):
    button.destroy()
    removefile("1.txt",peru)
def addfile(filename,data):
    with open(filename,'a') as file:
        file.write(str(data)+'\n')
def removefile(filename,data):
    with open(filename,'r') as file:
        lines=file.readlines()
    updated_lines = [line for line in lines if line.strip() != data]
    with open(filename,'w') as file:
            file.writelines(updated_lines)
tk= Tk()


Label2=Label(tk,text='enter the tasks')
Label2.pack()
entry=Entry(tk,width=30)
entry.pack()


button = Button(tk, text="submit", command=addbutton,width=10)
button.pack()

Label3=Label(tk,text="Note: After finishing the task click on the task to remove it")
Label3.pack()

tk.mainloop()
