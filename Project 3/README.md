# **Python Banking System Project**

## **Overview**

This is a **Python-based Banking System** that simulates real-world banking operations.
It allows users to create accounts, deposit and withdraw money, and view transaction history.
The project uses **MySQL** for data storage and **bcrypt** for secure PIN handling.

---

## **Features**

* **Account Creation**

  * Supports **Saving Account** and **Current Account**
  * Validates age, PAN number, phone number, and minimum balance
  * Unique account number starting from **1000**

* **Account Details**

  * View full account information including balance, name, PAN, contact, and account type

* **Deposit Money**

  * Deposit funds into an account
  * Transactions logged in **txn_details** table

* **Withdraw Money**

  * Withdraw from Saving or Current accounts
  * Saving accounts: minimum balance enforced
  * Current accounts: overdraft allowed up to ₹10,000
  * PIN verification for security (**bcrypt**)

* **Transaction History**

  * View all transactions or a specified number of recent transactions
  * Shows type (**Credit/Debit**), amount, balance, and timestamp

* **Secure PIN Management**

  * PIN hashed using **bcrypt**
  * Set and verify PIN for withdrawals

---

## **Technology Stack**

* **Programming Language:** Python 3.x
* **Database:** MySQL
* **Python Libraries:** `mysql.connector`, `bcrypt`, `time`

---

## **Database Structure**

### **1. holder Table**

Stores account holder information:

| **Column** | **Type**                                 | **Description**                          |
| ---------- | ---------------------------------------- | ---------------------------------------- |
| acc_no     | INT AUTO_INCREMENT PRIMARY KEY           | Unique account number starting from 1000 |
| acc_type   | ENUM('Saving_account','Current_account') | Account type                             |
| name       | VARCHAR(100)                             | Account holder name                      |
| pan_no     | VARCHAR(10) UNIQUE                       | PAN card number                          |
| age        | INT                                      | Age of account holder                    |
| gender     | ENUM('Male','Female','Other')            | Gender                                   |
| phone_no   | VARCHAR(10) UNIQUE                       | Contact number                           |
| email_id   | VARCHAR(255)                             | Email address                            |
| balance    | FLOAT                                    | Current account balance                  |
| created_at | TIMESTAMP DEFAULT CURRENT_TIMESTAMP      | Account creation date                    |
| hashed_pin | VARCHAR(255)                             | Hashed PIN for withdrawal                |

---

### **2. txn_details Table**

Stores transaction details:

| **Column**   | **Type**                            | **Description**           |
| ------------ | ----------------------------------- | ------------------------- |
| txn_no       | INT AUTO_INCREMENT PRIMARY KEY      | Unique transaction number |
| acc_no       | INT                                 | Account number            |
| name         | VARCHAR(100)                        | Account holder name       |
| Credit_Debit | ENUM('Credit','Debit')              | Transaction type          |
| amount       | FLOAT                               | Transaction amount        |
| balance      | FLOAT                               | Balance after transaction |
| txn_date     | TIMESTAMP DEFAULT CURRENT_TIMESTAMP | Transaction date and time |

---

## **How to Run**

1. **Install required Python libraries:**

```bash
pip install mysql-connector-python bcrypt
```

2. **Create the database and tables in MySQL:**

```sql
-- Create bank database
CREATE DATABASE IF NOT EXISTS bank;

USE bank;

-- Create holder table
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

-- Create txn_details table
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

3. **Update the database connection in `bank.py`:**

```python
dbms = mysql.connector.connect(
    host="localhost",
    user="your_user",
    password="your_password",
    database="bank"
)
```

4. **Run the main Python program:**

```bash
python main.py
```

---

## **How It Works**

1. On running `main.py`, the user sees a **menu** with options:

   * Open Account
   * View Account Details
   * Deposit
   * Withdraw
   * View Transaction Details
   * Exit

2. Users can **create accounts**, **deposit/withdraw money**, and **view transactions**.

3. Withdrawals are **PIN-protected**.

4. All transactions are logged automatically in **txn_details**.

---

## **Future Improvements**

* Add **user login authentication**
* Implement **admin panel** to manage accounts
* Generate **monthly statements**
* Support **multiple currencies**



Do you want me to do that next?
