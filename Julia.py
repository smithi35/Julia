from tkinter import Tk, Canvas, PhotoImage, mainloop
import math

# zoom in on the location indicated by the event
# modify the maxModules and maxIterations accordingly
def click(event) :
	global maxModules, maxIterations
	
	# (event.x, event.y) becomes the middle of the screen
	
	print("x = " + str(event.x) + ", y = " + str(event.y))

def draw_set(julia_set):
	top = Tk()
	value = 300
	canvas = Canvas(top, bg="white", height=value, width=value)
	canvas.bind("<Button-1>", click)
	img = PhotoImage(width=value, height=value)
	canvas.create_image((0, 0), image=img, state="normal")
	canvas.pack()
	
	deltax = 4 / value
	deltay = 4j / value
	pixelx = 0
	complexx = -2
	while pixelx < value:
		pixely = 0
		complexy = 2j

		while pixely < value: 
			complex = complexx + complexy

			# for each x and y value caluculate z 
			iterations = iterate(complex, julia_set)
			# print("iterations = " + str(iterations))

			col = colorZ(iterations)
			# print("col = " + str(col))
			
			# create a pixel at color: col at (pixelx, pixely)
			img.put(col, (pixelx, pixely))
		
			pixely = pixely + 1
			complexy = complexy - deltay

		pixelx = pixelx + 1
		complexx = complexx + deltax
		# print("complexx = " + str(complexx) + ", complexy = " + str(complexy))
	
	top.mainloop()

def iterate(complex, julia_set):
	count = 0
	# print("maxModules = " + str(maxModules))
	# print("maxIterations = " + str(maxIterations))

	while (count < maxIterations) and (math.fabs(complex.real) < maxModules):
		complex = julia_set(complex)
		# print("complex = " + str(complex))
		count = count + 1

	# print("count = " + str(count))
	# print("complex = " + str(complex))

	return count
	
# return a color corresponding to the value of the tuple z
def colorZ(z):
	col = ""
	
	if z == maxIterations:
		col = "black"
	elif z == 0:
		col = "white"
	else:
		# start with white, increment according to z
		icol = [0xff, 0xff, 0xff]
		col = "#"
		
		delta = int(icol[0] / maxIterations)
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
	global maxModules, maxIterations
	maxModules = 2.0
	maxIterations = 50

	draw_set(mandelbrot)
	# draw_set(first)
	# draw_set(second)
	# draw_set(third)
	# draw_set(fourth)
	# draw_set(fifth)

main()