import sqlalchemy
import json
from sqlalchemy.orm import sessionmaker
from CONFIG import DSN
from tables import Base, Publisher, Shop, Book, Stock, Sale, create_tables

engine = sqlalchemy.create_engine(DSN)
create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

with open('data.json', 'r') as fd:
    data = json.load(fd)

for record in data:
    print(record)
    model = {
        'publisher': Publisher,
        'shop': Shop,
        'book': Book,
        'stock': Stock,
        'sale': Sale,
    }[record.get('model')]

    session.add(model(id=record.get('pk'), **record.get('fields')))
session.commit()
