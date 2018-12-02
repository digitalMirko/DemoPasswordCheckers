# this is a password checker demo
# In this demo the user is prompted for the password
# if they answer correctly, they are granted access
# if they answer incorrectly, access is denied

def passwordChecker(password):

    correct_answer = password
    # user prompt for correct password
    submittion_Test = input("Enter the Correct Password to Proceed\n")

    # password submitted check
    if submittion_Test == correct_answer:
        print("\nWelcome User \nAccess Granted")
        result = "true"
    else:
        print("\nWrong Password \nAccess Denied")
        result = "true"

# correct password required to get access
passwordChecker("Let Me In Now")