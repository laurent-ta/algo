#!/usr/bin/python
#This function take a matrix and examines and print each item in a spiral order.

m = [[00, 01, 02, 03, 04],
    [10, 11, 12, 13, 14],
    [20, 21, 22, 23, 24],
    [30, 31, 32, 33, 34]]

def list_tab(m):
	
	x = 0
	y = 0
	i = 0

	dir = "right"	
	width = len(m[0])
	height = len(m)

	size = width*height

        top_border = 1
       	left_border = 0

	while i < size:

		if dir == "right": 
			while x < width - 1:
				print m[y][x]
				x += 1
				i += 1			
			
			width = width - 1
			dir = "bottom"

		if dir == "bottom":
			while y < height - 1:
				print m[y][x]
				y += 1
				i += 1       
			height = height - 1
			dir = "left"

		if dir == "left":
                	while x > left_border: 
                        	print m[y][x]
                        	x -= 1
                        	i += 1
			left_border = left_border + 1
			dir = "up"

		if dir == "up":
                	while y > top_border:
                        	print m[y][x]
                        	y -= 1
                        	i += 1
			top_border = top_border + 1
			dir = "right"

		if i == (size - 1):
			print m[y][x]
			i += 1

list_tab(m)
