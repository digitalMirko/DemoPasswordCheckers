# this is a password checker demo

def passwordChecker(password):

    correct_answer = password

    while True:
        # user prompt for correct password
        submittion_Test = input("Enter the Correct Password to Proceed\n")

        # password submitted check
        if submittion_Test == correct_answer:
            print("\nWelcome User \nAccess Granted")
            result = "true"
            return
        else:
            print("\nWrong Password \nAccess Denied")
            result = "true"

# correct password required to get access
passwordChecker("Open Sesame")

input("\nPress enter")