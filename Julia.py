from tkinter import *
import math

class Julia_Set:

	def __init__(self, set):
		self.set = set
		self.size = 200
		self.maxModules = 2.0
		self.maxIterations = 50

		self.tk = Tk()
		self.canvas = Canvas(self.tk, bg="white", height=self.size, width=self.size)
		self.canvas.pack()
		self.canvas.bind("<Button-1>", self.click)

		img = PhotoImage(width=self.size, height=self.size)
		self.drawnimage = self.canvas.create_image((0, 0), image=img, state="normal")

		self.top = 2j
		self.left = -2
		self.scale = 4

		self.draw_set()
		self.tk.mainloop()

	def click(self, event):
		# self.canvas.delete(ALL)
		# print("click")
		self.center = (event.x, event.y)
		# print(self.center)

		# convert to complex coordinates
		self.set_plane()
		# print(self.center)
		self.scale = self.scale / 1.5
		# print(self.scale)
		self.left = self.center.real - (self.scale / 2)
		# print(self.left)
		self.top = self.center.imag + (self.scale / 2)
		# print(self.top)

		# redraw
		self.draw_set()

	# convert self.center to the complex plane
	def set_plane(self):
		pixely = 0
		complexy = self.top
		stopper = self.center[1]

		while pixely < stopper:
			pixely = pixely + 1
			complexy = complexy - self.deltay

		pixelx = 0
		complexx = self.left
		stopper = self.center[0]

		while pixelx < stopper:
			pixelx = pixelx + 1
			complexx = complexx + self.deltax

		self.center = complexx + complexy

	def draw_set(self):
		out = PhotoImage(width=self.size, height=self.size)
		self.canvas.itemconfig(self.drawnimage, image=out)

		self.deltax = self.scale / self.size

		init_complex = 1j
		init_complex = self.scale * init_complex
		self.deltay = init_complex / self.size

		pixelx = 0
		complexx = self.left

		while pixelx < self.size:
			pixely = 0
			complexy = self.top

			while pixely < self.size: 
				complex = complexx + complexy
				# print(complex)

				# for each x and y value caluculate z 
				iterations = self.iterate(complex)
				# print("iterations = " + str(iterations))

				col = self.colorZ(iterations)
				# print("col = " + str(col))

				# create a pixel at color: col at (pixelx, pixely)
				out.put(col, (pixelx, pixely))

				pixely = pixely + 1
				complexy = complexy - self.deltay

			pixelx = pixelx + 1
			complexx = complexx + self.deltax
			# print("complexx = " + str(complexx) + ", complexy = " + str(complexy))
		print("Drawn")

	def iterate(self, complex):
		count = 0

		while (count < self.maxIterations) and (math.fabs(complex.real) < self.maxModules):
			complex = self.set(complex)
			# print("complex = " + str(complex))
			count = count + 1

		# print("count = " + str(count))
		# print("complex = " + str(complex))

		return count

	def colorZ(self, z):
		col = ""

		if z == self.maxIterations:
			col = "black"
		elif z == 0:
			col = "white"
		else:
			# start with white, increment according to z
			icol = [0xff, 0xff, 0xff]
			col = "#"

			delta = int(icol[0] / self.maxIterations)
			for i in range(3):
				j = 0
				while j < z:
					icol[i] = icol[i] - delta
					j = j + 1
				# append icol[i] to col

				out = hex(icol[i]).upper()
				out = "{0:02X}".format(icol[i])
				col = col + out

			# col = hex(icol).upper()
			# col = format(col, 'x')
		# print("col = " + str(col))

		return col

def mandelbrot(complex) :
	return complex * complex + complex

def first(complex) :
	c = -0.996 + 0.252j
	return (complex * complex) + c

def second(complex) :
	c = -0.274 - 0.702j
	return (complex * complex * complex) + c

def third(complex) :
	c = 0.522 - 0.53j
	return (c * complex) + ((1-c) * complex)

def fourth(complex) :
	c = 0.05 - 0.139j
	return (complex * complex) + (c / complex)

def fifth(complex) :
	c = 0.19 + 0.98j
	return (complex * c) + ((1 - c) / (complex * complex))

# need to map to plane
def main():
	mandelbrot_set = Julia_Set(mandelbrot)
	# first_set = Julia_Set(first)
	# second_set = Julia_Set(second)
	# third_set = Julia_Set(third)
	# fourth_set = Julia_Set(fourth)
	# fifth_set = Julia_Set(fifth)

main()