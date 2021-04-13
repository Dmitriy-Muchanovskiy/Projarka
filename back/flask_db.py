import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy import inspect

metadata = MetaData()
projarka = Table('first', metadata,
  Column('id', Integer, primary_key=True),
  Column('first_text', String),
  Column('sec_text', String),
)

engine = create_engine('mysql:///bookstore.db')
metadata.create_all(engine)
