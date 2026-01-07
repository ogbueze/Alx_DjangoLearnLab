---

### **File: `update.md`**

````markdown
# File: update.md

# UPDATE Operation

```python
from books.models import Book

book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

book
```
````
