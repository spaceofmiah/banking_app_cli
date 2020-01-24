from utility.utils import (
	reason_for_resend, 
	validate_user_input_to_int, 
	input_prompt
)


def create_bank_account_helper(bank):
	print("Do fill in your correct details for account creation\n")
	                               
	print("Email:")
	u_email = input_prompt()
	print("Name: ")
	u_name = input_prompt()
	print("Password: ")
	u_pass = input_prompt()
	print("Amount to deposit: ")
	a_amount = input_prompt()

	validity_response = validate_user_input_to_int(a_amount)

	# check the validity of the value entered as amount
	if validity_response == "error":
	    reason_for_resend("Invalid Amount -- Amount should be a number")
	    return False

	return bank.process_account_creation(u_name, u_email, u_pass, validity_response)


def authenticate_an_account_helper(bank):
	print("Please insert your correct login credentials")
	print("Email:")
	u_email = input_prompt()
	print("Password: ")
	u_pass = input_prompt()

	return bank.process_user_authentication(u_email, u_pass)