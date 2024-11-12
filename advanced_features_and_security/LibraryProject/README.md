#Library Project

This is a Django Project

## Permissions and Groups Setup

- **Groups:**
  - **Viewer**: Can only view books (`can_view` permission).
  - **Editor**: Can view, create, and edit books (`can_view`, `can_create`, `can_edit` permissions).
  - **Admin**: Can view, create, edit, and delete books (`can_view`, `can_create`, `can_edit`, `can_delete` permissions).

- **Permissions:**
  - **can_view**: Permission to view a book.
  - **can_create**: Permission to create a new book.
  - **can_edit**: Permission to edit an existing book.
  - **can_delete**: Permission to delete a book.
