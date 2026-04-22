import typer
from typing import Optional
from pydantic import ValidationError
from bot.client import get_client
from bot.orders import place_order
from bot.validators import OrderRequest
from bot.logging_config import setup_logger

log = setup_logger()

app = typer.Typer()

@app.command()
def trade(
    symbol:str = typer.Option(..., help="Trading pair, e.g. BTCUSDT"),
    side:str = typer.Option(...,help="BUY or SELL"),
    order_type: str = typer.Option(..., "--order-type", help="MARKET or LIMIT"),
    quantity:float = typer.Option(..., help="How much to buy or sell"),
    price:Optional[float]= typer.Option(None, help="Price for LIMIT orders only")
):
    log.info(f"New order request - {side} {quantity} {symbol} at {order_type} price")

    try:
        order = OrderRequest(
            symbol=symbol.upper(),
            side=side.upper(),
            order_type=order_type.upper(),
            quantity=quantity,
            price=price
        )
    except ValidationError as e: 
        log.error(f"Invalid input: {e}")
        raise typer.Exit(code=1)
    
    try:
        client = get_client()
        log.info("Connected to Binance Testnet successfully")
    except ValueError as e:
        log.error(f"Connection failed: {e}")
        raise typer.Exit(code=1)
    
    try:
        result = place_order(client, order)
        order_id = result.get("orderId","N/A")
        status = result.get("status", "N/A")
        fills = result.get("fills",[])
         
        avg_price = "N/A"
        if fills:
            total_cost = sum(float(f["price"]) * float(f["qty"]) for f in fills)
            total_qty = sum(float(f["qty"]) for f in fills)
            avg_price = round(total_cost/total_qty, 4)

        log.success(f"Order placed! ID={order_id} | Status={status} | Avg Price={avg_price}")
        typer.echo(f"\nOrder Successful!")
        typer.echo(f"   Order ID  : {order_id}")
        typer.echo(f"   Status    : {status}")
        typer.echo(f"   Avg Price : {avg_price}\n")
    
    except ValueError as e:
        log.error(f"Order setup error: {e}")
        raise typer.Exit(code=1)
 
    except Exception as e:
        log.error(f"Order failed: {e}")
        raise typer.Exit(code=1)
    
if __name__ == "__main__":
    app()


        


