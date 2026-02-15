from models import Book
from services import (
    ConsoleDisplay,
    ReverseDisplay,
    JsonSerializer,
    XmlSerializer,
)
from validators import BookValidator


def main():
    book = Book("Sample", "Some content")
    BookValidator.validate(book)

    display = ReverseDisplay()
    display.display(book)

    serializer = XmlSerializer()
    print(serializer.serialize(book))


if __name__ == "__main__":
    main()
