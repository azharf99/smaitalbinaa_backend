# SMA IT Al-Binaa - Backend Service

![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)
![GitHub stars](https://img.shields.io/github/stars/your-username/smaitalbinaa_backend.svg)

This repository contains the backend source code for the SMA IT Al-Binaa application. This service is responsible for handling all the core logic, data management, and API endpoints for the school's digital platform.

## 🌟 Features

-   **User Management:** Secure registration and authentication for students, teachers, and admins.
-   **Student Information System:** Manage student profiles, grades, and attendance.
-   **Class & Schedule Management:** Create and manage classes, subjects, and timetables.
-   **Announcements:** A system for posting and viewing school-wide announcements.
-   **RESTful API:** A well-structured API for client applications (e.g., web or mobile) to interact with.

## 🛠️ Tech Stack

-   **Backend:** Node.js, Express.js
-   **Database:** MongoDB with Mongoose ODM
-   **Authentication:** JSON Web Tokens (JWT)
-   **Testing:** Jest, Supertest
-   **Other:** Dotenv for environment variables, Bcrypt for password hashing

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Make sure you have the following installed on your machine:
-   [Node.js](https://nodejs.org/en/) (v18.x or later recommended)
-   [npm](https://www.npmjs.com/) (comes with Node.js)
-   [MongoDB](https://www.mongodb.com/try/download/community) (or a MongoDB Atlas account)

### Installation

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/your-username/smaitalbinaa_backend.git
    cd smaitalbinaa_backend
    ```

2.  **Install dependencies:**
    ```sh
    npm install
    ```

3.  **Set up environment variables:**
    Create a `.env` file in the root of the project by copying the example file:
    ```sh
    cp .env.example .env
    ```
    Now, open the `.env` file and fill in the required values:
    ```env
    # Server Configuration
    PORT=5000

    # MongoDB Connection
    MONGO_URI=mongodb://localhost:27017/smaitalbinaa

    # JWT Secret for Authentication
    JWT_SECRET=your_super_secret_jwt_key
    JWT_EXPIRES_IN=30d
    ```

### Running the Application

1.  **Start the development server:**
    ```sh
    npm run dev
    ```
    The server will start on the port you specified in your `.env` file (e.g., `http://localhost:5000`).

2.  **Run in production mode:**
    ```sh
    npm start
    ```

## 🧪 Running Tests

To run the automated tests for the API endpoints, use the following command:

```sh
npm test
```