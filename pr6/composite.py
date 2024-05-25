class Component(object):
    def operation(self):
        pass


class Leaf(Component):
    def operation(self):
        pass


class Composite(Component):
    def __init__(self):
        self.children = []

    def add(self, leaf):
        self.children.append(leaf)

    def remove(self, leaf):
        self.children.remove(leaf)

    def operation(self):
        for child in self.children:
            child.operation()


class Button(Leaf):
    def operation(self):
        print("Кнопка")


class TextField(Leaf):
    def operation(self):
        print("Текстовое поле")


class Label(Leaf):
    def operation(self):
        print("Метка")


if __name__ == "__main__":
    root = Composite()
    root.add(Button())
    root.add(TextField())
    root.add(Label())

    root.operation()
