# Orders Backend

An API to handle customers and respective orders they make. It enables an authenticated user to input / upload customers and orders.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)

## Features

- Authentification
- Add Customer
- Add orders

## Technologies Used

- Django 5.1.1
- Python 3.11.9
- PostgreSQL

## Installation

Follow these steps to set up your project locally:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ItotiaHarrison/OrdersBackend.git
   cd yourproject

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    
3. **Activate the virtual environment**:
   - On Windows:
    ```bash
    venv\Scripts\activate
    
  - On macOS/Linux:
    ```bash
      source venv/bin/activate

4. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    
5. **Set up the database**:
    Create a PostgreSQL database and update the database settings accordingly in pythonbackend/settings.py.
   
6. **Run migrations**:
    ```bash
    python manage.py migrate
    
## Usage

After completing the installation, you can run the project with the following command:
  -   ```bash
        python manage.py runserver
    
You can access the application by navigating to http://127.0.0.1:8000 in your web browser.

Example API Endpoints
- /api/orders/: List all orders.
- /api/customers/: List all customers.
