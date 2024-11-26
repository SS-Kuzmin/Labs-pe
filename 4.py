class Weapon:
    def __init__(self, name, damage, range):
        # Инициализация параметров оружия: имя, урон, радиус действия
        self.name = name
        self.damage = damage
        self.range = range

    def hit(self, actor, target):
        # Метод для нанесения удара по цели
        if not target.is_alive():
            print("Враг уже повержен")
        else:
            # Вычисление расстояния между актёром и целью
            distance = ((actor.pos_x - target.pos_x) ** 2 + (actor.pos_y - target.pos_y) ** 2) ** 0.5
            if distance > self.range:
                print(f"Враг слишком далеко для оружия {self.name}")
            else:
                print(f"Врагу нанесен урон оружием {self.name} в размере {self.damage}")
                target.get_damage(self.damage)

    def __str__(self):
        # Приведение объекта к строке - возвращает имя оружия
        return self.name


class BaseCharacter:
    def __init__(self, pos_x, pos_y, hp):
        # Инициализация базовых параметров персонажа: позиция и здоровье
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.hp = hp

    def move(self, delta_x, delta_y):
        # Метод для перемещения персонажа
        self.pos_x += delta_x
        self.pos_y += delta_y

    def is_alive(self):
        # Проверка, жив ли персонаж
        return self.hp > 0

    def get_damage(self, amount):
        # Метод для получения урона
        self.hp -= amount
        if self.hp <= 0:
            self.hp = 0

    def get_coords(self):
        # Возвращает текущие координаты персонажа
        return self.pos_x, self.pos_y


class BaseEnemy(BaseCharacter):
    def __init__(self, pos_x, pos_y, weapon, hp):
        # Инициализация врага с базовыми параметрами и оружием
        super().__init__(pos_x, pos_y, hp)
        self.weapon = weapon

    def hit(self, target):
        # Метод для атаки цели
        if not isinstance(target, MainHero):
            print("Могу ударить только Главного героя")
        else:
            self.weapon.hit(self, target)

    def __str__(self):
        # Приведение объекта к строке - возвращает информацию о враге
        return f"Враг на позиции ({self.pos_x}, {self.pos_y}) с оружием {self.weapon}"


class MainHero(BaseCharacter):
    def __init__(self, pos_x, pos_y, name, hp):
        # Инициализация главного героя с базовыми параметрами и именем
        super().__init__(pos_x, pos_y, hp)
        self.name = name
        self.weapons = []
        self.current_weapon_index = -1

    def hit(self, target):
        # Метод для атаки цели
        if not self.weapons:
            print("Я безоружен")
        elif not isinstance(target, BaseEnemy):
            print("Могу ударить только Врага")
        else:
            self.weapons[self.current_weapon_index].hit(self, target)

    def add_weapon(self, weapon):
        # Метод для добавления оружия в инвентарь
        if not isinstance(weapon, Weapon):
            print("Это не оружие")
        else:
            self.weapons.append(weapon)
            print(f"Подобрал {weapon}")
            if len(self.weapons) == 1:
                self.current_weapon_index = 0

    def next_weapon(self):
        # Метод для смены оружия
        if not self.weapons:
            print("Я безоружен")
        elif len(self.weapons) == 1:
            print("У меня только одно оружие")
        else:
            self.current_weapon_index = (self.current_weapon_index + 1) % len(self.weapons)
            print(f"Сменил оружие на {self.weapons[self.current_weapon_index]}")

    def heal(self, amount):
        # Метод для лечения героя
        self.hp += amount
        if self.hp > 200:
            self.hp = 200
        print(f"Полечился, теперь здоровья {self.hp}")


# Пример использования классов для проверки
weapon1 = Weapon("Короткий меч", 5, 1)
weapon2 = Weapon("Длинный меч", 7, 2)
weapon3 = Weapon("Лук", 3, 10)
weapon4 = Weapon("Лазерная орбитальная пушка", 1000, 1000)

# Создание базового персонажа - принцессы
princess = BaseCharacter(100, 100, 100)

# Создание врагов с разным оружием
archer = BaseEnemy(50, 50, weapon3, 100)
armored_swordsman = BaseEnemy(10, 10, weapon2, 500)

# Проверка действий
archer.hit(armored_swordsman)  # Могу ударить только Главного героя
armored_swordsman.move(10, 10)  # Перемещение врага
print(armored_swordsman.get_coords())  # Вывод текущих координат врага

# Создание главного героя
main_hero = MainHero(0, 0, "Король Артур", 200)

# Проверка различных действий главного героя
main_hero.hit(armored_swordsman)  # Я безоружен
main_hero.next_weapon()  # Я безоружен
main_hero.add_weapon(weapon1)  # Подобрал Короткий меч
main_hero.hit(armored_swordsman)  # Враг слишком далеко для оружия Короткий меч
main_hero.add_weapon(weapon4)  # Подобрал Лазерная орбитальная пушка
main_hero.hit(armored_swordsman)  # Враг слишком далеко для оружия Короткий меч
main_hero.next_weapon()  # Сменил оружие на Лазерная орбитальная пушка
main_hero.hit(princess)  # Могу ударить только Врага
main_hero.hit(armored_swordsman)  # Врагу нанесен урон оружием Лазерная орбитальная пушка в размере 1000
main_hero.hit(armored_swordsman)  # Враг уже повержен
