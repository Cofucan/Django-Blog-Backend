# Introduction

This is a simple blog application that allows users to create, read, update and delete blog posts and comments. The application is built using the Django web framework and Python 3.12.6. It was developed on a Linux environment, but should work on other operating systems as well.

## Features

- Users can create an account and log in.
- Users can create, read, update and delete blog posts.
- Users can create, read, update and delete comments on blog posts.

## Technologies

- Python
- Django
- SQLite

## Setup

To run this project, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/Cofucan/Django-Blog-Backend.git
    ```

2. Install the project dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Navigate to the project directory:

    ```bash
    cd Django-Blog-Backend
    ```

4. Copy the `.env.example` file to `.env`:

    ```bash
    cp .env.example .env
    ```

5. Update the `.env` file with your database credentials. By default, the project uses SQLite.

6. Run the Django migrations:

    ```bash
    python manage.py migrate
    ```

## Seeding the Database

There is a seed script that seeds some users and superusers to the db. To seed the database, run the following command:

```bash
python manage.py seed_users
```

You should see the status on the terminal. After running the server, you can login to any of the user accounts using the password '12345678`.

## Running the Server

To run the server, execute the following command:

```bash
python manage.py runserver
```

You can also specify the port in case you want to run the server on a different port:

```bash
python manage.py runserver 4000
```

The server should now be running on `http://127.0.0.1:8000/`. If you selected a different port, replace `8000` with the port you selected.

The Swagger documentation is available at `http://127.0.0.1:8000/api/docs`

## Testing

Thix project uses the Pytest framework for testing. To run the tests, execute the following command:

```bash
pytest
```
