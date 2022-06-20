show databases;
use company;
show tables;
describe branch;
select * from employee limit 5;
select * from student;
truncate branch;
select * from client;
select * from employee order by salary desc;
select * from employee order by sex,first_name,last_name;
select * from employee limit 5;
select first_name , last_name from employee;
select concat(first_name, " ",last_name)  as full_name from employee;
select distinct sex from  employee;

-- functions

select count(emp_id) from employee;
select count(emp_id) from employee where sex = 'f' and birth_day > '1970-01-01';
select * from employee where sex = 'f' and birth_day > '1970-01-01';
select avg(salary) from employee;
select sum(salary) from employee where sex = 'm';
select count(sex),sex from employee group by sex;
select sum(total_sales) ,client_id from works_with group by client_id;

-- wildcards

update branch_supplier set  supplier_name = 'stanford labels' where supply_type = 'custom forms'   ;
select * from branch_supplier;
select * from client where client_name like '%llc';
select * from branch_supplier where supplier_name like '%labels';
select * from employee where birth_day like '_____02%';
select * from client where client_name like '%school%';
select * from client;

-- union

select first_name from employee intersect select branch_name from branch; 
select  supplier_name , branch_id from branch_supplier union select client_name , branch_id from client;
select * from branch;
select salary from employee union select total_sales from works_with;

-- joins

select employee.emp_id,employee.first_name,branch.branch_name from employee inner join branch on  employee.emp_id = branch.mgr_id;
select employee.emp_id,employee.first_name,branch.branch_name from employee left join branch on employee.emp_id = branch.mgr_id;
select employee.emp_id,employee.first_name,branch.branch_name from branch left join employee on employee.emp_id = branch.mgr_id;
select * from employee
-- nested query

select first_name , last_name from employee where emp_id in (select emp_id from works_with where  total_sales > 30000 );
select client_name from client where branch_id = (select branch_id from branch where mgr_id  = 102); 

select * from branch;

-- on delete set null
delete from employee where emp_id = 102;
delete from branch where branch_id = 2;
select * from branch;
select * from employee;
select * from branch_supplier;
-- triggers
create table trigger_test(message char(100));
delimiter $$
create 
	trigger my_trigger before insert 
    on employee
	for each row begin
		insert into trigger_test values('add new employee');
	end $$  
    delimiter ;
select * from trigger_test;
delimiter $$
create 
	trigger my_trigger1 before insert 
    on employee
	for each row begin
		insert into trigger_test values(new.first_name);
	end $$  
    delimiter ;
    
insert into employee values(110,'kevin','malone','1970-03-20','m',45000,106,3);
select * from trigger_test;

delimiter $$
create 
	trigger my_trigger2 before insert 
    on employee
	for each row begin
		if new.sex = "m" then
			insert into trigger_test values('added male');
		elseif new.sex = 'f' then
			insert intp trigger_test values('added female');
		else
			insert into trigger_test values('addded other employee');
		end if;
	end $$  
delimiter ;

insert into employee values(111,'pam','beesly','1988-10-10','f',70000,106,3);
select * from trigger_test;

-- end of sql course by freecodecamp c'ya


select * from employee;
select top 1 salary  from (select distinct top 3  salary from employee  order by salary desc) as temp order by salary ;