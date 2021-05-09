import sqlalchemy
from sqlalchemy import create_engine
import re


engine = create_engine('mysql://user:user@projarka-db/projarka')

t=()
with engine.connect() as con:
  select = con.execute('SELECT * FROM first')
  for s in select:
      t=tuple(s)

text=t[1]
#print(f"{type(text)} + {text}")

