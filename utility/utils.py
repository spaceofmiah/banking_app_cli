"""
This file contains helper methods
"""



def validate_email(email):
    if '@' in email and '.com' in email:
        return True
    raise ValueError("Invalid email address -- " + email)


def input_prompt():
    """
    renders display for receiving user input
    """
    return input(">>> ")


def user_response_controller(bank_request, user_response):
    """
    processes user's response for bank's request sent
    : bank_request --> what is user currently requesting for 
    : user_response --> what a user wants to actually do amongst the options in the
              above bank_requests
    """
    user_response = validate_user_input_to_int(user_response)

    if user_response == "error":
        return ['resend_same_bank_request', 'No valid option choosen']

    if user_response >= 1 and user_response <= bank_request.get('available_options'):
        return user_response
    else:
        return ['resend_same_bank_request', 'Selected option not found']


def validate_user_input_to_int(user_input):
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
