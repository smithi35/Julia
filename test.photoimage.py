from tkinter import *
import math

def create_image():
	global img
	print("Creating")
	print(col[index])

	for i in range(40):
		for j in range(60):
			img.put(col[index], (j, i))

def click(event):
	global index
	index = index + 1

	if index == len(col):
		index = 0
	# print(index)

	create_image()

def main():
	global img

	tk = Tk()
	canvas = Canvas(tk, bg="white", height=600, width=800)
	canvas.pack()
	canvas.bind("<Button-1>", click)

	img = PhotoImage(width=500, height=500)
	canvas.create_image((0, 0), image=img)

	create_image()

	tk.mainloop()

col = ["black", "grey", "green", "red"]
index = 0

main()