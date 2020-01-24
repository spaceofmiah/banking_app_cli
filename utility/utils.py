"""
This file contains helper methods
"""



def validate_email(email):
    if '@' in email and '.com' in email:
        return True
    raise ValueError("Invalid email address -- " + email)
