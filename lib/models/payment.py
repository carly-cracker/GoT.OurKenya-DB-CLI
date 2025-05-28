from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship
from lib.connection import Base, Session
from datetime import datetime

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    tour_package_id = Column(Integer, ForeignKey("tour_packages.id"), nullable=False)
    amount = Column(Float, nullable=False)
    payment_date = Column(String, nullable=False)
    status = Column(String, nullable=False)

    customer = relationship("Customer", back_populates="payments")
    tour_package = relationship("TourPackage", back_populates="payments")

    def __init__(self, customer_id, tour_package_id, amount, payment_date, status):
        self.customer_id = customer_id
        self.tour_package_id = tour_package_id
        self.amount = amount
        self.payment_date = payment_date
        self.status = status

    @classmethod
    def create(cls, customer_id, tour_package_id, amount, payment_date, status):
        session = Session()
        try:
            payment = cls(customer_id, tour_package_id, amount, payment_date, status)
            session.add(payment)
            session.commit()
            return payment
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    @classmethod
    def get_all(cls):
        session = Session()
        try:
            payments = session.query(cls).all()
            return payments
        finally:
            session.close()

    @classmethod
    def find_by_id(cls, payment_id):
        session = Session()
        try:
            payment = session.get(cls, payment_id)
            if not payment:
                raise ValueError(f"Payment ID {payment_id} not found.")
            return payment
        finally:
            session.close()

    @classmethod
    def delete(cls, payment_id):
        session = Session()
        try:
            payment = session.get(cls, payment_id)
            if not payment:
                raise ValueError(f"Payment ID {payment_id} not found.")
            session.delete(payment)
            session.commit()
            return True
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def __repr__(self):
        return f"<Payment(id={self.id}, customer_id={self.customer_id}, tour_package_id={self.tour_package_id}, amount={self.amount}, date={self.payment_date}, status={self.status})>"