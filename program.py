import bank_utils

def main():
    bank_utils.welcome()
    id = bank_utils.account_verification()
    functions = [bank_utils.details, bank_utils.deposit, bank_utils.withdraw]
    while True:
        looper = True
        while looper:
            user_input = input("What would you like to do?\n1. View account details.\n2. Deposit money into account.\n3. Withdraw money from account.\n> ")
            if user_input.lower() not in ["1", "2", "3"]:
                print("Please make a valid choice. (1, 2, 3)")
            else:
                looper = False
        functions[int(user_input)-1](id)
        print("Would you like to do anything else?")
        looper2 = True
        while looper2:
            user_input2 = input("Yes/No: ").lower()
            if user_input2 not in ['yes', 'no']:
                print("Please make a valid answer.")
            elif user_input2 == 'yes':
                looper2 = False
            elif user_input2 == 'no':
                exit()

main()