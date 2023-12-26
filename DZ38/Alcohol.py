from DZ38.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Alcohol(Base):
    __tablename__ = 'alcohol'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    firm = Column(String(250), nullable=False)
    price = Column(Integer)
    group = Column(Integer, ForeignKey('groups.id'))

    def __init__(self, full_name, price, id_group):
        self.name = full_name[0]
        self.firm = full_name[1]
        self.price = price
        self.group = id_group


    def __repr__(self):
        return f"Алкоголь (Название: {self.name} {self.firm}), Цена: {self.price}, ID группы: {self.group}"