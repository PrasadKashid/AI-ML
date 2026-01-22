CREATE DATABASE IF NOT EXISTS employee_db;

use employee_db;

create table employees(
EmpId INT PRIMARY KEY,
FirstName VARCHAR(50) NOT NULL,
LastName VARCHAR(50) NOT NULL,
Department VARCHAR(50),
Salary INT,
HireDate DATE
);

INSERT INTO employees
values
(101, 'Alice', 'Johnson', 'IT', 6500, '2020-03-15'),
(102, 'Mark', 'Rivera', 'HR', 4800, '2019-07-22'),
(103, 'Sophia', 'Lee', 'Finance', 7200, '2021-01-10'),
(104, 'Daniel', 'Kim', 'IT', 5800, '2018-11-05'),
(105, 'Emma', 'Brown', 'Marketing', 5300, '2020-03-15'),
(106, 'Liam', 'Patel', 'Finance', 6900, '2020-09-29'),
(107, 'Olivia', 'Gracia', 'HR', 4600, '2017-06-30'),
(108, 'Noah', 'Thompson', 'IT', 7500, '2023-02-12'),
(109, 'Ava', 'Marteniz', 'Marketing', 5100, '2019-12-02'),
(110, 'Ethan', 'Davis', 'Finance', 8000, '2016-04-14');

select * from employees;

select FirstName, LastName, Salary from employees;

select * 
From employees
where Department = 'IT';

select * 
from employees
order by HireDate desc;

select distinct Department from employees;

select * 
from employees
where FirstName = 'A';

select *
from employees
where FirstName LIKE 'A%'; 

select *
from employees
where salary >= 4000 and salary <= 7000;

select avg(salary) from employees;

select department, COUNT(*) as emp_count
from employees
group by department
having COUNT(*) >= 3; 













