from lib.models.customer import Customer
from lib.models.tour_package import TourPackage
from lib.models.payment import Payment
from lib.connection import Session  
from datetime import datetime
import re

def exit_program():
    print("Thanks and Goodbye! ")
    exit()

def list_customers():
    customers = Customer.get_all()
    for customer in customers:
        print(customer)

def find_customer_by_name():
    name = input("Enter the customer's name: ")
    customer = next((c for c in Customer.get_all()if c.name.lower() == name.lower()), None)
    print(customer) if customer else print(f"Customer {name} not found")

def find_customer_by_id():
    id_ = input("Enter customer's id: ")
    customer = Customer.find_by_id(id_)
    print(customer) if customer else print(f"Customer with ID {id_} doesn't exist")
    
def create_customer():
    name =  input("Enter Customer's name: ")
    email = input("Enter Customer's email: ")
    tel_no = input("Enter Customer's tel no(07xxxxxxxx): ")
    try:
        customer = Customer.create(name,email,tel_no)
        print(f"customer{customer} successfully created")
    except Exception as e:
        print("Error creating customer", e)

def update_customer_details():
    id_ = input("Enter Customer's ID: ")
    session = None
    if customer := Customer.find_by_id(id_):
        try:
            name = input("Enter customer's new name: ")
            customer.name = name
            email = input("Enter custmoer's new email: ")
            customer.email = email
            tel_no = input("Enter customer's new phone number: ")
            customer.tel_no = tel_no

            session = Session()
            session.add(customer)
            session.commit()
            print("customer details successfully updated")
        except Exception as e:
            print('Error updating customer details', e)
        finally:
            session.close()
    
    else:
        print(f"customer {id_} not found")

def delete_customer_with_details():
    id_ = input("Enter customer's ID: ")
    if customer := Customer.find_by_id(id_):
        customer.delete(id_)
        print(f"Customer {id_} successfully removed from db")
    else:
        print(f"Customer{id_} not found")
