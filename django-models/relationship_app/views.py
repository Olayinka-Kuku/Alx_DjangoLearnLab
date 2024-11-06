from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views import views
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from .models import UserProfile
from django.contrib.auth.decorators import user_passes_test

# View for Admin users
@user_passes_test(lambda user: user.userprofile.role == 'Admin')
def admin_view(request):
    return render(request, 'admin_view.html')

# View for Librarian users
@user_passes_test(lambda user: user.userprofile.role == 'Librarian')
def librarian_view(request):
    return render(request, 'librarian_view.html')

# View for Member users
@user_passes_test(lambda user: user.userprofile.role == 'Member')
def member_view(request):
    return render(request, 'member_view.html')

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # Fetch all books from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})  # Render the template with books

# Class-based view for library details using DetailView
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# Register view (function-based)
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Login view
class LoginView(views):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'relationship_app/login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Adjust this as needed
        return render(request, 'relationship_app/login.html', {'form': form})

# LogoutView (class-based)
class LogoutView(views):
    def get(self, request):
        logout(request)
        return redirect('login')  # Redirect to login after logout

