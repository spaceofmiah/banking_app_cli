"""
This file contains bank processes
"""


class Account:

    def __init__(self, name, email, password, balance=0):
        self.account_name = name,
        self.account_email = email,
        self.account_password = password
        self.account_balance = balance

    def set_account_name(self, new_name, password):
        """
        changes an account name
        : new_name --> the new name of the account
        : password --> the account password
        """
        pass

    def set_account_email(self, old_email, new_email, password):
        """
        changes an account email address
        : old_email --> the current email address to be changed
        : new_email --> the new email address 
        : password --> the password for the account
        """
        pass

    def set_account_balance(self, amount):
        """
        set or update an account balance
        : amount --> the amount to be set or used in updating current balance
        """
        pass

    def change_password(self, old_password, new_password, confirm_password):
        """
        changes password for an account
        : old_password --> the current password of the account
        : new_password --> the new password of the account
        : confirm_password --> same as the new password

        new_password and current_password must match
        """
        pass

    def get_account_name(self):
        """
        returns an account name
        """
        return self.account_name

    def get_account_email(self, password):
        """
        returns an account email
        : password --> the password of the account
        """
        return self.account_email

    def get_account_balance(self, password):
        """
        return an account balance
        : password --> the password of the account
        """
        return sefl.account_balance

        



class Bank:
    
    def __init__(self):

        self.BANK_NAME = "Miah's Bank"
        

    def get_main_actions(self):
        actions = """               \n
        1. create account           \n
        2. transaction              \n
        """
        return actions

    def get_core_transactions(self):
        transactions = """
        1. check balance            \n
        2. withdraw                 \n
        3. transfer                 \n
        """
        return transactions

    def get_user_account_balance(self, password):
        """
        returns an account balance
        : password --> the password of the account whose balance is to be seen
        """
        pass

    def process_user_withdraw(self, amount, password):
        """
        withdraws an amount from a given account
        : amount --> the amount to be withdrawn from the account
        : password --> the password of the account on which withdrawal is to be made
        """
        pass

    def process_user_transfer(self, to_account_email, amount, from_account_password):
        """
        processes transfer of an amount from a given account to another account
        : to_account_email --> the email of the account an receiving the transfer
        : amount --> the amount to be transfered
        : from_account_password --> password of the account making the transfer
        """
        pass

    def process_user_authentication(self, email, password):
        """
        enable a user to be able to view transactions
        : email
        """
        pass


