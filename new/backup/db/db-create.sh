#!/bin/bash
dbname="projarka"
tablename="first"
pass="rootdb"

mysql -u root -p${pass} -e "CREATE DATABASE ${dbname};"
mysql -u root -p${pass} -e "CREATE USER user IDENTIFIED BY 'user';"
mysql -u root -p${pass} -e "GRANT SELECT ON ${dbname}.* TO 'user'@'%';"
mysql -u root -p${pass} -e "CREATE TABLE ${dbname}.${tablename}(id int not null auto_increment, first_text varchar(100), sec_text varchar(100), primary key (id));"
mysql -u root -p${pass} -e "INSERT INTO ${dbname}.${tablename}(first_text,sec_text) values('This is the projarka-test!', 'This is the projarka sec-text!');"
