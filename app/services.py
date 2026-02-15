from abc import ABC, abstractmethod
from models import Book
import json
import xml.etree.ElementTree as element_tree


class DisplayStrategy(ABC):
    @abstractmethod
    def display(self, book: Book) -> None:
        pass


class ConsoleDisplay(DisplayStrategy):
    def display(self, book: Book) -> None:
        print(book.content)


class ReverseDisplay(DisplayStrategy):
    def display(self, book: Book) -> None:
        print(book.content[::-1])


class PrintStrategy(ABC):
    @abstractmethod
    def print_book(self, book: Book) -> None:
        pass


class ConsolePrint(PrintStrategy):
    def print_book(self, book: Book) -> None:
        print(f"Printing the book: {book.title}...")
        print(book.content)


class ReversePrint(PrintStrategy):
    def print_book(self, book: Book) -> None:
        print(f"Printing in reverse: {book.title}...")
        print(book.content[::-1])


class Serializer(ABC):
    @abstractmethod
    def serialize(self, book: Book) -> str:
        pass


class JsonSerializer(Serializer):
    def serialize(self, book: Book) -> str:
        return json.dumps({"title": book.title, "content": book.content})


class XmlSerializer(Serializer):
    def serialize(self, book: Book) -> str:
        root = element_tree.Element("book")
        title = element_tree.SubElement(root, "title")
        title.text = book.title
        content = element_tree.SubElement(root, "content")
        content.text = book.content
        return element_tree.tostring(root, encoding="unicode")
