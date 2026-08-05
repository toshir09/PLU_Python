create database productdb;
use productdb;

create table product (
    productid int primary key,
    productname varchar(50),
    category varchar(50),
    price int
);

insert into product (productid, productname, category, price)
values
(1, 'Mouse', 'Electronics', 800),
(2, 'Laptop', 'Electronics', 65000),
(3, 'Chair', 'Furniture', 4500),
(4, 'Keyboard', 'Electronics', 1200);

select * from Product
where Price > 1000;

select * from product
where category = 'Electronics';

select * from product
where productname = 'Laptop';
