from tkinter import *
import math

def draw_set(top, maxModules, maxIterations, c):
	value = 100
	canvas = Canvas(top, bg="white", height=value, width=value)
	img = PhotoImage(width=value, height=value)
	canvas.create_image((0, 0), image=img, state="normal")
	canvas.pack(fill=BOTH, expand=YES)
	
	delta = 4 / value
	pixelx = 0
	complexx = -2
	while pixelx < value:
		pixely = 0
		complexy = 2
		while pixely < value: 
			# print("x = " + str(pixelx) + "\ny = " + str(pixely))
			# for each x and y value caluculate z 
			iterations = iterate(complexx, complexy, maxModules, maxIterations, c)
			# print("Iterations = " + str(iterations))
			col = colorZ(iterations,maxIterations)
			# print("col = " + str(col))
			
			# create a pixel at color: col at (pixelx, pixely)
			img.put(col, (pixelx, pixely))
		
			pixely = pixely + 1
			complexy = complexy - delta

		pixelx = pixelx + 1
		complexx = complexx + delta
	top.mainloop()

def iterate(x, y, maxModules, maxIterations, c):
	count = 0
	do_continue = 1
	# print("c = " + str(c))
	# print("maxModules = " + str(maxModules))

	while (count < maxIterations) and ((math.fabs(x.real) < maxModules) and (math.fabs(y.real) < maxModules)):
		x = (x * x) + c
		y = (y * y) + c
		# print("x = " + str(x))
		
		count = count + 1

	# print("count = " + str(count))
	# print("x = " + str(x))
	# print("y = " + str(y))

	return count
	
# return a color corresponding to the value of the tuple z
def colorZ(z, maxIterations):
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
	
# need to map to plane
def main():
	top = Tk()

	maxModules = 2.0
	maxIterations = 50

	c = -0.996 + 0.252j
	draw_set(top, maxModules, maxIterations, c)
	# c = -0.271 - 0.702j
	# draw_set(top, maxModules, maxIterations, c)
	# c = 0.522 - 0.53j
	# draw_set(top, maxModules, maxIterations, c)
	# c = 0.05 - 0.139j
	# draw_set(top, maxModules, maxIterations, c)
	# c = 0.19 + 0.98j
	# draw_set(top, maxModules, maxIterations, c)
	
	# top.mainloop()

main()