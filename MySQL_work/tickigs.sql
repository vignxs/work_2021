create database tickigs;
use tickigs;
show tables;
select * from auth_user;
select * from base_user_technologyname;
drop table  base_user_technologyname;
create table  base_user_technologyname (id int);

ALTER TABLE base_user_technologyname 
  DROP COLUMN id;