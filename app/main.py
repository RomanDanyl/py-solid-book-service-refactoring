from app.display import ConsoleDisplay, ReverseDisplay, Display
from app.print import ConsolePrinter, ReversePrinter, Printer
from app.serializers import JsonSerializer, XmlSerializer, Serializer


class Book:
    def __init__(
            self,
            title: str,
            content: str,
            display: Display = ConsoleDisplay(),
            printer: Printer = ConsolePrinter(),
            serializer: Serializer = JsonSerializer()
    ):
        self.title = title
        self.content = content
        self.display_service = display
        self.printer_service = printer
        self.serialize_service = serializer

    def display(self) -> None:
        self.display_service.display(self.content)

    def print_book(self) -> None:
        self.printer_service.print(self.title, self.content)

    def serialize(self) -> str:
        return self.serialize_service.serialize(self.title, self.content)


def main(
        book: Book,
        commands: list[tuple[str, str]],
) -> None | str:
    for cmd, method_type in commands:
        try:
            if cmd == "display":
                if method_type == "console":
                    book.display_service = ConsoleDisplay()
                elif method_type == "reverse":
                    book.display_service = ReverseDisplay()
                else:
                    raise ValueError(f"Unknown display type: {method_type}")
                book.display()
            elif cmd == "print":
                if method_type == "console":
                    book.printer_service = ConsolePrinter()
                elif method_type == "reverse":
                    book.printer_service = ReversePrinter()
                else:
                    raise ValueError(f"Unknown printer type: {method_type}")
                book.print_book()
            elif cmd == "serialize":
                if method_type == "json":
                    book.serialize_service = JsonSerializer()
                elif method_type == "xml":
                    book.serialize_service = XmlSerializer()
                else:
                    raise ValueError(f"Unknown serialization type: {method_type}")
                print(book.serialize())
            else:
                raise ValueError(f"Unknown command: {cmd}")
        except ValueError as e:
            print(f"Error: {e}")
    return None


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    result = main(sample_book, [("display", "reverse"), ("serialize", "xml")])
    if result:
        print(result)
