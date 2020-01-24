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
    return [user_response, bank_request.get('available_options')]


def _validate_user_input_to_int(user_input):
    """
    validates user input against type integer & automatically converts and returns the value
    : user_input --> value entered by user
    """
    try:
        return int(user_input)
    except Exception:
        return "error"

        
        



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
        
        user_input = response[0]
        request_option_len = response[1]


        if user_input >= 1 and user_input <= request_option_len:
            print("Nice computation")
            flag = False


        else:
            print("Bad computation")
            break;





if __name__ == "__main__":
    main()
