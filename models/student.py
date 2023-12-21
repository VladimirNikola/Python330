from models.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True)
    surname = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    patronymic = Column(String(250), nullable=False)
    age = Column(Integer)
    group = Column(Integer, ForeignKey('groups.id'))
