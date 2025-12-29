import time
from bank import *

if __name__ == "__main__":
    running = True

    while running:
        print("\nWelcome to our bank!")
        time.sleep(1)
        print(
            "\n1. Open Account"
            "\n2. View Account Details"
            "\n3. Deposit"
            "\n4. Withdraw"
            "\n5. View Transaction Details"
            "\n6. Exit\n"
        )

        try:
            choose = int(input("Select one option: "))
        except ValueError:
            print("\nPlease choose a valid option\n")
            time.sleep(1)
            continue

      
        if choose == 1:
            print("\n1. Saving Account \n2. Current Account\n")
            try:
                choose_type = int(input("Enter account type: "))
            except ValueError:
                print("\nPlease choose a valid option\n")
                continue

            acc_create = details_check(choose_type)
            if not acc_create:
                print("\nAccount creation failed!\n")
                continue

            name, pan_no, age, gender, phone_no, email_id, balance = acc_create

            if choose_type == 1:
                client = Saving_account(name, pan_no, age, gender, phone_no, email_id, balance)
                client.acc_type = "Saving_account"
            elif choose_type == 2:
                client = Current_account(name, pan_no, age, gender, phone_no, email_id, balance)
                client.acc_type = "Current_account"
            else:
                print("Invalid account type")
                continue

            client.acc_details_insertion()
            if client.status:
                print("\nAccount created successfully!\n")
            else:
                print("\nAccount creation failed (DB error)\n")

      
        elif choose == 2:
            try:
                acc_no = int(input("Enter account no: "))
            except ValueError:
                print("Invalid account number")
                continue

            acc = get_info(acc_no)
            if acc:
                acc.show_details()

       
        elif choose == 3:
            try:
                acc_no = int(input("Enter account number: "))
                deposit_amount = float(input("Enter the amount: "))
            except ValueError:
                print("Invalid input")
                continue

            depo_acc = deposit(acc_no)
            if depo_acc:
                depo_acc.deposit_amount(acc_no, deposit_amount)

       
        elif choose == 4:
            try:
                acc_no = int(input("Enter the account no: "))
                withdraw_amount = float(input("Enter the withdraw amount: "))
            except ValueError:
                print("Invalid input")
                continue

            withdraw(acc_no, withdraw_amount)

        
        elif choose == 5:
            try:
                acc_no = int(input("Enter the account no: "))
            except ValueError:
                print("Invalid account number")
                continue

            view_txn_details(acc_no)

        
        elif choose == 6:
            print("\nExiting.....\n")
            time.sleep(1)
            running = False

        else:
            print("Please choose a valid option")

cursor.close()
dbms.close()
