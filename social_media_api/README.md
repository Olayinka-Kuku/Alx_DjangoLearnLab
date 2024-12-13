This project provides a simple Django-based API for user registration and authentication. The API includes functionality for registering new users, logging in, and authenticating requests with JSON Web Tokens (JWT). Additionally, a custom user model is used to extend the default Django User model with extra fields.

Table of Contents
Setup Instructions
User Registration
User Authentication
User Model Overview
Setup Instructions
Prerequisites
Before you begin, ensure you have the following installed:

Python (3.x)
Django
Django REST Framework (DRF)
djangorestframework-simplejwt (for JWT authentication)
You can install the required dependencies by running the following command:

bash
Copy code
pip install -r requirements.txt
1. Clone the repository
Clone this repository to your local machine:

bash
Copy code
git clone https://github.com/yourusername/social_media_api.git
cd social_media_api
2. Set up the database
Run the following commands to create the database tables:

bash
Copy code
python manage.py makemigrations
python manage.py migrate
3. Create a superuser
To create an admin user for the Django admin panel, use the following command:

bash
Copy code
python manage.py createsuperuser
Follow the prompts to create the superuser.

4. Start the development server
Once everything is set up, you can start the Django development server with the following command:

bash
Copy code
python manage.py runserver
The API will be available at http://127.0.0.1:8000.

User Registration
1. Registration Endpoint
To register a new user, send a POST request to:

arduino
Copy code
POST /api/auth/register/
2. Request Body
Send the following data in the request body (JSON format):

json
Copy code
{
    "username": "new_user",
    "email": "new_user@example.com",
    "password": "secure_password123",
    "password2": "secure_password123"
}
username: Desired username for the user.
email: The user's email address.
password: The user's chosen password.
password2: A confirmation of the password.
3. Successful Registration Response
If the registration is successful, you will receive a response like this:

json
Copy code
{
    "detail": "User registered successfully."
}
4. Error Responses
If passwords do not match:

json
Copy code
{
    "password2": ["The two password fields didn't match."]
}
If the username already exists:

json
Copy code
{
    "username": ["A user with that username already exists."]
}
User Authentication
1. Login Endpoint
To log in and get a JWT token for authentication, send a POST request to:

bash
Copy code
POST /api/auth/login/
2. Request Body
Send the following data in the request body (JSON format):

json
Copy code
{
    "username": "existing_user",
    "password": "user_password123"
}
username: The username of the user.
password: The user's password.
3. Successful Login Response
On a successful login, you will receive a JWT token:

json
Copy code
{
    "refresh": "your_refresh_token",
    "access": "your_access_token"
}
access: This token is used for making authenticated requests.
refresh: This token can be used to get a new access token when it expires.
4. Using the Token for Authentication
To authenticate subsequent API requests, include the access token in the Authorization header as follows:

makefile
Copy code
Authorization: Bearer <your_access_token>
5. Error Responses
If the credentials are invalid:
json
Copy code
{
    "detail": "No active account found with the given credentials"
}
User Model Overview
This project uses a custom user model that extends Django's AbstractUser class. This custom model allows for additional fields, such as a bio and profile_picture, which are not present in the default User model.

Fields in the Custom User Model:
username (Inherited from AbstractUser): The unique username of the user.
email (Inherited from AbstractUser): The user's email address.
password (Inherited from AbstractUser): The hashed password for the user.
bio: A text field for the user's bio or description.
profile_picture: An image field for the user's profile picture.
followers: A Many-to-Many relationship with the same user model to store the users who are following this user.
following: A Many-to-Many relationship with the same user model to store the users this user is following.
Model Example:
python
Copy code
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)
    following = models.ManyToManyField('self', blank=True, related_name='followers', symmetrical=False)
API Endpoints
User Registration: POST /api/auth/register/
User Login: POST /api/auth/login/
Profile Update: PUT /api/auth/profile/
User List: GET /api/users/ (Admin-only)
