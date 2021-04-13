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
  select = con.execute("insert into first(id,first_text,sec_text) values('1','This is the projarka-test!', 'This is the projarka sec-text!')")





