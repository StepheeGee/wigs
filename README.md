# Django REST Framework & Docker - Class 31

## Project: Wigs

## Author: Stephanie G. Johnson

**Date**: 2.19.24

### Description

The Wigs project is a Django REST Framework application designed to manage information about wigs. This includes details such as wig name, color, length, curl pattern, density, hair origin, description, and price. The project utilizes Docker for containerization, making it easy to deploy and manage the application in various environments.

### Requirements

- Docker: The project uses Docker for containerization, allowing for consistent and reproducible deployments.
- Django: A high-level Python web framework used to build the backend of the Wigs project.
- Django REST Framework: A powerful and flexible toolkit for building Web APIs in Django.

### Features

- Django Models: The project defines a `Wig` model to represent the data structure for wig information.
- RESTful API: The application provides a RESTful API for performing CRUD operations on wig data.
- Dockerized: The project is containerized using Docker, simplifying deployment and ensuring consistency across different environments.

### Links and Resources

- [Django Documentation](https://docs.djangoproject.com/): Official documentation for the Django web framework.
- [Django REST Framework Documentation](https://www.django-rest-framework.org/): Documentation for the Django REST Framework.
- [Docker Documentation](https://docs.docker.com/): Official documentation for Docker, the containerization platform.


### Setup

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/stephegee/wigs.git
    cd wigs
    ```

2. **Install Dependencies:**

    ```bash
    # Install Docker (follow the instructions for your OS)
    # Install Docker Compose (follow the instructions for your OS)
    ```

3. **Configure Environment Variables:**

    Create a `.env` file in the project root and define the required environment variables:

    ```env
    # Example .env file
    PORT=8000
    DATABASE_URL=your_database_url
    ```

4. **Build and Run Docker Container:**

    ```bash
    docker-compose up --build
    ```

5. **Run Migrations:**

    ```bash
    docker-compose exec web python manage.py makemigrations
    docker-compose exec web python manage.py migrate
    ```

6. **Access the API:**

    The API should be accessible at [http://localhost:8000/api/](http://localhost:8000/api/).

### Tests

To run tests for the Wigs project, use the following command:

```bash
docker-compose exec web python manage.py test mywigs
```

This command will execute the test suite and provide information about any failures or errors. Ensure that the application is running and the necessary dependencies are installed before running the tests.

### Additional Resources

- [Django for Beginners](https://djangoforbeginners.com/): A comprehensive beginner-friendly guide to Django.
- [Django REST Framework Tutorial](https://www.django-rest-framework.org/tutorial/quickstart/): Quickstart guide for Django REST Framework.
- [Dockerizing Django with Postgres, Gunicorn, and Nginx](https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/): A tutorial on Dockerizing a Django application with Postgres, Gunicorn, and Nginx.

## Thank You