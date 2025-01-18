import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("yellow")

# Create a turtle
pen = turtle.Turtle()
pen.speed(0)  # Set the turtle speed to the fastest
pen.color("red")
pen.width(2)

# Draw a spiral pattern
for i in range(100):
    pen.forward(i * 10)
    pen.right(144)  # Angle for star-like shapes

# Close the drawing window on click
screen.mainloop()
