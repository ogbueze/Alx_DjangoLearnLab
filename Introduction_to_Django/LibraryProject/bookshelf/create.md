# CREATE Operation

## Python Command

```python
from books.models import Book

book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)
book.save()
book
```
