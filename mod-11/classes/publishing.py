from abc import ABC, abstractmethod

class Publishing(ABC):
    def __init__(self, name: str):
        self.name = name

    def print_info(self):
        print(f"Publishing Name: {self.name}")


class Book(Publishing):
    def __init__(self, name: str, author: str, page_count: int):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_info(self):
        print(f"Book: {self.name}")
        print(f"Author: {self.author}")
        print(f"Page Count: {self.page_count}")


class Magazine(Publishing):
    def __init__(self, name: str, director: str):
        super().__init__(name)
        self.director = director

    def print_info(self):
        print(f"Magazine: {self.name}")
        print(f"Director: {self.director}")