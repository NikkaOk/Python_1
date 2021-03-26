import random

PI = 3.14

class Circle:
    def __init__(self, r):
        self.r = r

    def diameter(self):
        return self.r * 2

    def area(self):
        return PI * (self.r ** 2)

    def lenght(self):
        return PI * 2 * self.r

    def info(self):
        return f'Radius - {self.r}, Area - {self.area()}, Lenght - {self.lenght()}'



def create_circles(n):
    result = []

    for i in range(n):
        tmp = Circle(random.randint(0, 10 ** 5))
        result.append(tmp)

    return result


if __name__ == '__main__':
    my_circles = create_circles(10)

    max_circle = my_circles[0]
    min_circle = my_circles[0]

    # for circle in my_circles:
    #     if circle.area() > max_circle.area():
    #         max_circle = circle
    #     if circle.area() < min_circle.area():
    #         min_circle = circle
    # print(max_circle.info())
    # print(min_circle.info())

    max_circle = max(my_circles, key= lambda c:c.area())
    print(max_circle.info())
    min_circle = min(my_circles, key=lambda c: c.area())
    print(min_circle.info())
