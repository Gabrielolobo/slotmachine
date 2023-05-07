
MAX_LINES = 3


def deposit():
    while True:
        amount = input("How much would you like to deposit: R$")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Please enter a positive value.")
        else:
            print("Please enter a number.")

    return amount


def get_number_of_lines():
    while True:
        lines = input(
            "Enter the number of line you would like to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Please enter a positive value.")
        else:
            print("Please enter a number.")

    return lines


def main():
    balance = deposit()


main()
