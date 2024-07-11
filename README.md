# Attendance System

This is a simple attendance management system for a school, built with Django for the backend and React for the frontend.

## Project Setup

### Prerequisites

- Python 
- Node.js
- npm
- Git

### Server (Django)

1. Navigate to the `server` folder:
    ```bash
    cd server
    ```
2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```
3. Install the required dependencies:
    ```bash
    pip install django djangorestframework djangorestframework-simplejwt
    ```
4. Run the migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
5. Start the server:
    ```bash
    python manage.py runserver
    ```



## Technologies Used

- **Frontend:** React
- **Backend:** Django REST Framework
- **Database:** SQLite (default for Django)
- **State Management:** React Hooks
- **HTTP Client:** Axios
- **Authentication:** JWT (JSON Web Tokens)


### Client (React)

1. Navigate to the `client/attendance-client` folder:
    ```bash
    cd client/attendance-client
    ```
2. Install the required dependencies:
    ```bash
    npm install
    ```
3. Start the client:
    ```bash
    npm start
    ```

### Folder Structure

The project is structured as follows:


attendance-system/
├── client/
│   ├── public/
│   │   ├── index.html
│   │   └── ...
│   ├── src/
│   │   ├── components/
│   │   │   ├── Login.js
│   │   │   └── Home.js
│   │   ├── api/
│   │   │   └── api.js
│   │   ├── App.js
│   │   ├── index.js
│   │   └── ...
├── server/
│   ├── attendance_server/
│   │   ├── authentication/
│   │   │   ├── migrations/
│   │   │   ├── templates/
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py
│   │   │   ├── tests.py
│   │   │   ├── urls.py
│   │   │   └── views.py
│   │   ├── attendance_system/
│   │   │   ├── settings.py
│   │   │   ├── urls.py
│   │   │   └── wsgi.py
│   │   ├── manage.py
│   │   └── requirements.txt
│   └── docs/
│       └── screenshots/
└── README.md




### Login Credentials for Testing

Use the following credentials to log in:
- Username: `andrew`
- Password: `1234`
- email: sandrew022000@gmail.com

### Screenshots

Add any relevant screenshots in the `docs` folder. Make sure to label them appropriately with the respective task number for easy reference.

## Commit Messages

As you progress through the tasks, commit your changes to the repository on GitHub. Each commit should correspond to a specific task number and include a descriptive message following the convention:

