from Book import Book
from Article import Article
from Podcast import Podcast

def save_to_file(items, filename):
    with open(filename, 'w') as file:
        for item in items:
            if isinstance(item, Book):
                file.write(f"Book,{item.uid},{item.title},{item.year},{item.author},{item.pages}\n")
            elif isinstance(item, Article):
                file.write(f"Article,{item.uid},{item.title},{item.year},{item.journal},{item.doi}\n")
            elif isinstance(item, Podcast):
                file.write(f"Podcast,{item.uid},{item.title},{item.year},{item.host},{item.duration}\n")

def load_from_file(filename):
    items = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            type_ = parts[0]
            if type_ == 'Book':
                _, uid, title, year, author, pages = parts
                items.append(Book(uid, title, year, author, pages))
            elif type_ == 'Article':
                _, uid, title, year, journal, doi = parts
                items.append(Article(uid, title, year, journal, doi))
            elif type_ == 'Podcast':
                _, uid, title, year, host, duration = parts
                items.append(Podcast(uid, title, year, host, duration))
    return items
