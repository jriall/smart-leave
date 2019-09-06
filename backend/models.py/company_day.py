from sqlalchemy import Column, Integer, Date

from base import Base


class CompanyDay(Base):
  """A denoted company day.

  Represents a day in which the entire company is closed. Does not include bank
  holidays.
  """
  __tablename__ = 'company_days'

  id = Column(Integer, primary_key=True)
  date = Column(Date)
  # TODO(jriall): Add company
