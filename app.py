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
        "Do ensure, you're selecting the right options using outlined number\n\n".center(30, " "))



def main():
    """
    main method for application
    """
    bank = Bank()
    flag = True
    # -----
    #   DISPLAY WELCOME MESSAGE AND HOW BANK MAY HELP USER
    # -----
    print(f"welcome to {bank.BANK_NAME}\n".center(50, " "))
    print(bank.how_can_we_help())
    
    while flag:
        response = _user_response_controller(
                        bank.BANK_REQUESTS.get('hcwh'), 
                        input_prompt())
        
        if isinstance(response, list):
            if response[0] == 'resend_same_bank_request':
                reason_for_resend(response[1])

        else:
            print(response)
            break;



if __name__ == "__main__":
    main()
