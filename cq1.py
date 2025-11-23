'''
Write a function average_velocity() that calculates the average velocity of an object.
'''
def average_velocity(s_i, s_f, t):
   if t == 0:
       return "Time cannot be zero!"
   v = (s_f - s_i) / t
   return v
s_i = float(input("Enter the initial position: "))
s_f = float(input("Enter the final position: "))
t = float(input("Enter the time taken: "))

print ("The average velocity is", average_velocity(s_i, s_f, t), "m/s")

