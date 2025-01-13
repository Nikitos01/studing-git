class Book(object):
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return (f"Название книги: {self.title}\n"
                f"Автор: {self.author}"
                f"Год издания: {self.title}")


"""
class Circle(object):
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if not isinstance(value, int) and value >= 0:
            raise Exception("")
        self._radius = value"""

class Circle(object):
    def __init__(self, radius):
        self._radius = radius

    def get_radius(self):
        return self._radius

    def set_radius(self, value):
        self._radius = value


def main() -> None:
    circle = Circle(10)
    circle.set_radius(20)
    print(circle.get_radius())


if  __name__ == "__name__":
    main()
