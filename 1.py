class Rectangle:
    def __init__(self, x, y, w, h):
        # Инициализация атрибутов прямоугольника
        self._x = x
        self._y = y
        self._w = w
        self._h = h
    
    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y
    
    def get_w(self):
        return self._w
    
    def get_h(self):
        return self._h
    
    def intersection(self, other):
        # Вычисление координат левого нижнего и правого верхнего углов пересечения
        x1 = max(self._x, other.get_x())
        y1 = max(self._y, other.get_y())
        x2 = min(self._x + self._w, other.get_x() + other.get_w())
        y2 = min(self._y + self._h, other.get_y() + other.get_h())
        
        # Проверка на пересечение (если пересечение существует)
        if x1 < x2 and y1 < y2:
            return Rectangle(x1, y1, x2 - x1, y2 - y1)
        else:
            return None

# Пример использования класса для проверки
rect1 = Rectangle(0, 0, 10, 10)
rect2 = Rectangle(10, 0, 10, 10)
rect3 = rect1.intersection(rect2)

if rect3 is None:
    print('No intersection')
else:
    print(rect3.get_x(), rect3.get_y(), rect3.get_w(), rect3.get_h())
