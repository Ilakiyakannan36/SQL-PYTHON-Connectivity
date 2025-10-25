create database bank; # Create new database


use bank;  # database


CREATE TABLE Accounts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    account_holder VARCHAR(100) NOT NULL UNIQUE,
    pin CHAR(4) NOT NULL,
    balance DECIMAL(15,2) NOT NULL DEFAULT 0.00,
    created_at TIMESTAMP DEFAULT current_timestamp
);


select* from Accounts;