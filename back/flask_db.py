import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy import inspect
from sqlalchemy.sql import text

metadata = MetaData()
projarka = Table('first', metadata,
  Column('id', Integer, primary_key=True),
  Column('first_text', String),
  Column('sec_text', String),
)

engine = create_engine('mysql://root:rootdb@projarka-db/projarka')
metadata.create_all(engine)


with engine.connect() as con:

    data = ( { "id": 1, "first": "This is the projarka-test!", "primary_author": "This is the projarka sec-text!" }    )

    statement = text("""INSERT INTO book(id, first_text, sec_text) VALUES(:id, :first_text, :sec_text)""")

    for line in data:
        con.execute(statement, **line)

        
    select = con.execute('SELECT first_text FROM first')

print(f"result of first query is \n {select}")

pattern=r"([\w\s-]+!)"
text=re.search(pattern,str(select))
