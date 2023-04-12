##slotmachine game goes here
## Text based slot machine

def slots():
        
    import random

    MAX_LINES = 3
    MAX_BET = 100
    MIN_BET = 1

    #size of slot machine
    MACHINE_ROWS = 3
    MACHINE_COLS = 3

    #how many symbols per column/slot reel
    symbol_count = {
        "A": 2,
        "B": 4,
        "C": 6,
        "D": 8
    }


    symbol_value = {
        "A": 5,
        "B": 3,
        "C": 2,
        "D": 1
    }

    #win status
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
                winning_lines.append(line + 1)
            
        return winnings, winning_lines




    def get_slot_machine_spin(rows, cols, symbols):
        all_symbols = []
        for symbol, symbol_count in symbols.items():
            for _ in range(symbol_count):
                all_symbols.append(symbol)

        columns = []
        for _ in range(cols):
            column = []
            current_symbols = all_symbols[::]
            for _ in range(rows):
                value = random.choice(current_symbols)
                current_symbols.remove(value)
                column.append(value)

            columns.append(column)

        return columns

    def print_slot_machine(columns):
        #transpose columns and print the spin
        for row in range(len(columns[0])):
            for i, column in enumerate(columns):
                if i != len(columns) - 1:
                    print(column[row], end=' | ')
                else:
                    print(column[row])


    def deposit():
        while True:
            amount = input('How much would you like to deposit? $')
            if amount.isdigit():
                amount = int(amount)
                if amount > 0:
                    break
                else:
                    print('Amount must be positive.')
            else:
                print("Please enter a number.")

        return amount

    def get_number_of_lines():
        while True:
            lines = input('How many lines would you like to bet on (1-' + str(MAX_LINES) + ')? ')
            if lines.isdigit():
                lines = int(lines)
                if 1 <= lines <= MAX_LINES:
                    break
                else:
                    print('Enter a valid number of lines.')
            else:
                print("Please enter a number.")

        return lines

    def get_bet():
        while True:
            amount = input('How much would you bet per line? $')
            if amount.isdigit():
                amount = int(amount)
                if MIN_BET <= amount <= MAX_BET:
                    break
                else:
                    print(f'Amount must be between {MIN_BET} - {MAX_BET}.')
            else:
                print("Please enter a number.")

        return amount

    def spin(balance):
        lines = get_number_of_lines()
        while True:
            bet = get_bet()
            total_bet = bet * lines

            if total_bet > balance:
                print(f'You do not have enough balance to make this bet.\nYou have {balance} left to bet.')
            else:
                break
        print(f'You are betting ${bet} on {lines} lines.\nTotal bet amount is ${total_bet}.')

        slots = get_slot_machine_spin(MACHINE_ROWS, MACHINE_COLS, symbol_count)
        print_slot_machine(slots)
        winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
        if winnings == 0:
            print('You didn\'t win this time.. Try again!')
        if winnings > 0:
            if len(winning_lines) == 1:
                print(f'You won ${winnings}.\nYou won on line number: ', *winning_lines)
            if len(winning_lines) > 1:
                print(f'You won ${winnings}.\nYou won on lines: ', *winning_lines)

        return winnings - total_bet


    def main():
        balance = deposit()
        initial_deposit = balance
        while True:
            print(f'Current balance is: ${balance}')
            answer = input('Press enter to play. (q to quit)')
            if answer.lower() == 'q':
                break
            balance += spin(balance)

        profit = balance - initial_deposit
        print(f'You left with ${balance}.')
        if profit <= 0:
            print(f'You lost ${abs(profit)} during this session.')
            print('Come back next time for better luck!')
        if profit > 0:
            print(f'This sessions earnings were: ${profit}')
            print('Are you Irish? Seems like luck is on your side!')


## not sure if this is correct.
## I wrapped this whole thing around slots() 
## so hopefully we can import it that way
## but I used to call this function with main()
## wont it auto run if I don't have this?
## How can I import this into another file like:
## from slots import slots
## and then play the game by calling slots()

    main()


if __name__ == '__main__':
    slots()
