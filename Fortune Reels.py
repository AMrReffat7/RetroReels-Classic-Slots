import random

# Constants
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

# Symbol configurations
SYMBOL_COUNT = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

SYMBOL_VALUE = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnings(columns, lines, bet, symbol_values):
    """
    Check for winnings in the slot machine.
    """
    total_winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            total_winnings += symbol_values[symbol] * bet
            winning_lines.append(line + 1)

    return total_winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    """
    Generate a random spin for the slot machine.
    """
    all_symbols = []
    for symbol, count in symbols.items():
        all_symbols.extend([symbol] * count)

    columns = []
    for _ in range(cols):
        column = random.sample(all_symbols, rows)
        columns.append(column)

    return columns


def print_slot_machine(columns):
    """
    Print the slot machine grid.
    """
    for row in zip(*columns):
        print(" | ".join(row))


def deposit():
    """
    Prompt the user to deposit money.
    """
    while True:
        amount = input("Please enter the amount you want to deposit: $")
        if amount.isdigit() and int(amount) > 0:
            return int(amount)
        print("Please enter a valid amount greater than 0.")


def get_number_of_lines():
    """
    Prompt the user to choose the number of lines to bet on.
    """
    while True:
        lines = input(f"How many lines do you want to bet on? (1-{MAX_LINES}): ")
        if lines.isdigit() and 1 <= int(lines) <= MAX_LINES:
            return int(lines)
        print("Please enter a valid number of lines.")


def get_bet():
    """
    Prompt the user to enter the bet amount.
    """
    while True:
        amount = input(f"How much do you want to bet on each line? (${MIN_BET}-{MAX_BET}): $")
        if amount.isdigit() and MIN_BET <= int(amount) <= MAX_BET:
            return int(amount)
        print(f"Please enter a valid bet amount between ${MIN_BET} and ${MAX_BET}.")


def spin(balance):
    """
    Perform a spin on the slot machine.
    """
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You don't have enough balance to bet that amount. Your current balance is: ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, SYMBOL_COUNT)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, SYMBOL_VALUE)
    print(f"You won ${winnings}.")
    if winning_lines:
        print("You won on lines:", ", ".join(map(str, winning_lines)))
    return winnings - total_bet


def main():
    """
    Main function to run the slot machine game.
    """
    balance = deposit()
    while True:
        print(f"Current balance: ${balance}")
        answer = input("Press Enter to play or 'Q' to quit: ").strip().lower()
        if answer == "q":
            break
        balance += spin(balance)

    print(f"Your remaining balance is: ${balance}")


main()
