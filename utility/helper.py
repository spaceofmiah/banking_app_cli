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


def withdrawal_helper(bank):
	print("Fill in details appropriately to process withdrawal")
	print("Amount to withdraw :")
	withdraw_amt = input_prompt()
	print("Enter password to proceed")
	withdraw_pass = input_prompt()

	return bank.process_user_withdraw(withdraw_amt, withdraw_pass)


def tranfer_amount_helper(bank):
	print("Fill details appropriately to process transfer")
	print("Enter beneficiary's email: ")
	to_account_email = input_prompt()
	print("Enter amount: ")
	trans_amount = input_prompt()
	print("Enter password to proceed: ")
	from_account_pass = input_prompt()

	return bank.process_user_transfer(to_account_email, trans_amount, from_account_pass)