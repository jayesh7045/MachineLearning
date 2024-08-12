import re

def validate_email(email):
    # Define a regular expression pattern for a basic email validation
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Use re.match to check if the email matches the pattern
    if re.match(pattern, email):
        return True
    else:
        return False

# Example usage
email = 'example@example.com'
if validate_email(email):
    print(f"'{email}' is a valid email address.")
else:
    print(f"'{email}' is not a valid email address.")