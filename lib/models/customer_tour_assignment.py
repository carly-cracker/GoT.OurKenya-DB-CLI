from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from lib.connection import Base, Session

class CustomerTourAssignment(Base):
    __tablename__ = "customer_tour_assignments"  
    
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    tour_package_id = Column(Integer, ForeignKey("tour_packages.id"), nullable=False)
    tour_package = relationship("TourPackage", back_populates="assignments")

    def __init__(self, customer_id, tour_package_id):
        self.customer_id = customer_id
        self.tour_package_id = tour_package_id

    @classmethod
    def create(cls, customer_id, tour_package_id):
        session = Session()
        try:
            assignment = cls(customer_id, tour_package_id)
            session.add(assignment)
            session.commit()
            return assignment
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    @classmethod
    def delete(cls, assignment_id):
        session = Session()
        try:
            assignment = session.get(cls, assignment_id)
            if not assignment:
                raise ValueError(f"Assignment ID {assignment_id} not found.")
            session.delete(assignment)
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
            assignments = session.query(cls).all()
            return assignments
        finally:
            session.close()

    @classmethod
    def find_by_id(cls, assignment_id):
        session = Session()
        try:
            assignment = session.get(cls, assignment_id)
            if not assignment:
                raise ValueError(f"Assignment ID {assignment_id} not found.")
            return assignment
        finally:
            session.close()

    def __repr__(self):
        return f"<CustomerTourAssignment(id={self.id}, customer_id={self.customer_id}, tour_package_id={self.tour_package_id})>"