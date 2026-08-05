create database info;
use info;

create table Employee (
    employeeid int primary key,
    employeename varchar(100),
    department varchar(50),
    salary int,
    joiningdate date
);
select * from Employee;