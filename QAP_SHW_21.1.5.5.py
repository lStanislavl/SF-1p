# При разработке графического редактора вам поручили реализовать класс Triangle,
# в котором инициализатор создает локальные атрибуты a, b, c — длины сторон треугольника.
# Добавьте методы:
# - is_triangle(), который возвращает True, если такой треугольник может существовать
# (если каждая сторона треугольника меньше суммы двух других сторон, значит,
# треугольник существует), и False — в противном случае.
# - get_triangle_area(), который возвращает площадь треугольника (формула Герона), но
# только если такой треугольник существует. Иначе метод должен возвращать значение 0.

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        return self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a

    def get_triangle_area(self):
        if self.is_triangle():
            s = (self.a + self.b + self.c) / 2
            return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5
        else:
            return 0
