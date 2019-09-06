import datetime

from sqlalchemy import Column, Integer, String, DateTime, Date

from base import Base


class Company(Base):
  """An individual company using the SmartLeave app."""
  __tablename__ = 'companies'

  id = Column(Integer, primary_key=True)
  name = Column(String)
  created_at = Column(DateTime, default=datetime.datetime.utcnow)
  year_start = Column(Date)
  year_end = Column(Date)
