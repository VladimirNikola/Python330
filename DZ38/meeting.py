from DZ38.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Meeting(Base):  # (Совещание)
    __tablename__ = 'meetings'

    id = Column(Integer, primary_key=True)
    meeting_name = Column(String(250), nullable=False)
    staff = relationship('Staff')

    def __repr__(self):
        return f" № Совещания  {self.id}, Название: {self.meeting_name})"
