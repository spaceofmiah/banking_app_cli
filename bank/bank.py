"""
This file contains bank processes
"""

from utility.utils import validate_email


class Account:

    def __init__(self, name, email, password, balance):

        if validate_email(email):
            self.account_name = name
            self.account_email = email
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
        validate_email(new_email)
        if self.email == old_email:
            if self.password == password:
                self.email = new_email
                return True
            else:
                return [False, "password does not match"]
        else:
            return [False, "email does not match"]
        

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
        return self.account_balance

        



class Bank:
    
    def __init__(self):

        self.BANK_NAME = "Miah's Bank"
        self.ACCOUNTS = dict()
        self.authenticated_account = None

        # ** REFACTOR SPOT
        #   This dictionary could also be refactored to hold the questions
        #   as a list e.g 
        #       'hwch': {
        #           'options': ['create account', 'transactions']
        #           'available_options' : len(options)
        #       }
        # ** REFACTOR SPOT
        self.BANK_REQUESTS = { 
           'hcwh': {
                "meaning" : "HOW CAN WE HELP",
                "available_options" : 2,
           },
        
           'trans': {
                "meaning" : "TRANSACTION",
                "available_options": 3,
           },
        } 
        

    def how_can_we_help(self):
        actions = """1. create account   \n2. transaction\n"""
        return actions

    def get_core_transactions(self):
        transactions = """1. check balance  \n2. withdraw    \n3. transfer  \n"""
        return transactions

    def get_user_account_balance(self):
        """
        returns an account balance
        """
        return self.authenticated_account.account_balance

    def process_user_withdraw(self, amount, password):
        """
        withdraws an amount from a given account
        : amount --> the amount to be withdrawn from the account
        : password --> the password of the account on which withdrawal is to be made
        """
        pass

    def process_account_creation(self, name, email, password, balance=0):
        """
        creates and return a bank account
        """
        if self.ACCOUNTS.get(email, False):
            return [False, 'there is already an account with same email provided']
        
        account = Account(name, email, password, balance)
        self.ACCOUNTS[email] = account
        return [True, 'account created successfully', account]
        

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
        : email --> email of the account to be signed on
        : password --> password of an account
        """
        if validate_email(email):
            self.authenticated_account = self.ACCOUNTS.get(email, None)
            if self.authenticated_account:
                if self.authenticated_account.account_password == password:
                    return [True, 'successfully authenticated']
                else:
                    return [False, 'invalid password']
            else:
                return [False, 'no account found with provided credentials']
        return [False, 'password not in a valid format']


