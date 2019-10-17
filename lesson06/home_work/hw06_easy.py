# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.


import math

class Triangle ():
    def __init__(self, xa, ya, xb, yb, xc, yc):
        self.xa = xa
        self.ya = ya
        self.xb = xb
        self.yb = yb
        self.xc = xc
        self.yc = yc
        self.AB_Side = round(math.sqrt(int (math.fabs(((yb - ya)**2) + ((xb - xa)**2)))),2)
        self.BC_Side = round(math.sqrt(int(math.fabs(((yc - yb) ** 2) + ((xc - xb) ** 2)))), 2)
        self.CA_Side = round(math.sqrt(int(math.fabs(((ya - yc) ** 2) + ((xa - xc) ** 2)))), 2)

    def perimetr(self):
        self.perimetr = (self.AB_Side + self.BC_Side + self.CA_Side)
        return (self.perimetr)

    def area(self):
        self.perimetr /=2
        self.area =  round(math.sqrt(self.perimetr*(self.perimetr - self.AB_Side)*(self.perimetr - self.BC_Side)* (self.perimetr - self.CA_Side)),2)
        return (self.area)

    def height(self):
        self.area *=2
        self.height =  round((self.area / self.CA_Side),2)
        return (self.height)


#test_triangle = Triangle(5,5,8,11,10,7)
#print('АВ = {}, ВС = {}, СА = {}'.format(test_triangle.AB_Side, test_triangle.BC_Side, test_triangle.CA_Side))
#print('Периметр АВС равен {}'.format(test_triangle.perimetr()))
#print('Площадь АВС равна {}'.format(test_triangle.area()))
#print('Высота равна {}'.format(test_triangle.height()))

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Side:
    def _length(self, p1: Point, p2: Point):
        return math.sqrt(math.pow(p1.x - p2.x, 2) + math.pow(p1.y - p2.y, 2))


class Trapezoid(Side):
    def __init__(self, p1: Point, p2: Point, p3: Point, p4: Point):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        self.AB = self._length(p1, p2)
        self.BC = self._length(p2, p3)
        self.CD = self._length(p3, p4)
        self.DA = self._length(p4, p1)
        self.height_trap = None

    def Side_AB(self):
        return self.AB

    def Side_BC(self):
        return self.BC

    def Side_CD(self):
        return self.CD

    def Side_DA(self):
        return self.DA

    def height_Trapezoid(self):
        if self.AB == self.CD:
            self.height_trap = self.p2.y - self.p1.y
        else:
            self.height_trap = self.p3.y - self.p2.y
        return self.height_trap

    def perimeter_Trapezoid(self):
        return self.AB + self.BC + self.CD + self.DA

    def area_Trapezoid(self):
        if self.AB == self.CD:
            area = self.height_trap * (self.BC + self.DA) / 2
        else:
            area = self.height_trap * (self.AB + self.CD) / 2
        return area

    def check_Trapezoid(self) -> bool:
        return bool(self.AB == self.CD and (self.p4.x - self.p1.x) / self.DA == (self.p3.x - self.p2.x) / self.BC or (
                self.BC == self.DA and (self.p2.x - self.p1) / self.AB == (self.p3.x - self.p4.x) / self.CD) or (
                            self.AB == self.CD and self.BC == self.DA))

#test_trapezoid = Trapezoid(Point (0, 0), Point(2, 4), Point(6, 4), Point(8, 0))
#if test_trapezoid.check_Trapezoid() == True:
#    print('Трапеция равнобедренная')
#    print('AB = {}, BC = {}, CD = {}, DA = {}'.format(test_trapezoid.Side_AB(), test_trapezoid.Side_BC(), test_trapezoid.Side_CD(), test_trapezoid.Side_DA()))
#    print('Высота трапеции равна = {}'.format(test_trapezoid.height_Trapezoid()))
#    print('Периметр = {}'.format(test_trapezoid.perimeter_Trapezoid()))
#    print('Площадь = {}'.format(test_trapezoid.area_Trapezoid()))
#else:
#    print('Трапеция неравнобедренная')