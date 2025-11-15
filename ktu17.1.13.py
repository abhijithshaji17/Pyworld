#Finding Quadrant of a given point
def find_quadrant(x,y):
	if x==0 and y==0:
  		return "Origin"
	elif x==0:
    		if y > 0:
        		return "Positive Y-axis"
    		else y < 0:
        		return "Negative Y-axis"
	elif y==0:
    		if x > 0:
        		return "Positive X-axis"
    		else x < 0:
        		return "Negative X-axis"
	elif x > 0 and y > 0:
    	return "Quadrant I"
	elif x < 0 and y > 0:
    	return "Quadrant II"
	elif x < 0 and y < 0:
    	return "Quadrant III"
	elif x > 0 and y < 0:
    	return "Quadrant IV"
x_coord = float(input("Enter the x-coordinate: "))
y_coord = float(input("Enter the y-coordinate: "))
result = find_quadrant(x_coord, y_coord)
print (find_quadrant(x,y))


