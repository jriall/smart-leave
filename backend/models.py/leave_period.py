from sqlalchemy import Column, DateTime, Float, Integer, String

from base import Base


class LeavePeriod(Base):
  """A period of annual leave  requested by an employee."""
  __tablename__ = 'leave_periods'

  id = Column(Integer, primary_key=True)
  date_requested = Column(DateTime)
  date_approved = Column(DateTime)
  date_rejected = Column(DateTime)
  # TODO(jriall) requested_by
  # TODO(jriall) approved_by
  # TODO(jriall) rejected_by
  total_days = Column(Float)
# TODO - Add start date, end date, and whether there are any half days. Need to think about how to represent this.

