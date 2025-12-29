---

# 🏦 Bank Management System (Python & MySQL)

A console-based **Bank Management System** built with **Python** and **MySQL**, allowing users to manage **Saving** and **Current accounts**, perform transactions, and view account and transaction details.

---

## Features

* **Open Account**

  * Saving Account (minimum age 18, minimum deposit ₹1000)
  * Current Account (minimum age 25, minimum deposit ₹10000)

* **View Account Details**

  * Display account number, type, name, PAN, gender, phone, email, and balance.

* **Deposit**

  * Deposit money into the account and automatically record transaction.

* **Withdraw**

  * Withdraw money with PIN verification
  * Supports overdraft for Current Accounts up to ₹10,000
  * Records transaction in database.

* **Transaction Details**

  * View last N transactions or all transactions for an account.

* **PIN Security**

  * Uses **bcrypt hashing** to securely store PINs in the database.

---

## Technologies Used

* Python 3.x
* MySQL 8.x or higher
* `mysql-connector-python` library
* `bcrypt` library for PIN hashing

---

## Database Setup

1. Create the database and tables:

```sql
CREATE DATABASE IF NOT EXISTS bank;
USE bank;

CREATE TABLE holder (
    acc_no INT UNIQUE PRIMARY KEY NOT NULL AUTO_INCREMENT,
    acc_type ENUM('Saving_account','Current_account') NOT NULL,
    name VARCHAR(100) NOT NULL,
    pan_no VARCHAR(10) UNIQUE NOT NULL,
    age INT NOT NULL,
    gender ENUM('Male','Female','Other') NOT NULL,
    phone_no VARCHAR(10) UNIQUE NOT NULL,
    email_id VARCHAR(255) NOT NULL,
    balance FLOAT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    hashed_pin VARCHAR(255)
);

ALTER TABLE holder AUTO_INCREMENT = 1000;

CREATE TABLE txn_details (
    txn_no INT UNIQUE AUTO_INCREMENT PRIMARY KEY NOT NULL,
    acc_no INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    Credit_Debit ENUM('Credit','Debit') NOT NULL,
    amount FLOAT NOT NULL,
    balance FLOAT NOT NULL,
    txn_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## How to Run

1. Install required Python libraries:

```bash
pip install mysql-connector-python bcrypt
```

2. Update database credentials in `bank.py`:

```python
dbms = mysql.connector.connect(
    host="localhost",
    user="your_user",
    password="your_password",
    database="bank"
)
```

3. Run the main program:

```bash
python main.py
```

---

## Privacy & Safety Notice

* **Do not enter real personal information of anyone else**.
* Only input **your own dummy or test data** if sharing the program.
* Storing or sharing someone else’s personal info without consent may violate **privacy laws**.
* PINs are securely hashed and stored, but always handle sensitive info carefully.

---

## Project Structure

```
Bank-Management-System/
│
├─ main.py            # Program interface, handles user input
├─ bank.py            # Core classes (Bank, Saving_account, Current_account)
├─ holder.sql         # SQL script to create 'holder' table
└─ txn_details.sql    # SQL script to create 'txn_details' table
```

---

## Future Improvements

* Add **GUI interface** with Tkinter or PyQt.
* Implement **multi-user login system**.
* Add **report generation** for account statements.
* Encrypt the entire database for additional security.

---
