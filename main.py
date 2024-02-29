class Triangle:
    def __init__(self, a, b, c):
        if self._is_valid_triangle(a, b, c):
            self.__a = a
            self.__b = b
            self.__c = c
        else:
            raise ValueError("Неправильні сторони")

    def perimeter(self):
        return self.__a + self.__b + self.__c

    def area(self):
        p = self.perimeter() / 2
        a = self.__a
        b = self.__b
        c = self.__c
        if self._is_valid_triangle(a, b, c):
            return (p * (p - a) * (p - b) * (p - c)) ** 0.5
        else:
            return float('-inf')

    def _is_valid_triangle(self, a, b, c):
        return a + b > c and a + c > b and b + c > a

def process_file(file_path):
    max_area_triangle = None
    max_perimeter_triangle = None
    max_area = float('-inf')
    max_perimeter = float('-inf')
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
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

if __name__ == '__main__':
    file_paths = [
        "C:/Users/Volod/Downloads/input01.txt",
        "C:/Users/Volod/Downloads/input02.txt",
        "C:/Users/Volod/Downloads/input03.txt"
    ]
    max_area = float('-inf')
    max_perimeter = float('-inf')
    for file_path in file_paths:
        max_area_triangle, max_perimeter_triangle = process_file(file_path)
        if max_area_triangle:
            area = max_area_triangle.area()
            if area > max_area:
                max_area = area
                max_perimeter = max_perimeter_triangle.perimeter()

    if max_area != float('-inf'):
        print("Найбільша площа трикутника:", max_area)
        print("Найбільший периметр трикутника:", max_perimeter)
    else:
        print("Не знайдено дійсних трикутників")

class Rectangle:
    def __init__(self, width, height):
        if width > 0 and height > 0:
            self.__width = width
            self.__height = height
        else:
            raise ValueError("Неправильні сторони")

    def perimeter(self):
        return 2 * (self.__width + self.__height)

    def area(self):
        return self.__width * self.__height

def process_file(file_path):
    max_area_rectangle = None
    max_perimeter_rectangle = None
    max_area = float('-inf')
    max_perimeter = float('-inf')
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
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

if __name__ == '__main__':
    file_paths = [
        "C:/Users/Volod/Downloads/input01.txt",
        "C:/Users/Volod/Downloads/input02.txt",
        "C:/Users/Volod/Downloads/input03.txt"
    ]
    max_area = float('-inf')
    max_perimeter = float('-inf')
    for file_path in file_paths:
        max_area_rectangle, max_perimeter_rectangle = process_file(file_path)
        if max_area_rectangle:
            area = max_area_rectangle.area()
            if area > max_area:
                max_area = area
                max_perimeter = max_perimeter_rectangle.perimeter()

    if max_area != float('-inf'):
        print("Найбільша площа прямокутника:", max_area)
        print("Найбільший периметр прямокутника:", max_perimeter)
    else:
        print("Не знайдено дійсних прямокутників")


class Trapeze:
    def __init__(self, base1, base2, side1, side2):
        if base1 > 0 and base2 > 0 and side1 > 0 and side2 > 0 and base1 != base2 and side1 != side2:
            self.__base1 = base1
            self.__base2 = base2
            self.__side1 = side1
            self.__side2 = side2
        else:
            raise ValueError("Неправильні сторони")

    def perimeter(self):
        return self.__base1 + self.__base2 + self.__side1 + self.__side2

    def area(self):
        h = self._height()
        return (self.__base1 + self.__base2) * h / 2

    def _height(self):
        return ((self.__side1 ** 2) - (((self.__base2 - self.__base1) ** 2) + (self.__side1 ** 2) - (self.__side2 ** 2)) / (2 * (self.__base2 - self.__base1))) ** 0.5

def process_file(file_path):
    max_area_trapeze = None
    max_perimeter_trapeze = None
    max_area = float('-inf')
    max_perimeter = float('-inf')
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
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

if __name__ == '__main__':
    file_paths = [
        "C:/Users/Volod/Downloads/input01.txt",
        "C:/Users/Volod/Downloads/input02.txt",
        "C:/Users/Volod/Downloads/input03.txt"
    ]
    max_area = float('-inf')
    max_perimeter = float('-inf')
    for file_path in file_paths:
        max_area_trapeze, max_perimeter_trapeze = process_file(file_path)
        if max_area_trapeze:
            area = max_area_trapeze.area()
            perimeter = max_perimeter_trapeze.perimeter()
            if area > max_area:
                max_area = area
                max_perimeter = perimeter

    if max_area != float('-inf'):
        print("Найбільша площа трапеції:", max_area)
        print("Найбільший периметр трапеції:", max_perimeter)
    else:
        print("Не знайдено дійсних трапецій")


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

def process_file(file_path):
    max_area_parallelogram = None
    max_perimeter_parallelogram = None
    max_area = -float('inf')
    max_perimeter = -float('inf')

    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
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

if __name__ == '__main__':
    file_paths = [
        "C:/Users/Volod/Downloads/input01.txt",
        "C:/Users/Volod/Downloads/input02.txt",
        "C:/Users/Volod/Downloads/input03.txt"
    ]
    max_area = -float('inf')
    max_perimeter = -float('inf')
    max_area_parallelogram = None
    max_perimeter_parallelogram = None

    for file_path in file_paths:
        max_area_parallelogram_file, max_perimeter_parallelogram_file = process_file(file_path)

        if max_area_parallelogram_file:
            area = max_area_parallelogram_file.area()
            perimeter = max_perimeter_parallelogram_file.perimeter()
            if area > max_area:
                max_area = area
                max_area_parallelogram = max_area_parallelogram_file
            if perimeter > max_perimeter:
                max_perimeter = perimeter
                max_perimeter_parallelogram = max_perimeter_parallelogram_file

    if max_area_parallelogram:
        print("Найбільша площа паралелограма:", max_area)
        print("Найбільший периметр паралелограма:", max_perimeter)
    else:
        print("Не знайдено дійсного паралелограма")

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

def process_file(file_path):
    max_area_circle = None
    max_perimeter_circle = None
    max_area = -float('inf')
    max_perimeter = -float('inf')

    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
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

    max_area_circle = None
    max_perimeter_circle = None
    max_area = -float('inf')
    max_perimeter = -float('inf')

    for file_path in file_paths:
        max_area_circle_file, max_perimeter_circle_file = process_file(file_path)

        if max_area_circle_file:
            area = max_area_circle_file.area()
            perimeter = max_perimeter_circle_file.perimeter()
            if area > max_area:
                max_area = area
                max_area_circle = max_area_circle_file
            if perimeter > max_perimeter:
                max_perimeter = perimeter
                max_perimeter_circle = max_perimeter_circle_file

    if max_area_circle:
        print("Найбільша площа круга:", max_area)
        print("Найбільший периметр круга:", max_perimeter)
    else:
        print("Не знайдено дійсного круга")
