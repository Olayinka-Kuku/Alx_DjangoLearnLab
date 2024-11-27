# Advanced API Project - CRUD Views for Books

## Book Views

### 1. **List Books (`GET /api/books/`)**
- Retrieves a list of all books in the system.
- Available to both authenticated and unauthenticated users.

### 2. **Retrieve Single Book (`GET /api/books/<id>/`)**
- Retrieves details of a specific book by its ID.
- Available to both authenticated and unauthenticated users.

### 3. **Create Book (`POST /api/books/create/`)**
- Allows authenticated users to create a new book.

### 4. **Update Book (`PUT /api/books/<id>/update/`)**
- Allows authenticated users to update an existing book.

### 5. **Delete Book (`DELETE /api/books/<id>/delete/`)**
- Allows authenticated users to delete a book.

## Book API - Filtering, Searching, and Ordering

### Filtering
- You can filter books by the following fields:
  - `title`
  - `author`
  - `publication_year`
- Example:
  - `GET /api/books/?title=Book Title`
  - `GET /api/books/?author=Author Name`
  - `GET /api/books/?publication_year=2021`

### Searching
- You can search books by `title` and `author`.
- Example:
  - `GET /api/books/?search=Django`

### Ordering
- You can order books by `title` and `publication_year`.
- Example:
  - `GET /api/books/?ordering=title`
  - `GET /api/books/?ordering=-publication_year` (reversed order)
