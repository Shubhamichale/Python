import mysql.connector
import bcrypt

dbms = mysql.connector.connect(
    host="localhost",
    user="your_user",
    password="your_password",
    database="bank"
)
cursor = dbms.cursor()


class Bank:
    def __init__(self, name, pan_no, age, gender, phone_no, email_id, balance, hashed_pin=None):
        self.name = name
        self.pan_no = pan_no
        self.age = age
        self.gender = gender
        self.phone_no = phone_no
        self.email_id = email_id
        self.balance = balance
        self.hashed_pin = hashed_pin

    def acc_details_insertion(self):
        self.status = True
        try:
            sql = "INSERT INTO holder (acc_type,name,pan_no,age,gender,phone_no,email_id,balance) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
            values = (self.acc_type, self.name, self.pan_no, self.age, self.gender, self.phone_no, self.email_id, self.balance)
            cursor.execute(sql, values)
            dbms.commit()
        except mysql.connector.Error:
            self.status = False
            return self.status

    def show_details(self):
        print(f"\nAccount no: {self.acc_no}")
        print(f"Account type: {self.acc_type}")
        print(f"Name: {self.name}")
        print(f"Pancard no: {self.pan_no}")
        print(f"Gender: {self.gender}")
        print(f"Phone No: {self.phone_no}")
        print(f"Email ID: {self.email_id}")
        print(f"Balance: {self.balance}\n")

    
    def deposit_amount(self, acc_no, deposit_amount):
        if deposit_amount < 0:
            print("Please enter correct amount!")
            return
        try:
            total_balance = self.balance + deposit_amount
            sql = "UPDATE holder SET balance=%s WHERE acc_no=%s"
            values = (total_balance, acc_no)
            cursor.execute(sql, values)
            dbms.commit()
        except Exception:
            print("Deposit was successful but Database error occured")
        try:
            print(f"Successfully Deposited (Balance: {total_balance})")
            self.txn = "Credit"
            query = "INSERT INTO txn_details (acc_no,name,Credit_Debit,amount,balance) VALUES (%s,%s,%s,%s,%s)"
            query_val = (acc_no, self.name, self.txn, deposit_amount, total_balance)
            cursor.execute(query, query_val)
            dbms.commit()
        except Exception:
            print("Database error occured")

    def pin_set(self, acc_no):
        self.atpin_set = True
        for i in range(2, -1, -1):
            try:
                pin = input("Set the Pin :")
            except ValueError:
                if i == 0:
                    self.atpin_set = False
                    break
                print(f"please enter valid pin (remaining chances: {i})")
                continue
            else:
                if not pin.isdigit() or len(pin) != 4:
                    if i == 0:
                        self.atpin_set = False
                        break
                    print(f"Please enter only number and pin should be four digit (remaining chances: {i})")
                    continue
            break

        if not self.atpin_set:
            print("Sorry! You unable to set pin. Please try again later")
            self.atpin_set = False
            return

        pin_bytes = pin.encode('utf-8')
        hashed = bcrypt.hashpw(pin_bytes, bcrypt.gensalt())
        self.hashed_pin = hashed

        try:
            sql = "UPDATE holder SET hashed_pin=%s WHERE acc_no=%s"
            value = (self.hashed_pin, acc_no)
            cursor.execute(sql, value)
            dbms.commit()
        except Exception:
            print("Database error occured")
            self.atpin_set = False
            return
        else:
            print("Successfully Pin Set")


class Saving_account(Bank):
    def saving_withdraw(self, acc_no, withdraw_amount):
        self.withdraw_status = True
        if withdraw_amount < 0:
            print("Please enter valid amount")
            self.withdraw_status = False
            return
        if not (withdraw_amount <= self.balance):
            print(f"Insufficient Balance (Balance: {self.balance})")
            self.withdraw_status = False
            return

        for i in range(2, -1, -1):
            pin_no = input("Enter the pin no :")
            if pin_no.isdigit() and len(pin_no) == 4:
                if bcrypt.checkpw(pin_no.encode(), self.hashed_pin):
                    self.balance -= withdraw_amount
                    break
                else:
                    if i == 0:
                        self.withdraw_status = False
                        break
                    print(f"Incorrect pin re-enter (remaining chances: {i})")
            else:
                if i == 0:
                    self.withdraw_status = False
                    break
                print(f"Please enter only number and pin should be four digit (remaining chances: {i})")

        if not self.withdraw_status:
            return

        try:
            sql = "UPDATE holder SET balance=%s WHERE acc_no=%s"
            values = (self.balance, acc_no)
            cursor.execute(sql, values)
            dbms.commit()
        except Exception:
            print("Withdraw was successful but database error occured")
        try:
            self.txn = "Debit"
            sql = "INSERT INTO txn_details (acc_no,name,Credit_Debit,amount,balance) VALUES (%s,%s,%s,%s,%s)"
            values = (acc_no, self.name, self.txn, withdraw_amount, self.balance)
            cursor.execute(sql, values)
            dbms.commit()
        except Exception:
            print("Database error occured")


class Current_account(Bank):
    def current_withdraw(self, acc_no, withdraw_amount):
        self.overdraft_limit = 10000
        self.withdraw_status = True
        if withdraw_amount < 0:
            print("Please enter valid amount")
            self.withdraw_status = False
            return

        if self.balance - withdraw_amount < -self.overdraft_limit:
            print(f"Overdraft limit exceeded (Balance: {self.balance}, Limit: {self.overdraft_limit})")
            self.withdraw_status = False
            return

        for i in range(2, -1, -1):
            pin_no = input("Enter the pin no :")
            if pin_no.isdigit() and len(pin_no) == 4:
                if bcrypt.checkpw(pin_no.encode(), self.hashed_pin):
                    self.balance -= withdraw_amount
                    break
                else:
                    if i == 0:
                        self.withdraw_status = False
                        break
                    print(f"Incorrect pin re-enter (remaining chances: {i})")
            else:
                if i == 0:
                    self.withdraw_status = False
                    break
                print(f"Please enter only number and pin should be four digit (remaining chances: {i})")

        if not self.withdraw_status:
            return

        try:
            sql = "UPDATE holder SET balance=%s WHERE acc_no=%s"
            values = (self.balance, acc_no)
            cursor.execute(sql, values)
            dbms.commit()
        except Exception:
            print("Withdraw was successful but database error occured")
        try:
            self.txn = "Debit"
            sql = "INSERT INTO txn_details (acc_no,name,Credit_Debit,amount,balance) VALUES (%s,%s,%s,%s,%s)"
            values = (acc_no, self.name, self.txn, withdraw_amount, self.balance)
            cursor.execute(sql, values)
            dbms.commit()
        except Exception:
            print("Database error occured")


def details_check(acc_type):
    try:
        name = input("Enter the name : ")
        pan_no = input("Enter pan card no : ")
        age = int(input("Enter the age : "))
        gender = input("Enter the gender : ").capitalize()
        phone_no = input("Enter the phone no : ")
        email_id = input("Enter the email id : ")
    except ValueError:
        print("Please choose valid option")
        return
    else:
        if acc_type == 1:
            try:
                balance = float(input("Enter the account opening deposit (min-1000) : "))
            except ValueError:
                print("Please enter valid number :")
                return
            if age < 18:
                print("You are not eligible to open a saving account in our bank")
                return
            if not pan_no.isalnum() or len(pan_no) != 10:
                print("Please enter valid pancard details")
                return
            if not phone_no.isdigit() or len(phone_no) != 10:
                print("Please enter valid phone no")
                return
            if balance < 1000:
                print("Minimum balance should be 1000")
                return
            return [name, pan_no, age, gender, phone_no, email_id, balance]

        elif acc_type == 2:
            try:
                balance = float(input("Enter the account opening deposit (min-10000) : "))
            except ValueError:
                print("Please enter valid number :")
                return
            if age < 25:
                print("You are not eligible to open a current bank (min-25)")
                return
            if not pan_no.isalnum() or len(pan_no) != 10:
                print("Please enter valid pancard details")
                return
            if not phone_no.isdigit() or len(phone_no) != 10:
                print("Please enter valid phone no")
                return
            if balance < 10000:
                print("Minimum balance should be 10000")
                return
            return [name, pan_no, age, gender, phone_no, email_id, balance]


def get_info(acc_no):
    sql = "SELECT acc_no,acc_type,name,pan_no,age,gender,phone_no,email_id,balance FROM holder WHERE acc_no=%s"
    value = (acc_no,)
    cursor.execute(sql, value)
    data = cursor.fetchone()
    if data:
        acc = Bank(data[2], data[3], data[4], data[5], data[6], data[7], data[8])
        acc.acc_no = data[0]
        acc.acc_type = data[1]
        return acc
    else:
        print("Account not found!")
        return None


def deposit(acc_no):
    try:
        sql = "SELECT name,balance FROM holder WHERE acc_no=%s"
        value = (acc_no,)
        cursor.execute(sql, value)
        data = cursor.fetchone()
    except Exception:
        print("Details not fetched!")
    else:
        if data:
            depo_acc = Bank(data[0], None, None, None, None, None, data[1])
            return depo_acc
        else:
            print("Account not found!")
            return None


def withdraw(acc_no, withdraw_amount):
    try:
        sql = "SELECT name,acc_type,balance,hashed_pin FROM holder WHERE acc_no=%s"
        value = (acc_no,)
        cursor.execute(sql, value)
        data = cursor.fetchone()
    except Exception:
        print("Database error occurred")
        return

    if not data:
        print("Account not found!")
        return

    
    if data[3] is None:
        print("Please set pin first :")
        client_pin = Bank(None, None, None, None, None, None, None)
        client_pin.pin_set(acc_no)
        if not client_pin.atpin_set:
            print("Sorry! Couldn't set pin, try later")
            return
        
        cursor.execute("SELECT hashed_pin FROM holder WHERE acc_no=%s", (acc_no,))
        data_hashed = cursor.fetchone()
        hashed_pin_from_db = data_hashed[0].encode() 
    else:
        hashed_pin_from_db = data[3].encode() 

    
    if data[1] == "Saving_account":
        client = Saving_account(data[0], None, None, None, None, None, data[2], hashed_pin_from_db)
        client.saving_withdraw(acc_no, withdraw_amount)
        if not client.withdraw_status:
            print("Sorry! Withdraw was unsuccessful")
            return
        else:
            print(f"Withdraw was successful (Balance: {client.balance})")
    elif data[1] == "Current_account":
        client = Current_account(data[0], None, None, None, None, None, data[2], hashed_pin_from_db)
        client.current_withdraw(acc_no, withdraw_amount)
        if not client.withdraw_status:
            print("Sorry! Withdraw was unsuccessful")
            return
        else:
            print(f"Withdraw was successful (Balance: {client.balance})")




def view_txn_details(acc_no):
    sql = "SELECT * FROM txn_details WHERE acc_no=%s ORDER BY txn_no DESC"
    value = (acc_no,)
    cursor.execute(sql, value)
    print("How many transaction you want: \n1. By no of transaction \n2. All")
    try:
        choose = int(input("Enter the option :"))
    except ValueError:
        print("Please enter valid option")
        return
    column = ("txn_no", "acc_no", "name", "Credit_Debit", "amount", "balance", "txn_date")
    if choose == 1:
        try:
            list_txn = int(input("Enter how many txn detials you want : "))
        except ValueError:
            print("Please enter valid no")
            return
        data = cursor.fetchmany(list_txn)
    elif choose == 2:
        data = cursor.fetchall()
    else:
        print("Please choose from the given option!")
        return
    if data:
        print(column)
        for row in data:
            print(row)
        print("------------")
    else:
        print("No transaction found!")
