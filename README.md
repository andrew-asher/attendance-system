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
### Description

- **client/**: Contains the frontend application files.
- **server/**: Contains the backend Django server files.
- **docs/**: Includes documentation files and screenshots.

### Login Credentials for Testing

Use the following credentials to log in:
- Username: `andrew`
- Password: `1234`
- email: sandrew022000@gmail.com


