create database five;
USE five;

create table employee (
    employeeid int primary key,
    name varchar(50),
    departmentid int
);

create table department (
    departmentid int primary key,
    departmentname varchar(50)
);

insert into employee (employeeid, name, departmentid)
values
(1, 'Rahul', 101),
(2, 'Priya', 102),
(3, 'Aman', 101);

insert into department (departmentid, departmentname)
values
(101, 'IT'),
(102, 'HR');

select
employee.name,
department.departmentname
from employee
inner join department
on employee.departmentid = department.departmentid;