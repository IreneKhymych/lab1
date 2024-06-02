class Triangle:
    def __init__(self, a, b, c):
        if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
            self.__a = a
            self.__b = b
            self.__c = c
        else:
            raise ValueError("Invalid triangle sides")

    def perimeter(self):
        return self.__a + self.__b + self.__c

    def area(self):
        s = self.perimeter() / 2
        return (s * (s - self.__a) * (s - self.__b) * (s - self.__c)) ** 0.5

    def show(self):
        print("Triangle with sides:", self.__a, self.__b, self.__c)

def process_file_triangle(file_path):
    max_area_triangle = None
    max_perimeter_triangle = None
    max_area = float('-inf')
    max_perimeter = float('-inf')
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if not parts:
                continue
            figure_type = parts[0]
            if figure_type == "Triangle":
                parameters = list(map(float, parts[1:]))
                if len(parameters) == 3:
                    try:
                        triangle = Triangle(*parameters)
                    except ValueError:
                        continue
                    perimeter = triangle.perimeter()
                    area = triangle.area()

                    if perimeter > max_perimeter:
                        max_perimeter = perimeter
                        max_perimeter_triangle = triangle
                    if area > max_area:
                        max_area = area
                        max_area_triangle = triangle
    return max_area_triangle, max_perimeter_triangle


class Rectangle:
    def __init__(self, width, height):
        if width > 0 and height > 0:
            self.__width = width
            self.__height = height
        else:
            raise ValueError("Invalid rectangle sides")

    def perimeter(self):
        return 2 * (self.__width + self.__height)

    def area(self):
        return self.__width * self.__height

    def show(self):
        print("Rectangle with sides:", self.__width, "and", self.__height)

def process_file_rectangle(file_path):
    max_area_rectangle = None
    max_perimeter_rectangle = None
    max_area = float('-inf')
    max_perimeter = float('-inf')
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if not parts:
                continue
            figure_type = parts[0]
            if figure_type == "Rectangle":
                parameters = list(map(float, parts[1:]))
                if len(parameters) == 2:
                    try:
                        rectangle = Rectangle(*parameters)
                    except ValueError:
                        continue
                    perimeter = rectangle.perimeter()
                    area = rectangle.area()

                    if perimeter > max_perimeter:
                        max_perimeter = perimeter
                        max_perimeter_rectangle = rectangle
                    if area > max_area:
                        max_area = area
                        max_area_rectangle = rectangle
    return max_area_rectangle, max_perimeter_rectangle


class Trapeze:
    def __init__(self, base1, base2, side1, side2):
        if base1 > 0 and base2 > 0 and side1 > 0 and side2 > 0 and base1 != base2:
            self.__base1 = base1
            self.__base2 = base2
            self.__side1 = side1
            self.__side2 = side2
        else:
            raise ValueError("Invalid trapeze sides")

    def perimeter(self):
        return self.__base1 + self.__base2 + self.__side1 + self.__side2

    def area(self):
        h = self._height()
        return (self.__base1 + self.__base2) * h / 2

    def _height(self):
        return ((self.__side1 ** 2) - (((self.__base2 - self.__base1) ** 2) + (self.__side1 ** 2) - (self.__side2 ** 2)) / (2 * (self.__base2 - self.__base1))) ** 0.5

    def show(self):
        print("Trapeze with bases:", self.__base1, self.__base2, "and sides:", self.__side1, self.__side2)

def process_file_trapeze(file_path):
    max_area_trapeze = None
    max_perimeter_trapeze = None
    max_area = float('-inf')
    max_perimeter = float('-inf')
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if not parts:
                continue
            figure_type = parts[0]
            if figure_type == "Trapeze":
                parameters = list(map(float, parts[1:]))
                if len(parameters) == 4:
                    try:
                        trapeze = Trapeze(*parameters)
                    except ValueError:
                        continue
                    perimeter = trapeze.perimeter()
                    area = trapeze.area()
                    if perimeter > max_perimeter:
                        max_perimeter = perimeter
                        max_perimeter_trapeze = trapeze
                    if area.real > max_area.real:
                        max_area = area
                        max_area_trapeze = trapeze

    return max_area_trapeze, max_perimeter_trapeze


class Parallelogram:
    def __init__(self, base, side, height):
        if base > 0 and side > 0 and height > 0:
            self.__base = base
            self.__side = side
            self.__height = height
        else:
            raise ValueError("Invalid parallelogram sides")

    def perimeter(self):
        return 2 * (self.__base + self.__side)

    def area(self):
        return self.__base * self.__height

    def show(self):
        print("Parallelogram with base:", self.__base, "side:", self.__side, "and height:", self.__height)

def process_file_parallelogram(file_path):
    max_area_parallelogram = None
    max_perimeter_parallelogram = None
    max_area = -float('inf')
    max_perimeter = -float('inf')

    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if not parts:
                continue
            figure_type = parts[0]
            if figure_type == "Parallelogram":
                parameters = list(map(float, parts[1:]))
                if len(parameters) == 3:
                    try:
                        parallelogram = Parallelogram(*parameters)
                    except ValueError:
                        continue
                    area = parallelogram.area()
                    perimeter = parallelogram.perimeter()

                    if area > max_area:
                        max_area = area
                        max_area_parallelogram = parallelogram
                    if perimeter > max_perimeter:
                        max_perimeter = perimeter
                        max_perimeter_parallelogram = parallelogram

    return max_area_parallelogram, max_perimeter_parallelogram


class Circle:
    def __init__(self, radius):
        if radius > 0:
            self.__radius = radius
        else:
            raise ValueError("Invalid radius")

    def perimeter(self):
        return 2 * 3.14159 * self.__radius

    def area(self):
        return 3.14159 * (self.__radius ** 2)

    def show(self):
        print("Circle with radius:", self.__radius)

def process_file_circle(file_path):
    max_area_circle = None
    max_perimeter_circle = None
    max_area = -float('inf')
    max_perimeter = -float('inf')

    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if not parts:
                continue
            figure_type = parts[0]
            if figure_type == "Circle":
                parameters = list(map(float, parts[1:]))
                if len(parameters) == 1:
                    try:
                        circle = Circle(*parameters)
                    except ValueError:
                        continue
                    area = circle.area()
                    perimeter = circle.perimeter()
                    if area > max_area:
                        max_area = area
                        max_area_circle = circle
                    if perimeter > max_perimeter:
                        max_perimeter = perimeter
                        max_perimeter_circle = circle

    return max_area_circle, max_perimeter_circle


if __name__ == '__main__':
    file_paths = [
        "C:/Users/Volod/Downloads/input01.txt",
        "C:/Users/Volod/Downloads/input02.txt",
        "C:/Users/Volod/Downloads/input03.txt"
    ]

    max_area_figure = None
    max_perimeter_figure = None
    max_area = -float('inf')
    max_perimeter = -float('inf')

    for file_path in file_paths:

        max_area_triangle, max_perimeter_triangle = process_file_triangle(file_path)
        if max_area_triangle and max_area_triangle.area() > max_area:
            max_area = max_area_triangle.area()
            max_area_figure = max_area_triangle
        if max_perimeter_triangle and max_perimeter_triangle.perimeter() > max_perimeter:
            max_perimeter = max_perimeter_triangle.perimeter()
            max_perimeter_figure = max_perimeter_triangle

        max_area_rectangle, max_perimeter_rectangle = process_file_rectangle(file_path)
        if max_area_rectangle and max_area_rectangle.area() > max_area:
            max_area = max_area_rectangle.area()
            max_area_figure = max_area_rectangle
        if max_perimeter_rectangle and max_perimeter_rectangle.perimeter() > max_perimeter:
            max_perimeter = max_perimeter_rectangle.perimeter()
            max_perimeter_figure = max_perimeter_rectangle

        max_area_trapeze, max_perimeter_trapeze = process_file_trapeze(file_path)
        if max_area_trapeze and max_area_trapeze.area() > max_area:
            max_area = max_area_trapeze.area()
            max_area_figure = max_area_trapeze
        if max_perimeter_trapeze and max_perimeter_trapeze.perimeter() > max_perimeter:
            max_perimeter = max_perimeter_trapeze.perimeter()
            max_perimeter_figure = max_perimeter_trapeze

        # Паралелограми
        max_area_parallelogram, max_perimeter_parallelogram = process_file_parallelogram(file_path)
        if max_area_parallelogram and max_area_parallelogram.area() > max_area:
            max_area = max_area_parallelogram.area()
            max_area_figure = max_area_parallelogram
        if max_perimeter_parallelogram and max_perimeter_parallelogram.perimeter() > max_perimeter:
            max_perimeter = max_perimeter_parallelogram.perimeter()
            max_perimeter_figure = max_perimeter_parallelogram

        max_area_circle, max_perimeter_circle = process_file_circle(file_path)
        if max_area_circle and max_area_circle.area() > max_area:
            max_area = max_area_circle.area()
            max_area_figure = max_area_circle
        if max_perimeter_circle and max_perimeter_circle.perimeter() > max_perimeter:
            max_perimeter = max_perimeter_circle.perimeter()
            max_perimeter_figure = max_perimeter_circle

    print("Фігура з найбільшою площею:")
    max_area_figure.show()
    print("Найбільша площа:", max_area)

    print("Фігура з найбільшим периметром:")
    max_perimeter_figure.show()
    print("Найбільший периметр:", max_perimeter)
