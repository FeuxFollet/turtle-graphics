# Turtle Graphics Polygon Art Generator

This Python program generates colorful geometric art using the turtle graphics library.
Users can choose from different shapes (triangle, square, pentagon, random shapes) and optional echo effects, which draw smaller versions of the polygon inside itself.

## ShapeMaster Class

This class is responsible for drawing all shapes.
Each object of this class knows what shape to draw and how many echoes (inner shapes) to generate.

### Attributes
- `shape` (str): What type of shape to draw `random` for random shape.
- `echo` (int, str): How many inner echos to draw `random` for random amounts of echo.

### Methods
- `_draw_polygon(...)`: Draw a shape based on the given in parameters.
- `_get_new_color()`: Returns a random RGB color.
- `_draw_one()`: Draw one random shape (with optional echoes).
- `draw()` : The actual method used to draw multiple shapes on the cavas.

##  How the program Works

The battle logic in `turtle_program.py` follows these steps:

1. First the program sets up turtle.
2. Ask the user for which art to generate.
    - Art 1 : All triangles, no echoes
    - Art 2 : All squares, no echoes
    - Art 3 : All pentagons, no echoes
    - Art 4 : Random shape, no echoes
    - Art 5 : All triangles, two echoes
    - Art 6 : All squares, two echoes
    - Art 7 : All pentagons, two echoes
    - Art 8 : Random shape, two echoes
    - Art 9 : Random shape, random echoes
3. Create a ShapeMaster object.
4. Draw it out.
5. Window stays until closed.

##  Running the program

To run the simulation, execute `turtle_program.py`:

```bash
python turtple_program.py