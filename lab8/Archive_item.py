class ArchiveItem:
    def __init__(self, uid, title, year):
        self.uid = uid
        self.title = title
        self.year = int(year)

    def __str__(self):
        return f"UID: {self.uid}, Title: {self.title}, Year: {self.year}"

    def __eq__(self, other):
        return isinstance(other, ArchiveItem) and self.uid == other.uid

    def is_recent(self, n):
        return (2025 - self.year) <= n
