class DefaultList(list):
    def __init__(self, default_value):
        self.default_value = default_value
        super().__init__()

    def __getitem__(self, index):
        try:
            return super().__getitem__(index)
        except IndexError:
            return self.default_value

# Пример использования
my_list = DefaultList(default_value=0)
my_list.append(1)
my_list.append(2)

print(my_list[0])  # Вывод: 1
print(my_list[1])  # Вывод: 2
print(my_list[2])  # Вывод: 0 (значение по умолчанию)
print(my_list[100])  # Вывод: 0 (значение по умолчанию)