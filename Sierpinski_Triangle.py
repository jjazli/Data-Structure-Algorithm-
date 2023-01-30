import turtle
#Muhammad Irsyad Jazli Bin Ramli, 223890U and Tutorial Group 1

def drawTriangle(points, myTurtle, index=0):
    colours = ["blue", "red", "green", "cyan", "yellow", "pink"]
    myTurtle.up()
    myTurtle.goto(points[0][0], points[0][1])
    myTurtle.down()

    myTurtle.fillcolor(colours[index % len(colours)])
    myTurtle.begin_fill()

    myTurtle.goto(points[1][0], points[1][1])
    myTurtle.goto(points[2][0], points[2][1])
    myTurtle.goto(points[0][0], points[0][1])

    myTurtle.end_fill()



def getMid(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)


def sierpinski(points, degree, myTurtle):

    drawTriangle(points, myTurtle, degree)

    if degree > 0:
        sierpinski([points[0],
                    getMid(points[0], points[1]),
                    getMid(points[0], points[2])],
                   degree - 1, myTurtle)
        sierpinski([points[1],
                    getMid(points[0], points[1]),
                    getMid(points[1], points[2])],
                   degree - 1, myTurtle)
        sierpinski([points[2],
                    getMid(points[2], points[1]),
                    getMid(points[0], points[2])],
                   degree - 1, myTurtle)


def main():
    myTurtle = turtle.Turtle()
    turtle.tracer(0, 0)  # To show up instantly
    myTurtle.speed(10)  # adjust the drawing speed here
    myWin = turtle.Screen()
    # 3 points of the first triangle based on [x,y] coordinates
    myPoints = [[-200, -50], [0, 200], [200, -50]]
    degree = 5  # Vary the degree of complexity here

    # first call of the recursive function
    sierpinski(myPoints, degree, myTurtle)

    myTurtle.hideturtle()  # hide the turtle cursor after drawing is
    # completed

    myWin.exitonclick()  # Exit program when user click on window


main()
