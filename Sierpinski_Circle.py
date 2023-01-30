import turtle
#Muhammad Irsyad Jazli Bin Ramli, 223890U, Tutorial Group 1

def drawCircle(radius, myTurtle, index=0):
    colours = ["blue", "red", "green", "cyan", "yellow", "pink"]  # Added Code
    myTurtle.up()

    myTurtle.down()
    myTurtle.fillcolor(colours[index % len(colours)])
    myTurtle.begin_fill()
    myTurtle.circle(radius)
    myTurtle.end_fill()
    myTurtle.up()


def getMid(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)


def sierpinski(curr_offset, radius, rotation_shift, degree, myTurtle):

    smaller_radius = radius * (2 ** 0.5 - 1)
    smaller_rotation_shift = 90
    drawCircle(radius, myTurtle, degree)

    # Locate starting position 
    if curr_offset + rotation_shift > 0:
        myTurtle.circle(radius, 360 - curr_offset - rotation_shift)

    if degree > 0:
        myTurtle.circle(radius, 45)
        sierpinski(45, smaller_radius, smaller_rotation_shift, degree - 1, myTurtle)
        myTurtle.circle(radius, 90)
        sierpinski(90 + 45, smaller_radius, smaller_rotation_shift, degree - 1, myTurtle)
        myTurtle.circle(radius, 90)
        sierpinski(90 + 45 + 90, smaller_radius, smaller_rotation_shift, degree - 1, myTurtle)
        myTurtle.circle(radius, 90 + 45)

    # Return to origin
    if curr_offset + rotation_shift > 0:
        myTurtle.circle(radius, curr_offset + rotation_shift)


def main():
    myTurtle = turtle.Turtle()
    turtle.tracer(0, 0)  # Uncomment To show up instantly
    myTurtle.speed(10)  # adjust the drawing speed here
    myWin = turtle.Screen()
    myTurtle.up()
    myTurtle.goto(0, -200)

    radius = 200
    degree = 5  # Vary the degree of complexity here

    sierpinski(0, radius, 0, degree, myTurtle)  # first call of the recursive function

    myTurtle.hideturtle()  # hide the turtle cursor after drawing is# completed
    myWin.exitonclick()  # Exit program when user click on window


main()