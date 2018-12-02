# this is a password checker demo
# In this demo the user is prompted for the password and it will continue
# to prompt them until the correct answer is given. Then they click the 'Enter' key
# and the program stops

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