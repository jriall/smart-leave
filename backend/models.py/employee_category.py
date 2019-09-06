from sqlalchemy import Column, Integer, String

from base import Base


class EmployeeCategory(Base):
  """The employee categories defined by a company."""
  __tablename__ = 'employee_categories'

  id = Column(Integer, primary_key=True)
  name = Column(String)
  # TODO(jriall): Add company
