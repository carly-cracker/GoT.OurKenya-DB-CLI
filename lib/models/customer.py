from sqlalchemy import Column, Integer, String, Table , ForeignKey
from sqlalchemy.orm import relationship
from lib.connection import Base, Session
import re

customer_tour_packages = Table(
    "customer_tour_packages",
    Base.metadata,
    Column("customer_id", Integer, ForeignKey("customers.id"), primary_key=True),
    Column("tour_package_id", Integer, ForeignKey("tour_packages.id"), primary_key=True)
)
class Customer(Base):
    tablename__ = "customers" 
    
    id = Column(Integer, primary_key=True)  
    _name = Column("name", String, nullable=False)  
    _email = Column("email", String, nullable=False, unique=True)  
    _tel_no = Column("tel_no", String, nullable=False, unique=True)  

    tour_packages = relationship("TourPackage", secondary=customer_tour_packages, back_populates="customers")

    def __init__(self, name, email, tel_no):
        self.name = name
        self.email = email
        self.tel_no = tel_no

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value or not isinstance(value, str) or len(value.strip()) < 2:
            raise ValueError("Name must be >= 2 characters.")
        self._name = value.strip()
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if not value or not isinstance(value, str) or not re.match(r"[^@]+@[^@]+\.[^@]+", value):
            raise ValueError("Invalid email format.")
        self._email = value.lower()

    @property
    def tel_no(self):
        return self._tel_no

    @tel_no.setter
    def tel_no(self, value):
        if not value or not isinstance(value, str) or not re.match(r"^\+2547\d{8}$", value):
            raise ValueError("Telephone number must be in the format +2547XXXXXXXX (Kenyan format).")
        self._tel_no = value
    
    @classmethod
    def create(cls, name, email, tel_no):
        session = Session()
        try:
            customer = cls(name, email, tel_no)
            session.add(customer)  
            session.commit()  
            return customer
        except Exception as e:
            session.rollback()  
            raise e
        finally:
            session.close() 
    
    @classmethod
    def delete(cls, customer_id):
        session = Session()
        try:
            customer = session.get(cls, customer_id)
            if not customer:
                raise ValueError(f"Customer ID {customer_id} not found.")
            session.delete(customer)
            session.commit()
            return True
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
    
    @classmethod
    def get_all(cls):
        session = Session()
        try:
            customers = session.query(cls).all()
            return customers
        finally:
            session.close()

    @classmethod
    def find_by_id(cls, customer_id):
        session = Session()
        try:
            customer = session.get(cls, customer_id)
            if not customer:
                raise ValueError(f"Customer ID {customer_id} not found.")
            return customer
        finally:
            session.close()

    def add_tour_package(self, tour_package_id):
        session = Session()
        try:
            from lib.models.tour_package import TourPackage
            tour_package = session.get(TourPackage, tour_package_id)
            if not tour_package:
                raise ValueError(f"Tour package ID {tour_package_id} not found.")
            if tour_package.slots_remaining <= 0:
                raise ValueError(f"No slots remaining for tour package {tour_package_id}.")
            if tour_package not in self.tour_packages:
                self.tour_packages.append(tour_package)  
                tour_package.slots_remaining -= 1 
                session.commit()
            return True
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def get_tour_package_details(self):
        details = {}
        for tour in self.tour_packages:
            details[tour.id] = (tour.name, tour.price, tour.departure_date)
        return details
