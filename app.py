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

                while True:
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
                            break

                        # on an errorneous account creation
                        else:
                            reason_for_resend(creation_response[1])
                







if __name__ == "__main__":
    main()
