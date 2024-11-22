# **Task Manager**

A simple task management web application built with Django. It includes features such as user authentication, task management, sending email invitations, and an admin dashboard.

## **Features**

- User authentication system with login, logout, and sign-up functionality.
- Role-based access (Admin can view all users and delete them).
- Task management: Add, edit, delete tasks.
- Send invitations via email.
- Admin dashboard with user management.
- Google login integration.

## **Technologies Used**

- **Backend**: Django 5.1.3
- **Frontend**: HTML, CSS, Bootstrap 5
- **Database**: SQLite (default)
- **Authentication**: Django's built-in auth system and Google OAuth
- **Deployment**: Localhost (instructions for hosting on platforms like Heroku can be added)

---

## **Installation and Setup**

### Task Manager

A simple task management web application built with Django. It includes features such as user authentication, task management, sending email invitations, and an admin dashboard.

## Features

- User authentication system with login, logout, and sign-up functionality.
- Role-based access (Admin can view all users and delete them).
- Task management: Add, edit, delete tasks.
- Send invitations via email.
- Admin dashboard with user management.
- Google login integration.

## Technologies Used

- **Backend**: Django 5.1.3
- **Frontend**: HTML, CSS, Bootstrap 5
- **Database**: SQLite (default)
- **Authentication**: Django's built-in auth system and Google OAuth
- **Deployment**: Localhost (instructions for hosting on platforms like Heroku can be added)

---

## Installation and Setup

### Prerequisites

1. Python 3.12 or later installed.
2. Git installed.
3. A GitHub repository created to store your project.

---

### Step 1: Clone the Repository

```bash
git clone https://github.com/212khannadeem/task-manager.git
cd task-manager
```

### Step 2: Set Up a Virtual Environment

```bash
python -m venv env
source env/bin/activate    # For macOS/Linux
env\Scripts\activate       # For Windows
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Set Up the Database

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Create a Superuser

```bash
python manage.py createsuperuser
```
Follow the prompts to set the username, email, and password.

### Step 6: Configure Google Login (Optional)

1. Go to the Google Developer Console.
2. Create a new project.
3. Set up OAuth 2.0 credentials.
4. Add http://127.0.0.1:8000/accounts/google/login/callback/ as a redirect URI.
5. Update your settings.py file with the following:
   
```bash
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '<your-client-id>'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '<your-client-secret>'
```

### Step 7: Run the Development Server
Start the Django development server:

```bash
python manage.py runserver
Visit http://127.0.0.1:8000/ in your web browser.
```

# **Usage**

## **For Users:**

1. Sign Up: Register with your email and password.
2. Log In: Access your tasks after logging in.
3. Task Management:
  - Add tasks.
  - Edit existing tasks.
  - Delete tasks
    
## **For Admins**:
  - Admin Dashboard: Access http://127.0.0.1:8000/admin_dashboard/ or Just click on "Go To Admin Dashboard" (login as a superuser).
  - Manage users and tasks.
  - Send invitations via email.

# **Contact**
For any inquiries or issues, contact:

- Name: Nadeem Khan
- Email: nadeemk212000@gmail.com


