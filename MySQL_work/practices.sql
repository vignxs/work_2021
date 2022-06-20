show databases;
create database practice;
use practice;
create table infoo(id int,namee varchar(20));
insert into infoo values(1,'vignesh');
insert into infoo values(1,'vignesh');
insert into infoo values(2,'akash');
insert into infoo values(2,'akash');
insert into infoo values(3,'dhivya');
insert into infoo values(4,'sangari');
select * from infoo;

select distinct namee,id  into info from infoo;


delete t1 from infoo  t1 inner join  infoo  t2 where t1.namee < t2.namee and t1.id = t2.id;
select * from info group by id having count(name) > 1;

 
select count(id) ,namee from infoo group by id  having count(id) > 1;
select * , row_number() over (partition by id  order by id) as r_n from infoo ;
delete from infoo where r_n > 1;
delete  from info s1 where id < (select max(id) from info s2 where s1.id = s2.id and s1.name = s2.name);

delete from 
(select * , row_number() over (partition by id ) as r_n from infoo)
where r_n > 1;


with CTE AS 
(select id,namee , row_number() over(partition by id , namee order by id,namee )as rn from infoo)
delete from  CTE where rn > 1;