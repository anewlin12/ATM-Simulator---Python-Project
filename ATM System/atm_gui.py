#These imports the essential classes and methods needed to access the,
#methods for handling the csv data and GUI.
import tkinter as tk
from tkinter import messagebox, simpledialog
from account_data import find_account, update_account_balance


#This class starts by starting a new window, it also holds the different methods used to handle the GUI.
class ATMGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.show_login_screen()
        print("TEST New Window Created")
    
#This method shows the first screen at the start of the program.
#This is the login page that you enter the user's account number and pin.
    def show_login_screen(self):

        
        self.window.title("Anthony's ATM Machine")
        self.window.geometry("800x600")
        self.window.resizable(False, False)
        self.window.configure(bg="#4c91ca")
        self.welcome_image = tk.PhotoImage(file="Graphics/welcome.png")
        self.accounts_sheet_image = tk.PhotoImage(file="Graphics/Accounts.png")

        accounts_sheet = tk.Label(self.window, image=self.accounts_sheet_image, bg="#4c91ca")
        accounts_sheet.place(x="8", y="250")
        
        title = tk.Label(self.window, image=self.welcome_image, bg="#4c91ca")
        title.pack(pady=70)
        
        account_label = tk.Label(self.window, text="Account Number:", font=("Arial", 24), bg="#4c91ca")
        account_label.pack()

        self.account_entry = tk.Entry(self.window, font=("Aria", 20), bg="#ffffff")
        self.account_entry.pack()

        pin_label = tk.Label(self.window, text="Pin Number:",font=("Arial", 24), bg="#4c91ca")
        pin_label.pack()
        
        self.pin_entry = tk.Entry(self.window, font=("Arial", 20), bg="#ffffff", show="*")
        self.pin_entry.pack()

        login_button = tk.Button(self.window, text="Login", font=("Arial", 22), bg="#c5c5c5", command=self.login_clicked)
        login_button.pack()
        
        self.account_entry.focus_set()
        print("TEST Login Screen Created")

#This method is the validation for the login page, it checks if the user == the csv data using the find_account method.
#If the account is found it will log the user in to the program and set the current user = to the account number and pin entered.
    def login_clicked(self):
        
        account_number = self.account_entry.get()
        pin = self.pin_entry.get()
        account = find_account(account_number, pin)

        if not account_number or not pin:
            messagebox.showerror("Error", "Please Enter an Account Number and Pin")
            return
        if account:
            self.current_account = account
            self.show_menu()
            print(f"TEST Account {account_number} has been found.")
        else:
            messagebox.showerror("Error", "Invalid Account Number or Pin")
        
#This method will show the main menu of the program after the user is validated.
#It starts by removing all the widgets and UI in the window, then it creates new labels and buttons for the different options.
    def show_menu(self):
        
        for widget in self.window.winfo_children():
            widget.destroy()
            
        welcome_user_label = tk.Label(self.window, text=f"Welcome, {self.current_account.name}!", font=("Arial Bold", 25), bg="#4c91ca")
        welcome_user_label.place(x="20",y="55")
            
        #Check Balance Button
        self.check_balance_image = tk.PhotoImage(file="Graphics/Balance.png")
        check_balance_button = tk.Button(self.window, relief="flat", borderwidth=0, highlightthickness=0, image=self.check_balance_image, command=self.check_balance)
        check_balance_button.place(x="10", y="315")
        
        #Deposit Button
        self.deposit_image = tk.PhotoImage(file="Graphics/Deposit.png")
        deposit_button = tk.Button(self.window, relief="flat", borderwidth=0, highlightthickness=0, image=self.deposit_image, command=self.deposit)
        deposit_button.place(x="515", y="50")
        
        #Get Cash (withdraw) Button
        self.withdraw_image = tk.PhotoImage(file="Graphics/Withdraw.png")
        withdraw_button = tk.Button(self.window, relief="flat", borderwidth=0, highlightthickness=0, image=self.withdraw_image, command=self.withdraw)
        withdraw_button.place(x="275", y="315")

        #Signout Button
        self.signout_image = tk.PhotoImage(file="Graphics/Exit.png")
        signout_button = tk.Button(self.window, relief="flat", borderwidth=0, highlightthickness=0, image=self.signout_image, command=self.signout)
        signout_button.place(x="10", y="210")

#This will be the function attached to the check balance button.
    def check_balance(self):
        balance = self.current_account.check_balance()
        messagebox.showinfo("Balance", f"Your balance is ${balance:.2f}")

#This will be the function attached to the deposit button.
    def deposit(self):
        amount = simpledialog.askfloat("Deposit", "Enter deposit amount:", minvalue=0.01)
        if amount is not None:
            if self.current_account.deposit(amount):
                update_account_balance(self.current_account.account, self.current_account.balance)
                messagebox.showinfo("Success", f"Successfully deposited ${amount:.2f}\nNew balance: ${self.current_account.balance:.2f}")
            else:
                messagebox.showerror("Error", "Invalid amount")

#This will be the function attached to the Get Cash (withdraw) button.
    def withdraw(self):  
        amount = simpledialog.askfloat("Withdraw", "Enter withdrawal amount:", minvalue=0.01)
        if amount is not None:
            if self.current_account.withdraw(amount):
                update_account_balance(self.current_account.account, self.current_account.balance)
                messagebox.showinfo("Success", f"Successfully withdrew ${amount:.2f}\nNew balance: ${self.current_account.balance:.2f}")
            else:
                messagebox.showerror("Error", "Insufficient funds or invalid amount")

#This will be the function attached to the check balance button.
    def signout(self):
        for widget in self.window.winfo_children():
            widget.destroy()
        print("TEST You have signed out... Goodbye :)")
        self.show_login_screen()
        self.current_account = None

#This method will be used in the main.py script which starts the window and keeps it running.
    def run(self):
        self.window.mainloop()