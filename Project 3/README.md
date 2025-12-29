Python Banking System Project
Overview

This is a Python-based Banking System project that allows users to perform basic banking operations such as account creation, deposits, withdrawals, and viewing transaction history. It uses MySQL for persistent data storage and bcrypt for secure PIN management. This project demonstrates the integration of Python with a relational database to simulate a real-world banking system.

Features

Account Creation

Supports Saving Account and Current Account.

Validates user details (age, PAN number, phone number, and minimum balance).

Automatically generates a unique account number starting from 1000.

Account Details

View full account information including balance, name, PAN, contact details, and account type.

Deposit Money

Deposit funds into a specific account.

Transaction details are stored in the txn_details table.

Withdraw Money

Withdraw funds from Saving or Current accounts.

Saving accounts ensure minimum balance, Current accounts allow overdraft up to ₹10,000.

PIN verification for security using bcrypt.

Transaction details are logged automatically.

Transaction History

View all transactions or a specific number of recent transactions.

Transactions include deposit (Credit) and withdrawal (Debit) with timestamp.

Secure PIN Management

PIN is hashed using bcrypt and stored securely in the database.

Users can set and verify PIN for withdrawals.

Technology Stack

Programming Language: Python 3.x

Database: MySQL

Python Libraries: mysql.connector, bcrypt, time

Database Structure
1. holder Table

Stores account holder details:

Column	Type	Description
acc_no	INT AUTO_INCREMENT PRIMARY KEY	Unique account number starting from 1000
acc_type	ENUM('Saving_account','Current_account')	Type of account
name	VARCHAR(100)	Account holder's name
pan_no	VARCHAR(10) UNIQUE	PAN card number
age	INT	Age of account holder
gender	ENUM('Male','Female','Other')	Gender
phone_no	VARCHAR(10) UNIQUE	Contact number
email_id	VARCHAR(255)	Email address
balance	FLOAT	Current account balance
created_at	TIMESTAMP DEFAULT CURRENT_TIMESTAMP	Account creation date
hashed_pin	VARCHAR(255)	Hashed PIN for withdrawal security
2. txn_details Table

Stores transaction details:

Column	Type	Description
txn_no	INT AUTO_INCREMENT PRIMARY KEY	Unique transaction number
acc_no	INT	Account number
name	VARCHAR(100)	Account holder's name
Credit_Debit	ENUM('Credit','Debit')	Transaction type
amount	FLOAT	Transaction amount
balance	FLOAT	Account balance after transaction
txn_date	TIMESTAMP DEFAULT CURRENT_TIMESTAMP	Date and time of transaction

How to Run

Install required Python libraries:

pip install mysql-connector-python bcrypt


Create the database and tables in MySQL using the provided SQL files:

-- Create holder table
CREATE DATABASE IF NOT EXISTS bank;
USE bank;
-- Paste holder table SQL code here

-- Create txn_details table
USE bank;
-- Paste txn_details table SQL code here


Update the database connection in bank.py:

dbms = mysql.connector.connect(
    host="localhost",
    user="your_user",
    password="your_password",
    database="bank"
)


Run the main Python program:

python main.py
