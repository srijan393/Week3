pass1 = input("Enter a new password (8-12 characters only): ")
if 8 <= len(pass1) <=12:
    pass2 = input("Confirm your password: ")
    if pass1 == pass2:
        print("Password Set")
    else:
        print("Error: Passwords do not match. Please try again.")
else:
    print("error: password must be between 8-12 characters")
    
