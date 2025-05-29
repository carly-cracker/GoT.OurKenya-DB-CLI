# GoTripKenya CLI DB

A command-line tool for managing a travel agency, built with **Python**, **SQLAlchemy**, and **SQLite**. Manage customers, tour packages, and payments with ease.

---

## Features

- **Manage customers**: Create, update, delete, and list customers.
- **Handle tour packages**: Manage name, price, departure date, and slots.
- **Track payments**: Record and manage payments for bookings.
- **Many-to-many relationships**: Customers can book multiple tour packages.

---

## Setup

1. **Install Dependencies**
   ```bash
   pipenv install
2. **Activate virtual env**
    ```bash
    pipenv shell
    ```
3. ** Seed data base**
    ```bash
    python -m lib.seed.py
    ```
## Usage
python cli.py
- this allows user to enter the cli and navigate through the operations.

GoTripKenya CLI
1. Customer Operations
2. Tour Package Operations
3. Payment Operations
4. Exit
Select an option (1-4): 3

Payment Operations
1. List Payments
2. Find Payment by ID
3. Create Payment
4. Delete Payment
5. Back
Select an option (1-5): 1

<Payment(id=1, customer_id=1, tour_package_id=1, amount=500.0, date=2025-06-01, status=completed)>

## Database
- Tables: customers, tour_packages, customer_tour_packages, payments
- Storage: travel_agency.db (ignored by Git)

## Dependencies
- SQLAlchemy
- Pipenv
