from django.urls import path
from .views import list_books, LibraryDetailView, views, LoginView, LogoutView

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', views.register, name='register'),  # Registration page
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),  # Login page
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),  # Logout page
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
    path('add/', views.add_book, name='add_book/'),
    path('edit/<int:book_id>/', views.edit_book, name='edit_book/'),
    path('delete/<int:book_id>/', views.delete_book, name='delete_book/'),
]
