import sqlite3
from lib.connection import init_db, DATABASE_PATH

def seed_data():
    init_db() 
    conn = sqlite3.connect(DATABASE_PATH)  
    cursor = conn.cursor()
    
    try:
        customers = [
            ("Korir Carlos", "korir226@gmail.com", "+254799202039"),
            ("Almasi Job", "job123@gmail.com", "+254712281431")
        ]
        cursor.executemany("INSERT INTO customers (name, email, tel_no) VALUES (?, ?, ?)", customers)
        
        tour_packages = [
            ("Maasai Mara Safari", 1500.0, "2025-07-01", 10),
            ("Amboseli Elephantage", 1200.0, "2025-08-01", 8)
        ]
        cursor.executemany("INSERT INTO tour_packages (name, price, departure_date, slots_remaining) VALUES (?, ?, ?, ?)", tour_packages)
        
        assignments = [
            (1, 1),
            (2, 2)
        ]
        cursor.executemany("INSERT INTO customer_tour_packages (customer_id, tour_package_id) VALUES (?, ?)", assignments)

        assignments = [
            (1, 1),
            (2, 2)
        ]
        
        cursor.executemany("INSERT INTO customer_tour_assignments (customer_id, tour_package_id) VALUES (?, ?)", assignments)
        
        payments = [
            (1, 1, 500.0, "2025-06-01", "completed"),
            (2, 2, 300.0, "2025-06-05", "pending")
        ]
        cursor.executemany("INSERT INTO payments (customer_id, tour_package_id, amount, payment_date, status) VALUES (?, ?, ?, ?, ?)", payments)
        
        cursor.execute("UPDATE tour_packages SET slots_remaining = slots_remaining - 1 WHERE id = ?", (1,))
        cursor.execute("UPDATE tour_packages SET slots_remaining = slots_remaining - 1 WHERE id = ?", (2,))
        
        conn.commit()
        print("Seeded data successfully using raw SQL.")
    except Exception as e:
        conn.rollback()
        print(f"Error seeding data: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    seed_data()