# OCP
from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name: str, color: Color, size: Size):
        self.name = name
        self.color = color
        self.size = size


class ProductFilter:
    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color:
                yield p

    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size:
                yield p

    def filter_by_color_and_size(self, products, color, size):
        for p in products:
            if p.color == color and p.size == size:
                yield p


# Enterprise Patterns: Specification
class Specification:
    def is_satisfied(self, item):
        pass

    def __and__(self, other):
        return AndSpecification(self, other)


class Filter:
    def filter(self, items, spec):
        pass


class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


class AndSpecification(Specification):
    def __init__(self, spec1, spec2):
        self.spec1 = spec1
        self.spec2 = spec2

    def is_satisfied(self, item):
        return self.spec1.is_satisfied(item) and self.spec2.is_satisfied(item)


class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item


def main():
    apple = Product("Apple", Color.GREEN, Size.SMALL)
    tree = Product("Tree", Color.GREEN, Size.LARGE)
    house = Product("House", Color.BLUE, Size.LARGE)

    products = [apple, tree, house]

    pf = ProductFilter()
    print('Green products (old method):')
    for p in pf.filter_by_color(products, Color.GREEN):
        print(f'{p.name} is green')

    bf = BetterFilter()
    green = ColorSpecification(Color.GREEN)
    print(f'Green products new:')
    for p in bf.filter(products, green):
        print(f'{p.name} is green')

    large = SizeSpecification(Size.LARGE)
    for p in bf.filter(products, large):
        print(f'{p.name} is large')

    print('Large Blue Items:')
    # large_blue = AndSpecification(large, ColorSpecification(Color.BLUE))
    large_blue = large and ColorSpecification(Color.BLUE)  # using __and__
    for p in bf.filter(products, large_blue):
        print(f'{p.name} is large & blue')


if __name__ == '__main__':
    main()
