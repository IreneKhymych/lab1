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

    def show(self):
        print("Triangle:", self.__a, self.__b, self.__c)

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
    for file_path in file_paths:
        max_area_triangle, _ = process_file(file_path)
        if max_area_triangle:
            area = max_area_triangle.area()
            if area > max_area:
                max_area = area
    if max_area != float('-inf'):
        print("Найбільша площа трикутника:", max_area)
    else:
        print("Не знайдено дійсних трикутників")

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


def process_file(file_path):
    max_area_rectangle = None
    max_area = float('-inf')

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
                    area = rectangle.area()

                    if area > max_area:
                        max_area = area
                        max_area_rectangle = rectangle

    return max_area_rectangle


if __name__ == '__main__':
    file_paths = [
        "C:/Users/Volod/Downloads/input01.txt",
        "C:/Users/Volod/Downloads/input02.txt",
        "C:/Users/Volod/Downloads/input03.txt"
    ]
    max_area = float('-inf')

    for file_path in file_paths:
        max_area_rectangle = process_file(file_path)

        if max_area_rectangle:
            area = max_area_rectangle.area()
            if area > max_area:
                max_area = area

    if max_area != float('-inf'):
        print("Найбільша площа прямокутника:", max_area)
    else:
        print("Не знайдено дійсних прямокутників")
