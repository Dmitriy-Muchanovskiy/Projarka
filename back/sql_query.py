import sqlalchemy
from sqlalchemy import create_engine
import re


engine = create_engine('mysql://root:rootdb@projarka-db/projarka')


with engine.connect() as con:
        
select = con.execute('SELECT first_text FROM first')

print(f"result of first query is \n {select}")

pattern=r"([\w\s-]+!)"
text=re.search(pattern,str(select))
