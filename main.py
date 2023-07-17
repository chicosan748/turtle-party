#Turtle Party
#By Santiago Samorano  
#07-17-23

#print("hello world!")

import turtle

#size=100
turtle.color ("red")
#turtle.forward (size)
#turtle.left (120) 
#turtle.forward (size)
#turtle.left (120)
#turtle.forward (size)
#turtle.left (120)

#for i in range(3):
#  turtle.forward (size)
#  turtle.left (120)

#def triangle(size):       #function name(parameter(s))
#  for i in range(3):      #function body with a range of 3 sides
#    turtle.forward (size) #function body
#    turtle.left (120)     #function body with a 120 degree angle
#    turtle.color("red")
    
#def square(size):         #function name(parameters)
#  for i in range(4):      #function body with a range of 4 sides
#    turtle.forward (size) #function body
#    turtle.left (90)      #function body with a 90 degree angle  
#    turtle.color("blue")
    
# def poly(size):           #function name(parameters)
#   for i in range(12):     #function body with a range of 12 sides
#     turtle.forward (size) #function body
#     turtle.left (30)      #function body with a 90 degree angle  
#     turtle.color("blue")

#   for i in range(6):      #function body with a range of 12 sides
#     turtle.forward (size) #function body
#     turtle.left (60)      #function body with a 90 degree angle  
#     turtle.color("red")

def back(len):           #function name(parameter(s))
  turtle.penup()
  turtle.backward(len)
  turtle.pendown()

#fwd helper function
def move(len):
  back(-1*len)
  
def poly(num, size):
  for i in range (num):
    turtle.forward (size)       #function body
    turtle.left (360 / num)     #function body with a 90 degree angle 
    
# for n in range(3,10):
#   move(50) #fwd
#   poly(n, 100/n)
#   back(50)
#   turtle.right (360/7)
      
def spiral(len,angle):
  for i in range (len,5,-5):
    turtle.forward (i)
    turtle.right(angle)
    
spiral(95,50)
move(150)
turtle.color("blue")
spiral(100,90)
    
# poly(3,100) 
# back(75)
# poly(140,1)
# square(100)  #calls the function: executed 1st since it's on top
# triangle(100)  #calls the function: executed 2nd
# back(75)
# poly(15) 
# back(50)
# square(25) 
