create database if not exists shopping;

use shopping;

create table customers(
customer_id int primary key,
name varchar(50),
city varchar(50)
);

insert into customers values
(1, 'Alice', 'Mumbai'),
(2, 'Bob', 'Kolkata'),
(3, 'Charlie', 'Delhi'),
(4, 'David', 'Pune');

CREATE TABLE orders(
order_id int PRIMARY KEY,
customer_id int,
amount int
);

insert into orders values
(101, 1, 200),
(102, 1, 1200),
(104, 2, 300),
(105, 4, 800);

select * from customers;
select * from orders;

-- inner join
select *
from customers as c
INNER JOIN orders as o
on c.customer_id = o.customer_id;

-- left join
select * 
from customers c
LEFT JOIN orders o
on c.customer_id = o.customer_id;

-- right join
select *
from customers c
RIGHT JOIN orders o
on c.customer_id = o.customer_id; 

-- outer join
select * 
from customers c
LEFT JOIN orders o
on c.customer_id = o.customer_id
UNION
select * 
from customers c
RIGHT JOIN orders o
on c.customer_id = o.customer_id;

-- cross join
select *
from customers
cross join orders;

-- self joins
select * 
from customers as A
join customers as B
on A.customer_id = B.customer_id;

-- left exclusive join
select *
from customers as c
left join orders as o
on c.customer_id = o.customer_id
where o.customer_id is null;

select * 
from customers as c
right join orders as o
on c.customer_id = o.customer_id
where o.customer_id is Null;

select * from customers;
select * from orders;

select * 
from orders 
where amount > (
	select avg(amount)
	from orders
);

select name,
(
	select count(*)
	from orders o 
	where o.customer_id = c.customer_id
) as order_count
from customers c;

select
	summary.customer_id,
    summary.avg_amount
from
	(	
		select 
			customer_id, 
            avg(amount) as avg_amount
		from orders
		Group by customer_id
	) as summary;
    
-- views in sql

create view v1 as
select name, customer_id from customers;

select * from v1;

create view v2 as
select name, c.customer_id, o.order_id
from customers c
inner join orders o
on c.customer_id = o.customer_id;

select * from v2;

create table accounts(
	account_id INT PRIMARY KEY,
    name varchar(30),
    balance DECIMAL(10,2),
    branch VARCHAR(50)
);

insert into accounts values
(1, 'Adam', 500.00, 'Mumbai'),
(2, 'Bob', 300.00, 'Delhi'),
(3, 'Alice', 200.00, 'Mumbai'),
(4, 'David', 400.00, 'Noida');

select * from accounts;

-- indexing
create index idx_branch on accounts(branch);

show index from accounts;

select * from accounts;

-- composite indexing

create index idx2 on accounts(branch, balance);

show index from accounts;

drop index idx2 on accounts;

select * from accounts;

delimiter $$
create procedure check_balance(IN acc_id int, out bal decimal(10,2))
BEGIN
	select balance into bal
    from accounts
    where account_id = acc_id;
END $$

delimiter ;

CALL check_balance(1, @balance);
select @balance;

drop procedure check_balance;












