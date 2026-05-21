# 📘 Assignment: Library Management System

## 🎯 Objective

Apply object-oriented design in Python to model a library system that manages books, patrons, and loans.

## 📝 Tasks

### 🛠️ Define Library Classes

#### Description
Create Python classes to represent books, library patrons, and the library itself.

#### Requirements
Completed code should:

- Define a `Book` class with `title`, `author`, `isbn`, and `available` attributes.
- Define a `Patron` class with `name`, `member_id`, and a list of borrowed books.
- Define a `Library` class that stores books and handles loans.

### 🛠️ Add Methods for Borrowing and Returning

#### Description
Implement methods that allow patrons to borrow and return books, and track availability.

#### Requirements
Completed code should:

- Allow a patron to borrow a book only when it is available.
- Mark the book as unavailable when borrowed and available when returned.
- Add or remove the book from the patron's borrowed list.
- Raise an appropriate message or exception when a book cannot be borrowed or returned.

### 🛠️ Demonstrate System Behavior

#### Description
Create a script that simulates library activity and prints the results of borrowing and returning books.

#### Requirements
Completed code should:

- Create at least two books and two patrons.
- Demonstrate a patron borrowing a book and then returning it.
- Print the library status and the patron's borrowed books after each action.
- Example output:

```python
print(book.available)  # False after borrowing
print(patron.borrowed_books)
```
