import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

# Dictionary
symbol_count = {
    "$": 3,
    "&": 4,
    "@": 6,
    "#": 8
}

symbol_value = {
    "$": 6,
    "&": 4,
    "@": 3,
    "#": 2
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(lines + 1)

    return winnings, winning_lines


def spin_slot_machine(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end="|")
            else:
                print(column[row], end="")

        print()


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
            "Enter the number of lines you would like to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Please enter a valid number.")
        else:
            print("Please enter a number.")

    return lines


def get_bet():
    while True:
        amount = input(
            "How much would you like to bet on each line: R$")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(
                    f"Amount must be between R${MIN_BET} - R${MAX_BET}.")
        else:
            print("Please enter a number.")

    return amount


def game(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(
                f"You do not have enough to bet that amount, your current balance is: R${balance}")
        else:
            break

    print(
        f"you are betting R${bet} on {lines} line(s). Total bet is: R${total_bet}")

    slots = spin_slot_machine(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won a total of R${winnings} on lines:", *winning_lines)

    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is R${balance}")
        play = input("Press ENTER to play or (Q) to cash out.")
        if play == "q":
            break
        balance += game(balance)

    print(f"You left with R${balance}. Thank you for playing!")


main()
