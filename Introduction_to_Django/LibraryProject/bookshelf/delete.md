---

### **File: `delete.md`**

````markdown
# File: delete.md

# DELETE Operation

```python
from books.models import Book

book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

Book.objects.all()
```
````
