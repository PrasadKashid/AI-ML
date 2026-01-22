-- to check what is value of autocommit 
select @@autocommit;

-- setting autocommit value to 0 / 1
set autocommit = 0;

create database if not exists bank;
use bank;

CREATE TABLE accounts(
id INT PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(30),
balance DECIMAL(10,2)
);

INSERT INTO accounts (name, balance) 
values
('Bob', 5000.00);

select * from accounts;

-- transactions

-- 1. committing the transaction
START TRANSACTION;

UPDATE accounts SET balance = balance - 500 WHERE id = 1;
UPDATE accounts SET balance = balance + 500 WHERE id = 2;

COMMIT;

-- 2. Rollback the transaction
START TRANSACTION;

UPDATE accounts SET balance = balance - 500 where id = 1;
UPDATE accounts SET balance = balance + 500 where id = 2;

ROLLBACK;

-- 3. Savepoint
START TRANSACTION;

UPDATE accounts SET balance = balance + 1000 where id = 1;
SAVEPOINT after_wallet_topup;

UPDATE accounts SET balance = balance + 10 where id = 1;
-- error
ROLLBACK TO after_wallet_topup;

COMMIT;

SELECT * FROM accounts;



