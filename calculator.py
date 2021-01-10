import tkinter as tk
from tkinter import *


def calculate(event):
	global scvalue
	text  = event.widget.cget("text")
	# print(text)
	if text == "=":
		if scvalue.get().isdigit():
			value=int(scvalue.get())
		else:
			try:
				value=eval(screen.get())
			except Exception as e:
				print(e)
				value="error"

		
		scvalue.set(scvalue.get()+' = '+str(value))
		screen.update()


	elif text =="C":
		scvalue.set("")
		screen.update()

	else:
		scvalue.set(scvalue.get()+ text)
		screen.update()

		

root=tk.Tk()
root.geometry("650x800")
root.title("calculator")
root.iconbitmap(r"C:\Users\Hp\Documents\Calculator project\calc_icon.ico")


scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvar=scvalue, font="lucida 40 bold")
screen.pack(fill=X,ipadx=8,pady=10,padx=10)

f=Frame(root,bg="grey")
b=Button(f,text="9",padx=25,pady=18,font="lucida 20 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",calculate)

b=Button(f,text="8",padx=25,pady=18,font="lucida 20 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",calculate)

b=Button(f,text="7",padx=25,pady=18,font="lucida 20 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",calculate)

b=Button(f,text="/",padx=25,pady=18,font="lucida 20 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",calculate)

f.pack()


f=Frame(root,bg="grey")
b=Button(f,text="6",padx=25,pady=18,font="lucida 20 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",calculate)

b=Button(f,text="5",padx=25,pady=18,font="lucida 20 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",calculate)

b=Button(f,text="4",padx=25,pady=18,font="lucida 20 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",calculate)

b=Button(f,text="*",padx=25,pady=18,font="lucida 20 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",calculate)

f.pack()


f=Frame(root,bg="grey")
b=Button(f,text="3",padx=25,pady=18,font="lucida 20 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",calculate)

b=Button(f,text="2",padx=25,pady=18,font="lucida 20 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",calculate)

b=Button(f,text="1",padx=25,pady=18,font="lucida 20 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",calculate)

b=Button(f,text="-",padx=25,pady=18,font="lucida 20 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",calculate)

f.pack()

f=Frame(root,bg="grey")
b=Button(f,text="0",padx=25,pady=18,font="lucida 20 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",calculate)

b=Button(f,text=".",padx=25,pady=18,font="lucida 20 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",calculate)

b=Button(f,text="%",padx=25,pady=18,font="lucida 20 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",calculate)

b=Button(f,text="+",padx=25,pady=18,font="lucida 20 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",calculate)

f.pack()


f=Frame(root,bg="grey")
b=Button(f,text="C",padx=25,pady=18,font="lucida 20 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",calculate)

b=Button(f,text="(",padx=25,pady=18,font="lucida 20 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",calculate)

b=Button(f,text=")",padx=25,pady=18,font="lucida 20 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",calculate)

b=Button(f,text="=",padx=25,pady=18,font="lucida 20 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button-1>",calculate)

f.pack()

root.mainloop()