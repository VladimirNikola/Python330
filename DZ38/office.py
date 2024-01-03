from DZ38.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship


association_table = Table('association', Base.metadata,
                          Column('office_id', Integer, ForeignKey('offices.id')),
                          Column('meeting_id', Integer, ForeignKey('meetings.id')))


class Office(Base):
    __tablename__ = 'offices'

    id = Column(Integer, primary_key=True)
    office_title = Column(String(250), nullable=False)
    meetings = relationship('Meeting', secondary=association_table, backref='meeting_office')

    def __repr__(self):
        return f"Номер кабинета {self.id}, Название кабинета: {self.office_title})"
