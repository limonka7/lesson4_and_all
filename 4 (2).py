import tkinter as tk
def myClick():
    message = f"Привет {entry.get()}!"
    popup = tk.Toplevel (root)
    popup. title ("Сообщение")
    label = tk. Label(popup,text=message)
    label.pack()
root = tk.Tk()
root. title("Окно с Entry и кнопкой")
entry = tk.Entry(root, width=50,bg='blue', fg='white', borderwidth=5)
entry. insert(0, "Введите ваше имя")
entry.pack()
button = tk.Button(root,text="Показать сообщение",command=myClick,bg='blue',fg='white',borderwidth=5)
button.pack()
root.mainloop()