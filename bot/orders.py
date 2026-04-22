from binance.client import Client
from bot.validators import OrderRequest

def place_order(client: Client, order: OrderRequest):
    if order.order_type=="MARKET":
        response = client.create_order(
            symbol = order.symbol,
            side = order.side,
            type = "MARKET",
            quantity = order.quantity
        )

    elif order.order_type == "LIMIT":
        if order.price is None:
            raise ValueError("A price is required for LIMIT orders")\

        response = client.create_order(
            symbol = order.symbol,
            side= order.side,
            type = "LIMIT",
            timeInForce="GTC",
            quantity = order.quantity,
            price = str(order.price)
        )
        
    return response
