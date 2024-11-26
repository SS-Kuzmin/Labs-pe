class SeaMap:
    def __init__(self):
        # Инициализация карты игры размером 10x10 с точками (пустая карта)
        self.map_size = 10
        self.map = [['.' for _ in range(self.map_size)] for _ in range(self.map_size)]

    def shoot(self, row, col, result):
        # Обработка результата выстрела
        if result == 'miss':
            # Промах: отмечаем клетку '*'
            self.map[row][col] = '*'
        elif result == 'hit':
            # Попадание: отмечаем клетку 'x'
            self.map[row][col] = 'x'
        elif result == 'sink':
            # Потопление: отмечаем клетку 'x' и помечаем клетки вокруг потопленного корабля
            self.map[row][col] = 'x'
            self._mark_sunk_ship(row, col)

    def cell(self, row, col):
        # Возвращает содержимое клетки по заданным координатам
        return self.map[row][col]

    def _mark_sunk_ship(self, row, col):
        # Список координат всех частей потопленного корабля
        ship_cells = [(row, col)]
        self.map[row][col] = 'x'

        # Проверка всех направлений от затопленной клетки
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Вверх, вниз, влево, вправо
        for direction in directions:
            r, c = row + direction[0], col + direction[1]
            # Проверяем, пока не выйдем за границы карты и пока встречаем 'x' (попадание)
            while 0 <= r < self.map_size and 0 <= c < self.map_size and self.map[r][c] == 'x':
                ship_cells.append((r, c))
                r += direction[0]
                c += direction[1]

        # Пометка клеток вокруг потопленного корабля '*'
        for r, c in ship_cells:
            for dr in range(-1, 2):  # -1, 0, 1 (сдвиги по рядам)
                for dc in range(-1, 2):  # -1, 0, 1 (сдвиги по колонкам)
                    nr, nc = r + dr, c + dc
                    # Проверяем, что координаты в пределах карты и что клетка пустая ('.')
                    if 0 <= nr < self.map_size and 0 <= nc < self.map_size and self.map[nr][nc] == '.':
                        self.map[nr][nc] = '*'

# Пример использования класса для проверки
sm = SeaMap()
sm.shoot(2, 0, 'sink')  # Потопленный корабль в клетке (2, 0)
sm.shoot(6, 9, 'hit')   # Попадание в клетку (6, 9)
for row in range(10):
    for col in range(10):
        # Вывод состояния каждой клетки карты
        print(sm.cell(row, col), end='')
    print()  # Новая строка для следующего ряда карты
