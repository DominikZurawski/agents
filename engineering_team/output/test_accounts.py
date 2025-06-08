import unittest
from accounts import Account, get_share_price

class TestAccount(unittest.TestCase):

    def setUp(self):
        self.account = Account("testuser", 1000.0)

    def test_initialization(self):
        self.assertEqual(self.account.username, "testuser")
        self.assertEqual(self.account.balance, 1000.0)
        self.assertEqual(self.account.holdings, {})
        self.assertEqual(self.account.transactions, [])

    def test_deposit(self):
        self.account.deposit(500.0)
        self.assertEqual(self.account.balance, 1500.0)
        self.assertIn("Deposited: $500.00", self.account.transactions)

        with self.assertRaises(ValueError):
            self.account.deposit(-100)

    def test_withdraw(self):
        self.account.withdraw(200.0)
        self.assertEqual(self.account.balance, 800.0)
        self.assertIn("Withdrew: $200.00", self.account.transactions)

        with self.assertRaises(ValueError):
            self.account.withdraw(1200.0)  # Insufficient funds
        with self.assertRaises(ValueError):
            self.account.withdraw(-100)

    def test_buy_shares(self):
        self.account.buy_shares("AAPL", 2)
        self.assertEqual(self.account.balance, 1000.0 - (150.0 * 2))
        self.assertEqual(self.account.holdings, {"AAPL": 2})
        self.assertIn("Bought 2 shares of AAPL at $150.00 each.", self.account.transactions)

        with self.assertRaises(ValueError):
            self.account.buy_shares("TSLA", 5)  # Insufficient funds
        with self.assertRaises(ValueError):
            self.account.buy_shares("AAPL", -1)

    def test_sell_shares(self):
        self.account.buy_shares("AAPL", 2)
        self.account.sell_shares("AAPL", 1)
        self.assertEqual(self.account.balance, 1000.0 - (150.0 * 2) + (150.0 * 1))
        self.assertEqual(self.account.holdings, {"AAPL": 1})
        self.assertIn("Sold 1 shares of AAPL at $150.00 each.", self.account.transactions)

        self.account.sell_shares("AAPL", 1)
        self.assertNotIn("AAPL", self.account.holdings)

        with self.assertRaises(ValueError):
            self.account.sell_shares("TSLA", 1)  # Not enough shares
        with self.assertRaises(ValueError):
            self.account.sell_shares("AAPL", -1)

    def test_get_portfolio_value(self):
        self.account.buy_shares("AAPL", 2)
        portfolio_value = self.account.get_portfolio_value()
        self.assertAlmostEqual(portfolio_value, self.account.balance + (2 * 150.0))

    def test_get_profit_loss(self):
        self.account.buy_shares("AAPL", 2)
        profit_loss = self.account.get_profit_loss(1000.0)
        self.assertAlmostEqual(profit_loss, self.account.get_portfolio_value() - 1000.0)

    def test_get_holdings(self):
        self.account.buy_shares("AAPL", 2)
        holdings = self.account.get_holdings()
        self.assertEqual(holdings, {"AAPL": 2})

    def test_get_transaction_history(self):
        self.account.deposit(100.0)
        self.account.buy_shares("AAPL", 1)
        transactions = self.account.get_transaction_history()
        self.assertIn("Deposited: $100.00", transactions)
        self.assertIn("Bought 1 shares of AAPL at $150.00 each.", transactions)

    def test_get_profit_loss_report(self):
        self.account.buy_shares("AAPL", 2)
        report = self.account.get_profit_loss_report(1000.0)
        self.assertIn("Profit/Loss: $\", report)

if __name__ == '__main__':
    unittest.main()