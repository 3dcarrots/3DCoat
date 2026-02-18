import random

class MyObject:
    def __init__(self, base_value):
        self.base_value = base_value
        print(f"Объект создан с базовым значением: {self.base_value}")

    @property
    def dynamic_list(self):
        """
        Этот метод будет вызываться КАЖДЫЙ раз при обращении 
        к 'obj.dynamic_list'.
        """
        print(">>> Генерирую новый список...")
        # Процедурная генерация:
        # создаем список на основе base_value + случайное число
        return [
            f"Sub-object {i + self.base_value + random.randint(0, 5)}" 
            for i in range(3)
        ]

# --- Демонстрация ---

# 1. Создаем объект
obj = MyObject(10)

# 2. Первое обращение к свойству
print("\n--- Первое обращение:")
my_list_1 = obj.dynamic_list
print(my_list_1)

# 3. Второе обращение к свойству
print("\n--- Второе обращение (список будет другим):")
my_list_2 = obj.dynamic_list
print(my_list_2)

# 4. Изменим внутреннее состояние объекта
obj.base_value = 100

# 5. Третье обращение (список снова генерируется, уже на основе нового base_value)
print("\n--- Третье обращение после изменения base_value:")
my_list_3 = obj.dynamic_list
print(my_list_3)