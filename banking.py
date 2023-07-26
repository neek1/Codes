class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self):
        self.name = input("Enter the new name: ")

    def change_pin(self):
        self.pin = input("Enter the new pin: ")

    def change_password(self):
        self.password = input("Enter the new password: ")

# Create a subclass of the User superclass
class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0
        self.withdraw_amt = 0
        self.deposit_amt = 0
        '''self.rec_user = None'''
        '''self.transfer_amt = 0'''
        
    # Create methods for BankUser subclass
    def show_balance(self):
        print(self.name, "has a balance of:", self.balance)

    def deposit(self, deposit_amt):
        self.deposit_amt = deposit_amt
        if self.deposit_amt == 0:
            self.deposit_amt = float(input("Enter the amount to deposit: "))
        self.balance += deposit_amt
        print(self.name, "has a balance of:", self.balance)

    def withdraw(self, withdraw_amt):
        self.withdraw_amt = withdraw_amt
        if self.withdraw_amt == 0:
            self.withdraw_amt = float(input("Enter the amount to withdraw: "))
        self.balance -= self.withdraw_amt
        print(self.name, "has a balance of:", self.balance)

    def transfer_money(self, rec_user):
        self.rec_user = rec_user
        self.transfer_amt = float(input("Enter the amount you would like to transfer: "))
        print("You would like to transfer", self.transfer_amt, "to", self.rec_user.name) 
        print("Authentication Required")
        transfer_pin = input("Enter your pin: ")
        if int(transfer_pin) == self.pin:
            print("Transfer Authorized")
            print("Transferring", self.transfer_amt, "to", self.rec_user.name)
            self.withdraw(self.transfer_amt)
            rec_user.deposit(self.transfer_amt)
            return True
        else:
            print("Invalid pin. Transaction canceled.")
            return False

    def request_money(self, sender):
        self.sender = sender
        self.send_amt = float(input("Enter the amount you would like to request: "))
        print("You are requesting", self.send_amt, "from", self.sender.name )
        print("User Authentication Required")
        pin = input("Enter " + self.sender.name + "'s pin: " )
        if int(pin) == self.sender.pin:
            password = input("Enter your Password: ")
            if password == self.password:
                print("Request Authorized")
            else:
                print("Invalid password. Transaction canceled")
                return False
        else:
            print("Invalid pin. Transaction cancled")
            return False
        sender.withdraw(self.send_amt)
        self.deposit(self.send_amt)
        


    


""" Driver Code for Task 1
user1 = User("Tom", 1234, "password1234")
print(user1.name, user1.pin, user1.password)"""


"""Driver Code for Task 2
user1 = User("Tom", 1234, "password1234")
print(user1.name, user1.pin, user1.password)

user1.change_name()
user1.change_pin()
user1.change_password()
print(user1.name, user1.pin, user1.password)"""


"""Driver Code for Task 3
user2 = BankUser("Jerry", 9876, "password9876")
print(user2.name, user2.pin, user2.password, user2.balance)"""

"""Driver Code for Task 4
user2 = BankUser("Jerry", 9876, "password9876")
user2.show_balance()
user2.withdraw_amt =50
print(user2.withdraw_amt, user2.deposit_amt)
user2.deposit(user2.deposit_amt)
user2.withdraw(user2.withdraw_amt)"""

"""Driver Code for task 5"""
user1 = BankUser("Tom", 1234, "password1234")
user2 = BankUser("Jerry", 9876, "password9876")
user2.transfer_money(user1)
user2.request_money(user1)
