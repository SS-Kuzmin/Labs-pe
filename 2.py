class LeftParagraph:
    def __init__(self, width):
        # Инициализация ширины поля вывода и создание пустого списка для текущей строки
        self.width = width
        self.current_line = []
        self.paragraph = []
    
    def add_word(self, word):
        # Добавление слова в текущую строку
        if sum(len(w) for w in self.current_line) + len(word) + len(self.current_line) <= self.width:
            self.current_line.append(word)
        else:
            # Если текущее слово не помещается, завершение текущей строки и начало новой
            self.paragraph.append(' '.join(self.current_line))
            self.current_line = [word]
    
    def end(self):
        # Завершение текущей строки и добавление её в абзац
        if self.current_line:
            self.paragraph.append(' '.join(self.current_line))
            self.current_line = []
        # Вывод всего абзаца
        for line in self.paragraph:
            print(line)
        # Очистка абзаца для новой порции текста
        self.paragraph = []

class RightParagraph:
    def __init__(self, width):
        # Инициализация ширины поля вывода и создание пустого списка для текущей строки
        self.width = width
        self.current_line = []
        self.paragraph = []
    
    def add_word(self, word):
        # Добавление слова в текущую строку
        if sum(len(w) for w in self.current_line) + len(word) + len(self.current_line) <= self.width:
            self.current_line.append(word)
        else:
            # Если текущее слово не помещается, завершение текущей строки и начало новой
            line = ' '.join(self.current_line)
            self.paragraph.append(line.rjust(self.width))
            self.current_line = [word]
    
    def end(self):
        # Завершение текущей строки и добавление её в абзац
        if self.current_line:
            line = ' '.join(self.current_line)
            self.paragraph.append(line.rjust(self.width))
            self.current_line = []
        # Вывод всего абзаца
        for line in self.paragraph:
            print(line)
        # Очистка абзаца для новой порции текста
        self.paragraph = []

# Пример использования классов для проверки
lp = LeftParagraph(8)
lp.add_word('abc')
lp.add_word('defg')
lp.add_word('hi')
lp.add_word('jklmnopq')
lp.add_word('r')
lp.add_word('stuv')
lp.end()
print()

rp = RightParagraph(8)
rp.add_word('abc')
rp.add_word('defg')
rp.add_word('hi')
rp.add_word('jklmnopq')
rp.add_word('r')
rp.add_word('stuv')
rp.end()
print()
