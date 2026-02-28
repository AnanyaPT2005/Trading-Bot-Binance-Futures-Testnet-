import logging

logger = logging.getLogger(__name__)

VALID_SIDES = ["BUY", "SELL"]
VALID_ORDER_TYPES = ["MARKET", "LIMIT"]


def validate_symbol(symbol: str):
    if not symbol or not isinstance(symbol, str):
        raise ValueError("Symbol must be a non-empty string")

    return symbol.upper()


def validate_side(side: str):
    side = side.upper()
    if side not in VALID_SIDES:
        raise ValueError("Side must be BUY or SELL")

    return side


def validate_order_type(order_type: str):
    order_type = order_type.upper()
    if order_type not in VALID_ORDER_TYPES:
        raise ValueError("Order type must be MARKET or LIMIT")

    return order_type


def validate_quantity(quantity):
    try:
        quantity = float(quantity)
        if quantity <= 0:
            raise ValueError
        return quantity
    except:
        raise ValueError("Quantity must be a positive number")


def validate_price(price):
    if price is None:
        return None

    try:
        price = float(price)
        if price <= 0:
            raise ValueError
        return price
    except:
        raise ValueError("Price must be a positive number")