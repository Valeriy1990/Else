from tkinter import *
from tkinter import ttk
 
root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")
 
canvas = Canvas(bg="white", width=250, height=150)
canvas.pack(fill=BOTH, expand=1)
 
# размеры прямоугольника
big_size = (60, 60, 150, 150)
small_size = (60, 60, 100, 100)
 
# обработчики событий
def make_big(event): canvas.coords(id, big_size)
def make_small(event): canvas.coords(id, small_size)
 
id = canvas.create_rectangle(small_size, fill="red")
# привязка событий к элементу с идентификатором id
canvas.tag_bind(id, "<Enter>", make_big)
canvas.tag_bind(id, "<Leave>", make_small)
 
root.mainloop()