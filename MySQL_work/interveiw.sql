use company;
select * from employee;
select top 1 salary  from (select distinct top 3  salary from  order by salary desc) as temp order by salary ;
create table salary(id int, salary int);
insert into salary values(1,5000);
insert into salary values(2,10000);
insert into salary values(3,12000);
insert into salary values(4,5500);
insert into salary values(5,13000);
insert into salary values(6,15000);
select * from salary;
delete from salary where id = 1;
update salary set salary = 11000 where id  = 1;
select  * from salary;
select max(salary) from salary where salary not in ( select max(salary) from salary);
select max(salary) from salary;
select min(salary) from salary;
select min(salary) from (select distinct salary  as  temp from employee order by salary desc) where rownum<3;
select * from employee;

select salary from salary order by salary desc limit 1,1;

select first_name,salary from employee as e1 where 4-1 = (select count(distinct salary) from employee as e2 where e2.salary > e1.salary); 
select salary from salary order by salary desc limit 1;
select * from salary;
select max(salary) from salary where salary < (select max(salary) from salary);
select max(salary) from salary where salary not in (select max(salary) from salary);
select * from employee as e1 where 2-1 = (select count(distinct salary) from employee as e2 where e2.salary > e1.salary);
delete name from hi as a1 inner join hi as a2 where a1.name = a2.name;
select * from hi;
show tables;
select * from infoo; 
use practice;

select id,namee,count(*) from infoo group by id having  count(*) > 1;

select * from infoo order by id;
select max(id) ,namee from infoo group by id;

delete from infoo where id not in
(select max(id) ,namee from infoo group by);

with infoo_CTE as  
(select namee,id , row_number() over (partition by id order by id) as rownumber from infoo)
delete from infoo_CTE where rownumber > 1;
 
truncate table infoo;
drop table infoo;
select * from employee;
create table hi like employee;

select * from heyyyye;
insert into heyyyye values select * from  employee;
create table heyyyye as(select * from employee where 2 = 1);
insert  into hey values  (select * from employee);
 
 show tables;