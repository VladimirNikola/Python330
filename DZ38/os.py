import os

from DZ38.database import DATABASE_COMPANY
import create_database_company as db_creator

if __name__ == '__main__':
    db_is_created = os.path.exists(DATABASE_COMPANY)
    if not db_is_created:
        db_creator.create_database()
