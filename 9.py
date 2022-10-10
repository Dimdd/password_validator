def valid_pass(passw):
    digit_counter = 0
    pass_valid = True
    if len(passw) > 10 or len(passw) < 6:     #the password must be between 6 and 10 charachters
        pass_valid = False
        print("Password must be between 6 and 10 characters")

    for characthers in passw:
        if characthers.isdigit():
            digit_counter += 1
        if characthers in "@_!#$%^&*()<>?/\|}{~:": #the password must not contain special charachters
            pass_valid = False
            print("Password must consist only of letters and digits")
    if digit_counter < 2:                          #the password must contain atleast 2 digits
        print("Password must have at least 2 digits")
        pass_valid=False
    return pass_valid
password = input()
pass_valid = valid_pass(password)

if pass_valid:
    print("Password is valid")

