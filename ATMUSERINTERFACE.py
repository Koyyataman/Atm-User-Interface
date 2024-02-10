import tkinter as tk
from tkinter import messagebox, simpledialog

class ATMInterface:
    def __init__(self, master, account_number, pin):
        self.master = master
        self.master.title("ATM User Interface")

        self.balance = 1000  # Initial balance for demonstration purposes
        self.pin = pin
        self.account_number = account_number

        self.logged_in = False  # Flag to track if the user is logged in

        # Ask for account number initially
        self.validate_account()

    def validate_account(self):
        entered_account_number = simpledialog.askstring("Account Number", "Enter your account number:")
        if entered_account_number == self.account_number:
            self.logged_in = True
            messagebox.showinfo("Login Successful", "Account number verified. You are now logged in.")
            self.setup_ui()  # Display UI options after successful login
        else:
            messagebox.showerror("Invalid Account Number", "Invalid account number. Exiting.")
            self.master.destroy()

    def setup_ui(self):
        # Buttons
        self.button_deposit = tk.Button(self.master, text="Deposit", command=self.deposit)
        self.button_deposit.pack(pady=5)

        self.button_withdraw = tk.Button(self.master, text="Withdraw", command=self.withdraw)
        self.button_withdraw.pack(pady=5)

        self.button_balance = tk.Button(self.master, text="Balance Enquiry", command=self.check_balance)
        self.button_balance.pack(pady=5)

        self.button_mini_statement = tk.Button(self.master, text="Mini Statement", command=self.mini_statement)
        self.button_mini_statement.pack(pady=5)

        self.button_pin_change = tk.Button(self.master, text="Pin Change", command=self.pin_change)
        self.button_pin_change.pack(pady=5)

    def deposit(self):
        if self.logged_in and self.validate_pin():
            amount = float(simpledialog.askstring("Deposit", "Enter deposit amount:"))
            if amount > 0:
                self.balance += amount
                self.update_balance()

    def withdraw(self):
        if self.logged_in and self.validate_pin():
            amount = float(simpledialog.askstring("Withdraw", "Enter withdrawal amount:"))
            if amount > 0 and amount <= self.balance:
                self.balance -= amount
                self.update_balance()
            else:
                messagebox.showwarning("Invalid Withdrawal", "Insufficient funds or invalid amount.")

    def check_balance(self):
        if self.logged_in and self.validate_pin():
            messagebox.showinfo("Balance Enquiry", "Your balance is: $"+str(self.balance))

    def mini_statement(self):
        if self.logged_in and self.validate_pin():
            # Implement mini statement logic here
            messagebox.showinfo("Mini Statement", "Transaction history:\n1. Deposit: $100\n2. Withdrawal: $50")

    def pin_change(self):
        if self.logged_in and self.validate_pin():
            new_pin = simpledialog.askstring("Pin Change", "Enter new PIN:")
            if new_pin:
                self.pin = new_pin
                messagebox.showinfo("Pin Change", "PIN changed successfully.")

    def update_balance(self):
        self.label_balance.config(text="Balance: $"+str(self.balance))

    def validate_pin(self):
        entered_pin = simpledialog.askstring("Enter PIN", "Enter your PIN:")
        if entered_pin == self.pin:
            return True
        else:
            messagebox.showerror("Wrong PIN", "Wrong PIN entered. Please try again.")
            return False


if __name__ == "__main__":
    fixed_account_number = "123456789"
    fixed_pin = "4321"

    root = tk.Tk()
    app = ATMInterface(root, fixed_account_number, fixed_pin)
    root.mainloop()
