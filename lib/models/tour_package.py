from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from lib.connection import Base, Session
from lib.models.customer import customer_tour_packages
from datetime import datetime

class TourPackage(Base):
    __tablename__ = "tour_packages"  

    id = Column(Integer, primary_key=True)
    _name = Column("name", String, nullable=False)
    _price = Column("price", Float, nullable=False)
    _departure_date = Column("departure_date", String, nullable=False)
    _slots_remaining = Column("slots_remaining", Integer, nullable=False)

    customers = relationship("Customer", secondary=customer_tour_packages, back_populates="tour_packages")
    assignments = relationship("CustomerTourAssignment", back_populates="tour_package", cascade="all, delete-orphan")

    def __init__(self, name, price, departure_date, slots_remaining):
        self.name = name
        self.price = price
        self.departure_date = departure_date
        self.slots_remaining = slots_remaining

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # Validate name: must be a string, at least 2 characters long
        if not value or not isinstance(value, str) or len(value.strip()) < 2:
            raise ValueError("Name must be >= 2 characters.")
        self._name = value.strip()

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        # Validate price: must be a positive number
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Price must be positive.")
        self._price = float(value)

    @property
    def departure_date(self):
        return self._departure_date

    @departure_date.setter
    def departure_date(self, value):
        try:
            datetime.strptime(value, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Date must be YYYY-MM-DD.")
        self._departure_date = value

    @property
    def slots_remaining(self):
        return self._slots_remaining

    @slots_remaining.setter
    def slots_remaining(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Slots must be non-negative.")
        self._slots_remaining = value

    @classmethod
    def create(cls, name, price, departure_date, slots_remaining):
        session = Session()
        try:
            tour_package = cls(name, price, departure_date, slots_remaining)
            session.add(tour_package)
            session.commit()
            return tour_package
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
    
    @classmethod
    def delete(cls, tour_package_id):
        session = Session()
        try:
            tour_package = session.get(cls, tour_package_id)
            if not tour_package:
                raise ValueError(f"Tour package ID {tour_package_id} not found.")
            session.delete(tour_package)
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
            tour_packages = session.query(cls).all()
            return tour_packages
        finally:
            session.close()

    @classmethod
    def find_by_id(cls, tour_package_id):
        session = Session()
        try:
            tour_package = session.get(cls, tour_package_id)
            if not tour_package:
                raise ValueError(f"Tour package ID {tour_package_id} not found.")
            return tour_package
        finally:
            session.close()

    def get_customer_details(self):
        details = {}
        for customer in self.customers:
            details[customer.id] = (customer.name, customer.email)
        return details

    def __repr__(self):
        return f"<TourPackage(id={self.id}, name={self.name}, price={self.price}, departure_date={self.departure_date}, slots_remaining={self.slots_remaining})>"