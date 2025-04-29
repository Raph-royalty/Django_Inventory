# Inventory Management System

This project is a web-based Inventory Management System built using Django. It allows users to efficiently manage their inventory by providing features to add, view, update, and delete products.

## Features

- **Add Products**: Users can add new products to the inventory with details such as name, SKU, price, quantity, and supplier.
- **View Products**: A list of all products in the inventory is displayed in a tabular format.
- **Update Products**: Users can update the details of existing products.
- **Delete Products**: Products can be removed from the inventory.

## Technologies Used

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS (Bootstrap for styling)
- **Database**: SQLite

## Setup Instructions

1. Clone the repository.
2. Install dependencies using `pipenv install`.
3. Run migrations using `python manage.py migrate`.
4. Start the development server using `python manage.py runserver`.
5. Access the application at `http://127.0.0.1:8000/`.

## Folder Structure

- `invApp/`: Contains the main application code, including models, views, forms, and templates.
- `templates/invApp/`: Contains HTML templates for the application.
- `migrations/`: Contains database migration files.
- `db.sqlite3`: SQLite database file.

## License

This project is licensed under the MIT License.