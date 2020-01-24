"""
This file serves as the entry point for application
"""
from bank.bank import Bank






def input_prompt():
    """
    renders display for receiving user input
    """
    return input(">>> ")


def _user_response_controller(bank_request, user_response):
    """
    processes user's response for bank's request sent
    : bank_request --> what is user currently requesting for 
    : user_response --> what a user wants to actually do amongst the options in the
              above bank_requests
    """
    user_response = _validate_user_input_to_int(user_response)

    if user_response == "error":
        return ['resend_same_bank_request', 'No valid option choosen']

    if user_response >= 1 and user_response <= bank_request.get('available_options'):
        return user_response
    else:
        return ['resend_same_bank_request', 'Selected option not found']


def _validate_user_input_to_int(user_input):
    """
    validates user input against type integer & automatically converts and returns the value
    : user_input --> value entered by user
    """
    try:
        return int(user_input)
    except Exception:
        return "error"

        
def reason_for_resend(why):
    print("ERROR ERROR".center(60, " "))
    print(why.center(61, " "))
    print(
        "Do ensure, you're inserting the right options as needed\n\n".center(30, " "))



def main():
    """
    main method for application
    """
    bank = Bank()
    flag = True

    while flag:
        # -----
        #   DISPLAY WELCOME MESSAGE AND HOW BANK MAY HELP USER
        # -----
        print(f"welcome to {bank.BANK_NAME}\n".center(50, " "))
        print(bank.how_can_we_help())
    
        response = _user_response_controller(
                        bank.BANK_REQUESTS.get('hcwh'), 
                        input_prompt())
        
        if isinstance(response, list):
            if response[0] == 'resend_same_bank_request':
                reason_for_resend(response[1])

        else:
            if response == 1:

                # -----
                #    CREATE BANK ACCOUNT
                #       this process should continue until user stops it by his reponse
                #       or successfully create a bank account
                # -----
                
                account_creation_flag = True
                while account_creation_flag:
                    print("Do fill in your correct details for account creation\n")
                    
                    
                    print("Email: ")
                    u_email = input_prompt()
                    print("Name: ")
                    u_name = input_prompt()
                    print("Password: ")
                    u_pass = input_prompt()
                    print("Amount to deposit: ")
                    a_amount = input_prompt()
                    
                    validity_response = _validate_user_input_to_int(a_amount)

                    # check the validity of the value entered as amount
                    if validity_response == "error":
                        reason_for_resend("Invalid Amount -- Amount should be a number")

                    else:
                        creation_response = bank.process_account_creation(
                            u_name, u_email, u_pass, validity_response)
                        
                        # if account creation is successful
                        if creation_response[0]:
                            print(creation_response[1])
                            account_creation_flag = False

                        # on an errorneous account creation
                        else:
                            reason_for_resend(creation_response[1])
                
            elif response == 2:
                
                authentication_flag = True
                while authentication_flag:

                    # ----
                    #   FIRST AUTHENTICATE THE ACCOUNT
                    #       Before a user can perform any transaction, they first need to be
                    #       authenticated
                    # ----

                    print("Please insert your correct login credentials")
                    print("Email:")
                    u_email = input_prompt()
                    print("Password: ")
                    u_pass = input_prompt()

                    auth_response = bank.process_user_authentication(u_email, u_pass)


                    # when auth credentials fails to authenticate, display why and  
                    # re-initiate the login process

                    if auth_response[0] == False:
                        reason_for_resend(auth_response[1])

                    # when auth credentials passes authentication, then display available
                    # transactions that can be processed by the authenticated user
                    else:

                        transaction_flag = True
                        while transaction_flag:
                            # ------
                            # PROCESS USER TRANSACTIONS
                            #   process reponse of user for transaction computations
                            # ------
                            print(bank.get_core_transactions())
                            response = _user_response_controller(
                                bank.BANK_REQUESTS.get('trans'),
                                input_prompt())

                            # if a user doesn't choose the correct outlisted option
                            if isinstance(response, list):
                                if response[0] == "resend_same_bank_request":
                                    reason_for_resend(response[1])

                            # if a user chooses correct outlisted option
                            else:

                                # check balance
                                if response == 1:
                                    print(f"Your current balance is: {bank.get_user_account_balance()}")

                                # process withdrawal
                                elif response == 2:
                                    process_withdrawal_flag = True

                                    # -----
                                    #   PROCESS WITHDRAWAL
                                    #       this process will continue until user inputs
                                    #       a valid detail or cancel operation
                                    # -----
                                    while process_withdrawal_flag:
                                        print("Fill in details appropriately to process withdrawal")
                                        print("Amount to withdraw :")
                                        withdraw_amt = _validate_user_input_to_int(input_prompt())
                                        print("Enter password to proceed")
                                        withdraw_pass = input_prompt()


                                        if withdraw_amt == 'error':
                                            reason_for_resend('Invalid amount specified')
                                        
                                        else:
                                            withdrawal_response = bank.process_user_withdraw(withdraw_amt, withdraw_pass)
                                            if withdrawal_response[0]:
                                                print(withdrawal_response[1])
                                                process_withdrawal_flag = False

                                            else:
                                                reason_for_resend(withdrawal_response[1])






                                # process transfer
                                elif response == 3:
                                    print("We'll definitely process your transaction")
                                    break
                            break 

                    break

                        





if __name__ == "__main__":
    main()
