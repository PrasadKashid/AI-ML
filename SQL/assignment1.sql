create database if not exists college;

use college;

CREATE TABLE teacher(
id INT PRIMARY KEY NOT NULL,
name VARCHAR(30) NOT NULL,
subject VARCHAR(30),
salary INT DEFAULT 25000
);

insert into teachers 
values
(23, 'ajay', 'math', 50000),
(47, 'bharat', 'english', 60000),
(18, 'chetan', 'chemistry', 45000),
(9, 'divya', 'physics', 75000);

SELECT * FROM teachers;

select * from teachers
where salary >= 55000;

alter table teachers
change salary ctc int default 25000;

update teachers
set ctc = ctc * 0.25;

select * from teachers;

alter table teachers
add column city varchar(30) default 'mumbai';

alter table teachers 
drop ctc;

SELECT * FROM teachers;

create table student(
roll_no INT PRIMARY KEY,
name VARCHAR(50) NOT NULL,
city VARCHAR(50),
marks int 
);

alter table student
rename to students;

insert into students
values
(110, 'adam', 'Delhi', 76),
(108, 'bob', 'Mumbai', 65),
(124, 'casey', 'Pune', 94),
(112, 'duke', 'pune', 80);

select * from students
where marks >= 75;

select city 
from students
group by city;

select city, max(marks)
from students
group by city;

select avg(marks) 
from students;

alter table students
add column grade varchar(10);

update students
set grade = 'O'
where marks >= 80;

update students
set grade = 'A'
where marks between 70 and 79;

update students 
set grade = 'B'
where marks between 60 and 69;

select * from students;





