create database if not exists instagram;

use instagram;

CREATE TABLE user(
id INT,
age INT,
name VARCHAR(30) NOT NULL,
email varchar(30) UNIQUE,
follower int default 0,
constraint age_check check (age >= 18),
primary key (id)
);

insert into user values
(1, 26, "Prasad", "p@gmail.com", 0),
(2, 23, "Nisha", "n@gmail.com", 0);

select * from user;

create table posts(
post_id INT not null,
content varchar(30),
user_id INT not null,
PRIMARY KEY(post_id),
foreign key (user_id) references user(id)
);

insert into posts values
(1, 'Hello World', 1),
(2 , 'Bye bye', 2);

select * from posts;

insert into user (id, age, name, email)
values
(3, 26, "Alica", "a@gmail.com" ),
(4, 23, "Bob", "b@gmail.com");

select id, age, email from user;

select distinct age from user;

select * 
from user 
where age >= 26 or name= 'Prasad';

update user set follower = 300 where id = 1;
update user set follower = 200 where id = 2;

update user set follower = 100 where id = 3;
update user set follower = 500 where id = 4;
select * from user;
		
select * 
from user 
where age >= 26 and name= 'Prasad';

select * 
from user
where age >= 25 or name = 'Prasad';

select * 
from user
where age between 12 and 23;

select * 
from user
where email in ("n@gmail.com", "p@gmail.com");

select * 
from user
where age not in (22,26);

select * 
from user
where age > 18
Limit 2;

select * from user 
order by age asc;

select * from user 
order by follower desc;

select max(follower) from user;
select count(follower) from user where age > 25;
select min(follower) from user;
select sum(follower) from user;
select avg(age) from user;

select age, max(follower)
from user
group by age;

select age, max(follower)
from user
group by age
having max(follower) >= 500;

update user
set follower = 600
where age = 23;

delete from user
where id = 4;

alter table user
add column city varchar(30) default 'Mumbai';

alter table user
drop column city;

alter table users
rename to user;

alter table user
change column id user_id int;

alter table user
modify  follower int default 5;

delete from user
where user_id = 4;

insert into user
(user_id, age, name, email)
values
(4, 23, "Bob", "b@gmail.com");

select * from user;

truncate table user;

drop table user;










