import sqlalchemy
from sqlalchemy.orm import sessionmaker
from CONFIG import DSN
from tables import create_tables, insert, Publisher, Book, Stock, Sale, Shop
import pandas as pd


def select(publisher):
    query = session.query(Publisher, Book, Stock, Sale, Shop)
    query = query.join(Publisher, Publisher.id == Book.id_publisher)
    query = query.join(Book, Book.id == Stock.id_book)
    query = query.join(Stock, Stock.id == Sale.id_stock)
    query = query.join(Shop, Shop.id == Stock.id_shop)

    records = query.all()
    for publisher, book, stock, sale, shop in records:  # execute all you need
        print(publisher.name, book, stock, sale, shop)


def select_sql(publisher):
    answer = con.execute((
        """
    SELECT p.name, sh.name, sa.price, sa.date_sale FROM publisher AS p
    JOIN book AS b ON p.id = b.id_publisher
    JOIN stock AS s ON b.id = s.id_book
    JOIN shop AS sh ON s.id_shop = sh.id
    JOIN sale AS sa ON s.id = sa.id_stock
    WHERE p.name LIKE %s;"""), publisher).fetchall()
    pf = pd.DataFrame(answer, columns=["Название книги", "Название магазина", "Цена", "Дата"])
    print(pf)


if __name__ == '__main__':
    db, user, password, db_name = input("Введите название типа БД "), input("Введите пользователя "), \
                                  input("Введите пароль "), input("Введите название БД ")
    DSN = db + "://" + user + ":" + password + "@localhost:5432/" + db_name
    engine = sqlalchemy.create_engine(DSN)
    con = engine.connect()
    create_tables(engine)  # создаем таблицу
    Session = sessionmaker(bind=engine)
    session = Session()
    insert(session)  # Добавляем значения в таблицу
    # author = 'Pearson'
    author = input("Введите автора, для поиска ")
    select_sql(author)
