"""
Module for a simple account management system for a trading simulation platform.
"""

class Account:
    def __init__(self, username: str, initial_deposit: float):
        """
        Initializes a new account with a username and an initial deposit.

        :param username: The name of the user.
        :param initial_deposit: Initial funding amount for the account.
        """
        self.username = username
        self.balance = initial_deposit
        self.holdings = {}  # Dictionary to hold the stock quantities
        self.transactions = []  # List to hold transaction history

    def deposit(self, amount: float) -> None:
        """
        Deposits a specified amount to the account.

        :param amount: The amount to deposit.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        self.transactions.append(f"Deposited: ${amount:.2f}")

    def withdraw(self, amount: float) -> None:
        """
        Withdraws a specified amount from the account.

        :param amount: The amount to withdraw.
        :raises ValueError: If withdrawal exceeds balance.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds for withdrawal.")
        self.balance -= amount
        self.transactions.append(f"Withdrew: ${amount:.2f}")

    def buy_shares(self, symbol: str, quantity: int) -> None:
        """
        Records the purchase of shares for a specific symbol and quantity.

        :param symbol: The stock symbol to buy.
        :param quantity: The quantity of shares to buy.
        :raises ValueError: If insufficient funds or invalid quantity.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        share_price = get_share_price(symbol)
        total_cost = share_price * quantity
        if total_cost > self.balance:
            raise ValueError("Insufficient funds to buy shares.")
        self.balance -= total_cost
        if symbol in self.holdings:
            self.holdings[symbol] += quantity
        else:
            self.holdings[symbol] = quantity
        self.transactions.append(f"Bought {quantity} shares of {symbol} at ${share_price:.2f} each.")

    def sell_shares(self, symbol: str, quantity: int) -> None:
        """
        Records the sale of shares for a specific symbol and quantity.

        :param symbol: The stock symbol to sell.
        :param quantity: The quantity of shares to sell.
        :raises ValueError: If quantity exceeds holdings or invalid quantity.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        if symbol not in self.holdings or self.holdings[symbol] < quantity:
            raise ValueError("Not enough shares to sell.")
        share_price = get_share_price(symbol)
        total_income = share_price * quantity
        self.balance += total_income
        self.holdings[symbol] -= quantity
        if self.holdings[symbol] == 0:
            del self.holdings[symbol]
        self.transactions.append(f"Sold {quantity} shares of {symbol} at ${share_price:.2f} each.")

    def get_portfolio_value(self) -> float:
        """
        Calculates the total value of the user's portfolio.

        :return: Total portfolio value.
        """
        total_value = self.balance
        for symbol, quantity in self.holdings.items():
            total_value += get_share_price(symbol) * quantity
        return total_value

    def get_profit_loss(self, initial_deposit: float) -> float:
        """
        Calculates the total profit or loss from the initial deposit.

        :param initial_deposit: The initial deposit amount.
        :return: Profit or loss amount.
        """
        return self.get_portfolio_value() - initial_deposit

    def get_holdings(self) -> dict:
        """
        Reports the current holdings of the user.

        :return: Dictionary of stock holdings with quantities.
        """
        return self.holdings

    def get_profit_loss_report(self, initial_deposit: float) -> str:
        """
        Reports the current profit or loss of the user.

        :param initial_deposit: The initial deposit amount.
        :return: A string reporting profit or loss.
        """
        profit_loss = self.get_profit_loss(initial_deposit)
        return f"Profit/Loss: ${profit_loss:.2f}"

    def get_transaction_history(self) -> list:
        """
        Lists the transactions that the user has made over time.

        :return: List of transaction strings.
        """
        return self.transactions

def get_share_price(symbol: str) -> float:
    """
    Mock function to return share prices for fixed symbols.

    :param symbol: The stock symbol to get the price for.
    :return: The price of the stock.
    """
    prices = {
        "AAPL": 150.00,
        "TSLA": 700.00,
        "GOOGL": 2800.00
    }
    return prices.get(symbol, 0.0)