SCHEMA_SQL = """
DROP TABLE IF EXISTS customer_tour_packages;
DROP TABLE IF EXISTS tour_packages;
DROP TABLE IF EXISTS payments;
DROP TABLE IF EXISTS customers;


CREATE TABLE customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    tel_no TEXT NOT NULL UNIQUE
);

CREATE TABLE tour_packages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    departure_date TEXT NOT NULL,
    slots_remaining INTEGER NOT NULL
);

CREATE TABLE customer_tour_packages (
    customer_id INTEGER NOT NULL,
    tour_package_id INTEGER NOT NULL,
    PRIMARY KEY (customer_id, tour_package_id),
    FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE CASCADE,
    FOREIGN KEY (tour_package_id) REFERENCES tour_packages(id) ON DELETE CASCADE
);


CREATE TABLE payments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    tour_package_id INTEGER NOT NULL,
    amount REAL NOT NULL,
    payment_date TEXT NOT NULL,
    status TEXT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE CASCADE,
    FOREIGN KEY (tour_package_id) REFERENCES tour_packages(id) ON DELETE CASCADE,
    FOREIGN KEY (customer_id, tour_package_id) REFERENCES customer_tour_packages(customer_id, tour_package_id) ON DELETE CASCADE
);
"""