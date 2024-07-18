from database import Base
from sqlalchemy import Column, String, Integer


class Students(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    address = Column(String)