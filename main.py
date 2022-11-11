import sqlalchemy
from sqlalchemy.orm import sessionmaker
from CONFIG import DSN
from tables import create_tables, insert


def select(publisher):
    None

if __name__ == '__main__':
    engine = sqlalchemy.create_engine(DSN)
    create_tables(engine) # создаем таблицу
    Session = sessionmaker(bind=engine)
    session = Session()
    insert(session) # Добавляем значения в таблицу



