import gradio as gr
from accounts import Account, get_share_price

# Initialize account
account = Account("DemoUser", 10000.0)
initial_deposit = account.balance  # Store initial deposit for profit/loss calculation

def deposit(amount):
    try:
        amount = float(amount)
        account.deposit(amount)
        return account.balance, account.get_portfolio_value(), account.get_profit_loss(initial_deposit), account.get_holdings(), account.get_transaction_history()
    except ValueError as e:
        return account.balance, account.get_portfolio_value(), account.get_profit_loss(initial_deposit), account.get_holdings(), str(e)

def withdraw(amount):
    try:
        amount = float(amount)
        account.withdraw(amount)
        return account.balance, account.get_portfolio_value(), account.get_profit_loss(initial_deposit), account.get_holdings(), account.get_transaction_history()
    except ValueError as e:
        return account.balance, account.get_portfolio_value(), account.get_profit_loss(initial_deposit), account.get_holdings(), str(e)

def buy_shares(symbol, quantity):
    try:
        quantity = int(quantity)
        account.buy_shares(symbol, quantity)
        return account.balance, account.get_portfolio_value(), account.get_profit_loss(initial_deposit), account.get_holdings(), account.get_transaction_history()
    except ValueError as e:
        return account.balance, account.get_portfolio_value(), account.get_profit_loss(initial_deposit), account.get_holdings(), str(e)

def sell_shares(symbol, quantity):
    try:
        quantity = int(quantity)
        account.sell_shares(symbol, quantity)
        return account.balance, account.get_portfolio_value(), account.get_profit_loss(initial_deposit), account.get_holdings(), account.get_transaction_history()
    except ValueError as e:
        return account.balance, account.get_portfolio_value(), account.get_profit_loss(initial_deposit), account.get_holdings(), str(e)

with gr.Blocks() as demo:
    gr.Markdown("# Simple Trading Account")

    with gr.Row():
        with gr.Column():
            deposit_amount = gr.Number(label="Deposit Amount")
            deposit_button = gr.Button("Deposit")

            withdraw_amount = gr.Number(label="Withdraw Amount")
            withdraw_button = gr.Button("Withdraw")

            buy_symbol = gr.Textbox(label="Buy Symbol")
            buy_quantity = gr.Number(label="Buy Quantity")
            buy_button = gr.Button("Buy Shares")

            sell_symbol = gr.Textbox(label="Sell Symbol")
            sell_quantity = gr.Number(label="Sell Quantity")
            sell_button = gr.Button("Sell Shares")

        with gr.Column():
            balance_output = gr.Number(label="Account Balance")
            portfolio_value_output = gr.Number(label="Portfolio Value")
            profit_loss_output = gr.Number(label="Profit / Loss")
            holdings_output = gr.JSON(label="Holdings")
            transaction_history_output = gr.Textbox(label="Transaction History", lines=5)

    deposit_button.click(
        deposit,
        inputs=[deposit_amount],
        outputs=[balance_output, portfolio_value_output, profit_loss_output, holdings_output, transaction_history_output],
    )

    withdraw_button.click(
        withdraw,
        inputs=[withdraw_amount],
        outputs=[balance_output, portfolio_value_output, profit_loss_output, holdings_output, transaction_history_output],
    )

    buy_button.click(
        buy_shares,
        inputs=[buy_symbol, buy_quantity],
        outputs=[balance_output, portfolio_value_output, profit_loss_output, holdings_output, transaction_history_output],
    )

    sell_button.click(
        sell_shares,
        inputs=[sell_symbol, sell_quantity],
        outputs=[balance_output, portfolio_value_output, profit_loss_output, holdings_output, transaction_history_output],
    )

    # Initialize the display with starting values
    balance_output.value = account.balance
    portfolio_value_output.value = account.get_portfolio_value()
    profit_loss_output.value = account.get_profit_loss(initial_deposit)
    holdings_output.value = account.get_holdings()
    transaction_history_output.value = "\n".join(account.get_transaction_history())

demo.launch()