---

### **Contents of `CRUD_operations.md`**

````markdown
# File: CRUD_operations.md

# CRUD Operations in Django Shell

## CREATE

```python
Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)

## RETRIEVE
book = Book.objects.get(title="1984")
book.title, book.author, book.publication_year

# UPDATE
book.title = "Nineteen Eighty-Four"
book.save()

#DELET
book.delete()
Book.objects.all()
```
````
