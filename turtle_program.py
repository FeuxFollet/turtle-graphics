import turtle
import random

class ShapeMaster:
    def __init__(self, shape, echo):
        self.shape = shape
        self.echo = echo

    def _draw_polygon(self, num_sides, size, orientation, location, color, border_size):
        turtle.penup()
        turtle.goto(location[0], location[1])
        turtle.setheading(orientation)
        turtle.color(color)
        turtle.pensize(border_size)
        turtle.pendown()
        for _ in range(num_sides):
            turtle.forward(size)
            turtle.left(360 / num_sides)
        turtle.penup()

    def _get_new_color(self):
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def _draw_one(self):
        # choose number of sides
        if self.shape == "triangle":
            num_sides = 3
        elif self.shape == "square":
            num_sides = 4
        elif self.shape == "pentagon":
            num_sides = 5
        elif self.shape == "random":
            num_sides = random.randint(3, 5)

        # draw a polygon at a random location, orientation, color, and border line thickness
        size = random.randint(50, 150)
        orientation = random.randint(0, 360)
        location = [random.randint(-300, 300), random.randint(-200, 200)]
        color = self._get_new_color()
        border_size = random.randint(1, 5)

        self._draw_polygon(num_sides, size, orientation, location, color, border_size)

        # draw inner echoes
        if self.echo == "random":
            num_echoes = random.randint(0,3)
        else:
            num_echoes = self.echo
        for _ in range(num_echoes):
            reduction_ratio = 0.618

            # reposition the turtle and get a new location
            turtle.penup()
            turtle.forward(size * (1 - reduction_ratio) / 2)
            turtle.left(90)
            turtle.forward(size * (1 - reduction_ratio) / 2)
            turtle.right(90)
            location[0] = turtle.pos()[0]
            location[1] = turtle.pos()[1]

            # adjust the size according to the reduction ratio
            size *= reduction_ratio

            # draw the second polygon embedded inside the original
            self._draw_polygon(num_sides, size, orientation, location, color, border_size)

    def draw(self):
        n = random.randint(20, 35)
        for i in range(n):
            self._draw_one()
            try:
                turtle.update()
            except Exception:
                pass
        turtle.done()


# Setup turtle
turtle.speed(0)
turtle.bgcolor('black')
turtle.colormode(255)
turtle.tracer(0)

while True:
    userinp = input('Which art do you want to generate? Enter a number between 1 to 9 inclusive: ')
    try:
        userinp = int(userinp)
        if userinp in range(1,10):
            break
        print("Invalid input")
    except ValueError:
        print("Invalid input")


if userinp == 1:
    number1 = ShapeMaster("triangle", 0)
    number1.draw()
elif userinp == 2:
    number2 = ShapeMaster("square", 0)
    number2.draw()
elif userinp == 3:
    number3 = ShapeMaster("pentagon" ,0)
    number3.draw()
elif userinp == 4:
    number4 = ShapeMaster("random", 0)
    number4.draw()
elif userinp == 5:
    number5 = ShapeMaster("triangle", 2)
    number5.draw()
elif userinp == 6:
    number6 = ShapeMaster("square", 2)
    number6.draw()
elif userinp == 7:
    number7 = ShapeMaster("pentagon", 2)
    number7.draw()
elif userinp == 8:
    number8 = ShapeMaster("random", 2)
    number8.draw()
elif userinp == 9:
    number9 = ShapeMaster("random", "random")
    number9.draw()