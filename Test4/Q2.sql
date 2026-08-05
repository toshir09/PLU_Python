CREATE DATABASE Studentdb;
USE Studentdb;

create table student (
    studentid int primary key,
    name varchar(50),
    course varchar(50),
    marks int
);
select * from student;

insert into student (studentid, name, course, marks)
values
(101, 'Rahul', 'Python', 80),
(102, 'Priya', 'Java', 75),
(103, 'Aman', 'Python', 90),
(104, 'Neha', 'SQL', 70);

select * from student;

select name, marks
from student;

select course
from student;