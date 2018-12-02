# this is a password checker demo

def passwordChecker(password):

    correct_answer = password
    # user prompt for correct password
    submittion_Test = input("Enter the Correct Password to Proceed\n")

    # password submitted check
    if submittion_Test == correct_answer:
        print("\nWelcome User \nAccess Granted")
        result = "true"
    else:
        print("\nWrong Password User \nAccess Denied")
        result = "true"

# correct password required to get access
passwordChecker("Let Me In Now")