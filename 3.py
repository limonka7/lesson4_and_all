from tkinter import*
root=Tk()
def myClick():
    myLabel=Label(root, text="Look! i clicked a Button!")
    myLabel.pack()
myButton=Button(root, text="Click Me!", command=myClick, fg="blue", bg="#ffffff")
myButton.pack()
root.mainloop()