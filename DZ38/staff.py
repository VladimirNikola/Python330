from DZ38.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Staff(Base):  # (персонал)
    __tablename__ = 'staff'

    id = Column(Integer, primary_key=True)
    surname = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    patronymic = Column(String(250), nullable=False)
    age = Column(Integer)
    meeting = Column(Integer, ForeignKey('meetings.id'))

    def __init__(self, full_name, age, id_meeting):
        self.surname = full_name[0]
        self.name = full_name[1]
        self.patronymic = full_name[2]
        self.age = age
        self.meeting = id_meeting

    def __repr__(self):
        return f"Сотрудник (ФИО: {self.surname} {self.name} {self.patronymic}, " \
               f"Возраст: {self.age}, № кабинета: {self.meeting})"
