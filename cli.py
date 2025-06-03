from lib.connection import init_db
from helpers import (exit_program,list_customers, find_customer_by_name,find_customer_by_id,
    create_customer,update_customer_details, delete_customer_with_details, list_tour_packages_by_customer,list_tour_packages, find_tour_package_by_name,
    find_tour_package_by_id, create_tour_package, update_tour_package,delete_tour_package, list_customers_by_tour_package,list_payments,
    find_payment_by_id, create_payment, delete_payment)

def main_menu():
    while True:
        print("\nGoTripKenya CLI")
        print("1. Customer Operations")
        print("2. Tour Package Operations")
        print("3. Payment Operations")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ")


        if choice == "1":
            customer_menu()
        elif choice == "2":
            tour_package_menu()
        elif choice == "3":
            payment_menu()
        elif choice == "4":
            exit_program()
        else:
            print("Invalid option. Please try again.")

def customer_menu():
    while True:
        print("\nCustomer Operations")
        print("1. List all customers")
        print("2. Find Customer by Name")
        print("3. find customer by ID")
        print("4. Create Customer")
        print("5. Update Customer details")
        print("6. Delete Customer with details")
        print("7. List all tour packages by customer")
        print("8. Back")
        choice = input("select an option (1-7):")

        if choice == "1":
            list_customers()
        elif choice == "2":
            find_customer_by_name()
        elif choice == "3":
            find_customer_by_id()
        elif choice == "4":
            create_customer()
        elif choice == "5":
            update_customer_details()
        elif choice == "6":
            delete_customer_with_details()
        elif choice == "7":
            list_tour_packages_by_customer()
        elif choice == "8":
            break

def tour_package_menu():
    while True:
        print("\nTour Package Operations")
        print("1. List tour packages")
        print("2. Find Tour Package By Name")
        print("3. Find Tour Package By ID")
        print("4. Create Tour Package")
        print("5. Update Tour Package")
        print("6. Delete Tour Package")
        print("7. List all customers for a tour package")
        print("8. Back")
        choice = input("Select an option (1-7): ")

        if choice == "1":
            list_tour_packages()
        elif choice == "2":
            find_tour_package_by_name()
        elif choice == "3":
            find_tour_package_by_id()
        elif choice == "4":
            create_tour_package()
        elif choice == "5":
            update_tour_package()
        elif choice == "6":
            delete_tour_package()
        elif choice == "7":
            list_customers_by_tour_package()
        elif choice == "8":
            break

def payment_menu():
    while True:
        print("\nPayment Operations")
        print("1. List Payments")
        print("2. Find Payment by ID")
        print("3. Create Payment")
        print("4. Delete Payment")
        print("5. Back")
        choice = input("Select an option (1-5): ")

        if choice == "1":
            list_payments()
        elif choice == "2":
            find_payment_by_id()
        elif choice == "3":
            create_payment()
        elif choice == "4":
            delete_payment()
        elif choice == "5":
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main_menu()