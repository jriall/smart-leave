from sqlalchemy import Boolean, Column, DateTime, Float, Integer, String

from base import Base


class User(Base):
  """A user of the SmartLeave application."""
  __tablename__ = 'users'

  id = Column(Integer, primary_key=True)
  name = Column(String)
  email = Column(String)
  date_created = Column(DateTime)
  is_admin = Column(Boolean)
  total_leave_days = Column(Float)
  leave_days_taken = Column(Float) # TODO(jriall): Is this property needed?
  # TODO(jriall): Properties to add:
  # - Consider how to show data against particular years.
  # - Company company
  # - EmployeeCategory employee_category
  # - User approver # Person who approves their holiday. I’d also say admins can approve anyone’s holiday?
