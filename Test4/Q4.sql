create database four;
use four;

create table customer (
    customerid int primary key,
    customername varchar(100),
    city varchar(50),
    mobile varchar(15)
);

insert into customer (customerid, customername, city, mobile)
values
(1, 'Rahul', 'Delhi', '9876543210'),
(2, 'Priya', 'Mumbai', '9876543211'),
(3, 'Aman', 'Pune', '9876543212');

select * from customer;