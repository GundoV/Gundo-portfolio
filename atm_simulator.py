# atm_simulator.py

def main():
    print("=" * 40)
    print("      SMART ATM WITHDRAWAL SIMULATOR     ")
    print("=" * 40)

    # 1. Fixed bank balance
    balance = 500.00
    print(f"Current Balance: R{balance:.2f}\n")

    # 2. Ask user for withdrawal amount and convert to float
    withdrawal_input = input("Enter amount to withdraw (R): ").strip()
    withdrawal_amount = float(withdrawal_input)

    # 3-5. Conditionals for withdrawal logic
    if withdrawal_amount <= 0:
        # Step 4: Check for zero or negative amount
        print("Invalid amount. You must withdraw more than R0.")
    elif withdrawal_amount <= balance:
        # Step 3: Check for sufficient funds
        balance -= withdrawal_amount
        print(f"Withdrawal successful! Remaining balance: R{balance:.2f}")
    else:
        # Step 5: Insufficient funds
        print("Declined. Insufficient funds.")

    print("=" * 40)


if __name__ == "__main__":
    main()