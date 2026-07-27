create database salarydb;
use salarydb;

create table orders (
    orderid int primary key,
    customername varchar(100),
    orderdate date,
    amount int
);

insert into orders (orderid, customername, orderdate, amount)
values
(101, 'Rahul', '2025-07-01', 5000),
(102, 'Priya', '2025-07-02', 3000),
(103, 'Aman', '2025-07-03', 4500);

create index idx_orderid
on orders(orderid);