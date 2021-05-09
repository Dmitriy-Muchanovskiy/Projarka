#!/bin/bash

dbname="projarka"
tablename="first"
pass="rootdb"
mysql -u root -p${pass} -e "UPDATE ${dbname}.${tablename} SET first_text='This is the projarka update-text!' WHERE id=1;"
