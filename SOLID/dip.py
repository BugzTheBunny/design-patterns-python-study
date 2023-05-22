# DIP - Dependency Inversion Principle
from abc import abstractmethod
from enum import Enum


class Relationship(Enum):
    PARTEN = 0
    CHILD = 1
    SIBLING = 2


class Person:
    def __init__(self, name):
        self.name = name


class RelationshipBrowser:
    @abstractmethod
    def find_all_children_of(self, name): pass


class Relationships(RelationshipBrowser):

    def __init__(self):
        self.relations = []

    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARTEN:
                yield r[2].name

    def add_parent_and_child(self, parent, child):
        self.relations.append(
            (parent, Relationship.PARTEN, child)
        )
        self.relations.append(
            (child, Relationship.CHILD, parent)
        )


class Research:
    def __init__(self, browser):
        for p in browser.find_all_children_of('John'):
            print(f"John has a child called {p}")


parent_ = Person("John")
child1 = Person("Chris")
child2 = Person("Matt")

relationships_ = Relationships()
relationships_.add_parent_and_child(parent_, child1)
relationships_.add_parent_and_child(parent_, child2)
Research(relationships_)

