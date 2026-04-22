from pydantic import BaseModel, field_validator
from typing import Optional 

class OrderRequest(BaseModel):
    symbol: str
    side: str
    order_type: str
    quantity: float
    price: Optional[float] = None

    @field_validator("side")
    def side_valid(cls, value):
        value = value.upper()
        if value not in ('BUY','SELL'):
            raise ValueError("Side must be BUY or SELL")
        return value
    
    @field_validator("order_type")
    def order_type_valid(cls, value):
        value = value.upper()
        if value not in ("MARKET","LIMIT"):
            raise ValueError("Order Type must be MARKET or LIMIT")
        return value
    
    @field_validator("quantity")
    def quantity_valid(cls, value):
        if value<=0:
            raise ValueError("Quantity must be greater than zero")
        return value