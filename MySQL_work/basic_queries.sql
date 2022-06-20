use vignxs;
describe student;
select * from student;
alter table student drop column  age;
show columns from student;
alter table student add age int; 
select *from employe;

# update and delete

update student set major = 'comp sci' where sid = 9 and sname ='aad';
delete from student where sid = 9 and sname = 'aad'; 

#queries

select sname from student;
select sname,major  from student;
select student.sname from student;
select student.sname , student.sid , student.major from student order by sname;
select sname from student order by sid desc;
select sname from student order by sid asc limit 5;
select * from student order by sname limit 4;
select * from student 