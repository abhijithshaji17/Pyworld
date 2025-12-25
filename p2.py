# Write a function average_velocity() that calculates the average velocity of an object. The function should take the initial position (s_i), final position (s_f), and time elapsed (t) as input. Use the formula: v = (s_f-s_i) / t.

def average_velocity():
	s_i = float(input("Enter the initial position: "))
	s_f = float(input("Enter the final position: "))
	t = float(input("Enter the time taken: "))
	v = (s_f - s_i)/t
	return (v)

print ("average velocity is", average_velocity(), "m/s")