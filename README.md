
# Listed & Lifted Backend API


Welcome to the backend repository of Listed & Lifted, your premier online marketplace built with Django Rest Framework. This repository contains the codebase for the RESTful API that powers the backend functionality of the Shortlisted platform.
## Features

- **User Authentication:** Secure user authentication using Django's token-based authentication for accessing API endpoints.
- **Product Listings:** CRUD (Create, Read, Update, Delete) operations for managing product listings. Users can create, read, and update their product listings, but they cannot delete the products they have listed.
- **User Management:** Endpoint for managing user profiles, including registration, login, and updating user information.
- **Order Management:** Endpoint for creating and managing purchasing products.
- **Reviews:** API endpoint for users to leave reviews for products.
- **Filtering:** Implement filtering functionality for product listings.

## Getting Started

1. Clone Repository: Clone this repository to your local machine using git clone https://github.com/Tahsin005/Shortlisted

2. Install Dependencies: Navigate to the project directory and install the required dependencies using pip install -r requirements.txt.

3. Database Setup: Configure your database settings in the settings.py file. By default, the project is configured to use PostgreSQL, but you can change it to use SQLite or MySQL as per your preference.

4. Migrations: Run database migrations to create the necessary database schema using python manage.py migrate.

5. Create Superuser: Create a superuser account to access the Django admin panel and manage users and product listings using python manage.py createsuperuser.

6. Run Server: Start the Django development server using python manage.py runserver.

7. Explore API Endpoints: Explore the available API endpoints by navigating to http://127.0.0.1:8000/ in your web browser or API client.
## Technology used



**Backend:** Django REST API, PostgreSQL


## Documentation

[Documentation](https://docs.google.com/document/d/1T4xksYexwfVn3DL_4BhjQ74RO2jSyqf8FNJl_0ZwBBM/edit?usp=sharing)


## Live Link

https://shortlisted.vercel.app/index.html

