import sqlalchemy
from sqlalchemy.orm import sessionmaker
from CONFIG import DSN
from tables import create_tables, insert, Publisher, Book, Stock, Sale, Shop


def select(publisher):
    query = session.query(Publisher, Book, Stock, Sale, Shop)
    query = query.join(Publisher, Publisher.id == Book.id_publisher)
    query = query.join(Book, Book.id == Stock.id_book)
    query = query.join(Stock, Stock.id == Sale.id_stock)
    query = query.join(Shop, Shop.id == Stock.id_shop)

    records = query.all()
    for publisher, book, stock, sale, shop in records: # execute all you need
        print(publisher.name, book, stock, sale, shop)


if __name__ == '__main__':
    engine = sqlalchemy.create_engine(DSN)
    create_tables(engine)  # создаем таблицу
    Session = sessionmaker(bind=engine)
    session = Session()
    insert(session)  # Добавляем значения в таблицу
    select('Pearson')
