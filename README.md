# SMA IT Al-Binaa - Backend Service

![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)

This repository contains the backend source code for the SMA IT Al-Binaa application. This service is responsible for handling all the core logic, data management, and API endpoints for the school's digital platform.

## 🌟 Features

-   **User Management:** Secure registration and authentication for students, teachers, and admins.
-   **Student Information System:** Manage student profiles, class reports, and achievements.
-   **Class & Schedule Management:** Create and manage classes, subjects, and timetables.
-   **News & Announcements:** A system for posting and viewing school-wide news and announcements.
-   **RESTful API:** A well-structured API for client applications (e.g., web or mobile) to interact with.

## 🛠️ Tech Stack

-   **Backend:** Django, Django REST Framework
-   **Database:** MySQL
-   **Authentication:** Simple JWT, Social Auth (Google, Facebook)
-   **Containerization:** Docker, Docker Compose
-   **Other:** Gunicorn, CKEditor

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
Make sure you have the following installed on your machine:
-   [Python](https://www.python.org/downloads/) (3.10 or later)
-   [Pip](https://pip.pypa.io/en/stable/installation/)
-   [Docker](https://www.docker.com/products/docker-desktop/)
-   [Docker Compose](https://docs.docker.com/compose/install/)

### Installation

1.  **Clone the repository:**
    ```sh
    git clone <your-repo-url>
    cd smaitalbinaa_backend
    ```

2.  **Create a `requirements.txt` file:**
    If you don't have one, create it from your virtual environment.
    ```sh
    pip freeze > requirements.txt
    ```

3.  **Set up environment variables:**
    Create a `.env` file in the root of the project. You can copy the structure from your existing setup. For Docker, ensure you have these variables set:
    ```env
    # Django
    SECRET_KEY=your_super_secret_django_key
    DEBUG=True
    
    # Database for Docker
    LOCAL_MYSQL_DB_NAME=smait_db
    LOCAL_MYSQL_DB_USER=smait_user
    LOCAL_MYSQL_DB_PASSWORD=your_db_password
    LOCAL_MYSQL_ROOT_PASSWORD=your_db_root_password
    LOCAL_MYSQL_DB_HOST=db  # <-- This should be the service name from docker-compose.yml
    LOCAL_MYSQL_DB_PORT=3306

    # Frontend Host
    MY_FRONTEND_HOST=http://localhost:5173
    ```

### Running the Application with Docker

1.  **Build and run the containers:**
    ```sh
    docker-compose up --build -d
    ```
    The backend will be available at `http://localhost:8000`.

2.  **Apply database migrations:**
    Run this command in a separate terminal.
    ```sh
    docker-compose exec backend python manage.py migrate
    ```

3.  **Create a superuser (optional):**
    ```sh
    docker-compose exec backend python manage.py createsuperuser
    ```

4.  **Stopping the application:**
    ```sh
    docker-compose down
    ```