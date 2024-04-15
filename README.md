# django-react-app

## Overview

This project showcases an order management system built using the Django framework. The system features a RESTful API that enables user, order, and product management.

## Key Features

### User Management

- User registration, login, and logout
- User management (add, edit, and delete)

### Order Management

- View orders (with filtering and sorting options)
- Add a new order
- Edit an existing order
- Add products to an order

### Product Management

- View product list
- Add a new product
- Edit an existing product
- Delete a product

### Reports

- Generate sales summary report for a customer (including total order amount)

## Technologies

- Django framework
- Django REST framework
- SQLite database
- React (optional)
- TypeScript (optional)
- OpenAPI (optional)

## Installation:

###### Important: Use code with caution.

#### Install Dependencies

```properties
pip install -r requirements.txt
```

#### Run Database Migrations

```
python manage.py migrate

```

#### Start Development Server

```
python manage.py runserver

```

#### Using the API

###### The API is accessible at the following URL:

```
http://localhost:8000/

```

###### Detailed API documentation can be found at:

```
http://localhost:8000/docs/

```

### Additional Resources

- Django framework: https://djangoproject.com/
- Django REST framework: https://www.django-rest-framework.org/
- React: https://reactjs.org/
- TypeScript: https://www.typescriptlang.org/
- OpenAPI: https://swagger.io/
