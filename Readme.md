Task Manager with Google Login
Overview
This is a basic web application built using Django that allows users to manage their personal tasks after logging in with their Google account. The app includes the following features:

Google Login for user authentication.
CRUD operations for task management.
Admin panel to manage Google OAuth keys and invite new users.
Features
Google Authentication

Users can log in securely using their Google account.
Task Management

Users can create, view, edit, and delete tasks.
Each task includes a title and description.
Tasks are private to the logged-in user.
Admin Panel

Admins can manage Google OAuth keys.
Admins can send email invitations to invite new users.
Getting Started
Prerequisites
Python 3.8 or higher
Django 4.0 or higher
Google Cloud account to set up OAuth credentials
Setup Instructions
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/task-manager.git
cd task-manager
Create a virtual environment and activate it:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Set up the database:

bash
Copy code
python manage.py migrate
Configure Google OAuth:

Go to the Google Cloud Console.
Enable the "OAuth Consent Screen" and set up credentials for a web application.
Add the redirect URI: http://127.0.0.1:8000/accounts/google/login/callback/.
Add your Google client ID and secret to settings.py:
python
Copy code
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': 'your-google-client-id',
            'secret': 'your-google-client-secret',
            'key': ''
        }
    }
}
Run the development server:

bash
Copy code
python manage.py runserver
Access the app at http://127.0.0.1:8000.

