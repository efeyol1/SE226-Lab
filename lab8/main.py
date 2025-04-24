from Book import Book
from Article import Article
from Podcast import Podcast
from file_utils import save_to_file, load_from_file

if __name__ == "__main__":
    archive_items = [
        Book("B002", "Clean Code", 2010, "Robert C. Martin", 464),
        Article("A102", "AI in Medicine", 2020, "Science", "10.5678/aimed"),
        Podcast("P302", "History Hour", 2015, "John Smith", 60)
    ]

    filename = "archive.txt"

    save_to_file(archive_items, filename)
    loaded_items = load_from_file(filename)

    print("All Items:")
    for item in loaded_items:
        print(item)

    print("\nRecent Items:")
    for item in loaded_items:
        if item.is_recent(5):
            print(item)

    print("\nArticles with DOI starting '10.1234':")
    for item in loaded_items:
        if isinstance(item, Article) and item.doi.startswith("10.1234"):
            print(item)
