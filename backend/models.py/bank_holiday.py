from sqlalchemy import Column, Integer, Date

from base import Base


class BankHoliday(Base):
  """A bank holiday date."""
  __tablename__ = 'bank_holidays'

  id = Column(Integer, primary_key=True)
  date = Column(Date)
  # TODO(jriall): Add company
