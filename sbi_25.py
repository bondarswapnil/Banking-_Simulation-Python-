'''
Author - Swapnil Bondar
Description - Console Based application
              For Account Create(with use random number),
              Deposit Amount, Mini Statement, Withdraw Amount
Date- 25-11-2022

'''
import sys
import random
import pandas as pd
from datetime import date

try:

    balance = 0.0
    listings = []
    date_now = str(date.today())
    tempAccountNumber = random.randint(111111111111,999999999999)
    
    print("******* Welcome To State Bank of India *******")

    while True:
        print("\n******************* MENU *********************")
        print("1] Create Account \n2] Deposit Money \n3] Withdraw Money \n4] Transaction Statement \n5] Exit")

        choice = input("\nEnter Your Choice = ")
        if choice == '1':
            print("\n*** Account Creation For New Users ***")
            name = input("Enter Your Full Name = ")
            age = int(input("Enter Your Age = "))
            aadharNumber = int(input("Enter Your Aadhar Card Number = "))
            panNumber = input("Enter Your PAN Card Number = ")
            gender = input("Enter Your Gender (Male/Female/Other) = ")
            email = input("Enter Your E-Mail ID = ")
            pwd = input("Enter password: ")
            conf_pwd = input("Confirm password: ")
            if conf_pwd == pwd:
                with open(f"{tempAccountNumber}.txt", "w") as f:
                    f.write(email + "\n")
                    f.write(pwd)
                f.close()
                print("You have registered successfully!")
            else:
                    print("Password is not same as above! \n")
            deposit = float(input("Enter Amount To be Deposited (Min. Rs.500) = Rs. "))
            if deposit>=500:
                balance += deposit
                print("\n_________ Account Has Been Created _________")
                print(f"Account No. = {tempAccountNumber}\t\tGender = {gender}")
                print(f"Name = {name}\t\tAge = {age}")
                print(f"Aadhar Number = {aadharNumber}")
                print(f"Pan Card Number = {panNumber}")
                print(f"Total Balance = Rs. {balance}")

                firstDeposit = str(deposit) + " (Credited) " + date_now
                listings.append(firstDeposit)
                df = pd.DataFrame({'Transaction': listings})
                writer = pd.ExcelWriter(f'{tempAccountNumber}.xlsx', engine='xlsxwriter')
                df.to_excel(writer, sheet_name='Sheet1', index=False)
                writer.close()
            else:
                print("Minimun Balance Must be Rs.500")

        elif choice == '2':
            print("\n*** Money Deposition ***")
            newDeposit = float(input("Enter Amount To Be Deposited = Rs. "))
            balance += newDeposit
            print(f"Total Balance = Rs. {balance}")
            newDepositCr = str(newDeposit) + " (Credited) " + date_now
            listings.append(newDepositCr)
            df = pd.DataFrame({'Transaction': listings})
            writer = pd.ExcelWriter(f'{tempAccountNumber}.xlsx', engine='xlsxwriter')
            df.to_excel(writer, sheet_name='Sheet1', index=False)
            writer.close()

        elif choice == '3':
            print("\n*** Money Withdrawal ***")
            newWithdraw = float(input("Enter Amount Of Withdrawal = Rs. "))
            if newWithdraw < balance:
                balance -= newWithdraw
                print(f"Total Balance = Rs. {balance}")
                newWithdrawDb = str(newWithdraw) + " (Debited) " + date_now
                listings.append(newWithdrawDb)
                df = pd.DataFrame({'Transaction': listings})
                writer = pd.ExcelWriter(f'{tempAccountNumber}.xlsx', engine='xlsxwriter')
                df.to_excel(writer, sheet_name='Sheet1', index=False)
                writer.close()
            else :
                print("Low Balance !")

        elif choice == '4':
            print("\n*** Transaction Statement ***")
            print("____Login to See Details____")
            filer = input("Enter Account Number = ")
            email = input("Enter email: ")
            pwd = input("Enter password: ")
            with open(f"{filer}.txt", "r") as f:
                stored_email, stored_pwd = f.read().split("\n")
                f.close()
            if email == stored_email and pwd == stored_pwd:
                print("Logged in Successfully!")
                reader = pd.read_excel(f'{filer}.xlsx')
                print("\n________________________________________________")
                print(reader)
                print("________________________________________________")
            else:
                print("Login failed! \n")
            
            

        elif choice == '5':
            print("Thank You For Choosing Our Bank ....")
            sys.exit()

        else:
            print("\n_______ Enter A Valid Choice ! _______")

except BaseException as ex:
    print(ex)