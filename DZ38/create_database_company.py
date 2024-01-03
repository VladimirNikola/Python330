from faker import Faker

from DZ38.database import create_db, Session
from DZ38.office import Office
from DZ38.staff import Staff
from DZ38.meeting import Meeting


def create_database(load_fake_data=True):
    create_db()
    if load_fake_data:
        _load_fake_data(Session())


def _load_fake_data(session):
    office_names = ['Директор', 'Коммерческий директор', 'Бухгалтерия', 'Отдел внешнеэкономических связей',
                    'Секретариат', 'Служба делопроизводства', 'Отдел кадров']

    meeting1 = Meeting(meeting_name='Актовый зал')
    meeting2 = Meeting(meeting_name='Зал совещаний')

    session.add(meeting1)
    session.add(meeting2)

    for key, it in enumerate(office_names):
        office = Office(office_title=it)
        office.meetings.append(meeting1)
        if key % 2 == 0:
            office.meetings.append(meeting2)
        session.add(office)

    session.commit()

    faker = Faker('ru_Ru')
    meeting_list = [meeting1, meeting2]

    for _ in range(50):
        full_name = faker.name().split()
        age = faker.random.randint(18, 50)
        meeting = faker.random.choice(meeting_list)
        staff = Staff(full_name, age, meeting.id)
        session.add(staff)

    session.commit()
    session.close()
