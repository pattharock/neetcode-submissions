class BankAccount:
    total_accounts = 0
    total_balance = 0

    def __init__(self, name: str, balance: float) -> None:
        self.name = name
        self.balance = balance
        BankAccount.total_accounts += 1
        BankAccount.total_balance += balance
    
    def __str__(self) -> str:
        return f"{self.name}'s balance: ${self.balance}"

# TODO: Create two accounts
# TODO: Print the information using the mentioned format

alice_account = BankAccount("Alice", 1000)
bob_account = BankAccount("Bob", 2000)

print(alice_account)
print(bob_account)

print(f"Total Accounts: {BankAccount.total_accounts}")
print(f"Total Balance: ${BankAccount.total_balance}")