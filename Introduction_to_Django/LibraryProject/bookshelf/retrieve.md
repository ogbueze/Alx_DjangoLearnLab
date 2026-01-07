---

### **File: `retrieve.md`**

````markdown
# File: retrieve.md

# RETRIEVE Operation

```python
from books.models import Book

book = Book.objects.get(title="1984")
book.title, book.author, book.publication_year
```
````
