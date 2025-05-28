from lib.models.customer import Customer
from lib.models.tour_package import TourPackage
from lib.models.payment import Payment
from lib.connection import Session 
from sqlalchemy.orm import sessionmaker 
from lib.connection import engine
from datetime import datetime
import re

Session = sessionmaker(bind=engine)


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

def list_tour_packages():
    tour_packages = TourPackage.get_all()
    for tour_package in tour_packages:
        print(tour_package)

def find_tour_package_by_name():
    name = input("Enter tour package's name: ")
    tour_package = next((tp for tp in TourPackage.get_all()
    if tp.name.lower()==name.lower()), None)
    print(tour_package) if tour_package else print(f"tour package {name} not found in the database")
def find_tour_package_by_id():
    id_ = input("Enter the tour package's ID: ")
    tour_package = TourPackage.find_by_id(id_)
    print(tour_package) if tour_package else print("tour package {id_} not found in the db")
def create_tour_package():
    name = input("Enter the tour package name: ")
    price = float(input("Enter the tour package price: "))
    departure_date = input("Enter the tour package's depature date (YYYY-MM-DD): ")
    slots_remaining = int(input("Enter the remaining slots for the tour package: "))
    session = Session()
    try:
        tour_package = TourPackage(
            name=name,
            price=price,
            departure_date=departure_date,
            slots_remaining=slots_remaining
        )
        session.add(tour_package)
        session.commit()
        print(f"Tour package '{tour_package.name}' successfully added to db with ID {tour_package.id}")
    except Exception as e:
        print("error creating tour package", e)
def update_tour_package():
    id_ = input("Enter tour package id to be updated: ")
    session = Session()
    if tour_package := TourPackage.find_by_id(id_):
        try:
            name = input("Enter tourpackage's new name: ")
            tour_package.name = name
            price = float(input("Enter tourpackage's new price: "))
            tour_package.price = price
            departure_date = input("Enter the tour package's new departure date (YYYY-MM-DD): ")
            tour_package.departure_date = departure_date
            slots_remaining = int(input("Enter the tour package's new slots remaining: "))
            tour_package.slots_remaining = slots_remaining
            session.add(tour_package)
            session.commit()
        except Exception as e:
            print("Error updating tour package: ", e)