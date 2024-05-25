class Node:
    def accept(self, visitor):
        visitor.visit(self)

class City(Node):
    def __init__(self, name):
        self.name = name

class Industry(Node):
    def __init__(self, name):
        self.name = name
class Visitor:
    def visit(self, city):
        print(f"Visiting city: {city.name}")

    def visit(self, industry):
        print(f"Visiting industry: {industry.name}")
if __name__ == "__main__":
    # Создание узлов графа
    city = City("Moscow")
    industry = Industry("Yandex")

    # Создание посетителя
    visitor = Visitor()

    # Посещение узлов
    city.accept(visitor)
    industry.accept(visitor)
