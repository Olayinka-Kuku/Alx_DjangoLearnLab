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

# Security Settings Documentation

## HTTPS Configuration
- `SECURE_SSL_REDIRECT`: Ensures that all HTTP requests are redirected to HTTPS.
- `SECURE_HSTS_SECONDS`: Specifies how long browsers should only access the site via HTTPS.
- `SECURE_HSTS_INCLUDE_SUBDOMAINS`: Applies HSTS to all subdomains.
- `SECURE_HSTS_PRELOAD`: Allows the site to be preloaded into browsers for strict HTTPS enforcement.

## Secure Cookies
- `SESSION_COOKIE_SECURE`: Ensures that session cookies are only sent over HTTPS.
- `CSRF_COOKIE_SECURE`: Ensures that CSRF cookies are only sent over HTTPS.

## Security Headers
- `X_FRAME_OPTIONS`: Protects against clickjacking by preventing the site from being framed.
- `SECURE_CONTENT_TYPE_NOSNIFF`: Prevents browsers from MIME-sniffing a response away from the declared content-type.
- `SECURE_BROWSER_XSS_FILTER`: Enables browser XSS filtering for protection against cross-site scripting attacks.

## Deployment Configuration
- Ensure that SSL/TLS certificates are installed for your domain.
- Configure Nginx or Apache to serve your site over HTTPS and redirect HTTP traffic to HTTPS.

## Testing
- Test that all HTTP traffic is redirected to HTTPS.
- Test secure cookies by verifying that cookies are only sent over HTTPS connections.
