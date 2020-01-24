"""
This file serves as the entry point for application
"""
from bank.bank import Bank
from utility.utils import user_response_controller, reason_for_resend, input_prompt

from utility.helper import (
    create_bank_account_helper,
    authenticate_an_account_helper,
    withdrawal_helper,
    tranfer_amount_helper
)



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
    
        response = user_response_controller(
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
                    creation_response = create_bank_account_helper(bank)

                    if isinstance(creation_response, list):
                        # if account creation is successful
                        if creation_response[0]:
                            print(creation_response[1])
                            account_creation_flag = False
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

                    auth_response = authenticate_an_account_helper(bank)

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
                            response = user_response_controller(
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
                                        
                                        withdrawal_response = withdrawal_helper(bank)
                                        if withdrawal_response[0]:
                                            print(withdrawal_response[1])
                                            process_withdrawal_flag = False

                                        else:
                                            reason_for_resend(withdrawal_response[1])

                                # process transfer
                                elif response == 3:
                                    
                                    # ------
                                    #   PROCESS FUND TRANSFER
                                    #       this process will continue until user inputs
                                    #       a valid detail or cancel operation
                                    # ------
                                    
                                    process_transfer_flag = True
                                    while process_transfer_flag:

                                        transfer_response = tranfer_amount_helper(bank)

                                        # if transfer is successful
                                        if transfer_response[0]:
                                            print(transfer_response[1])
                                            process_transfer_flag = False

                                        # if transfer is unsuccessful
                                        else:
                                            reason_for_resend(transfer_response[1])


                                
                                break 

                    break

                        





if __name__ == "__main__":
    main()
