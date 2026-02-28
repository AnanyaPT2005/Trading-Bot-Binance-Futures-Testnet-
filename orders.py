import logging
from client import BinanceFuturesClient

logger = logging.getLogger(__name__)


class OrderService:
    def __init__(self):
        self.client = BinanceFuturesClient()

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            # Business rule validation
            if order_type == "LIMIT" and price is None:
                raise ValueError("Price is required for LIMIT orders")

            if order_type == "MARKET" and price is not None:
                logger.warning("Price provided for MARKET order. It will be ignored.")

            logger.info("Processing order in OrderService")

            response = self.client.create_order(
                symbol=symbol,
                side=side,
                order_type=order_type,
                quantity=quantity,
                price=price
            )

            # Extract useful response details
            order_summary = {
                "orderId": response.get("orderId"),
                "status": response.get("status"),
                "executedQty": response.get("executedQty"),
                "avgPrice": response.get("avgPrice", "N/A")
            }

            logger.info(f"Order placed successfully: {order_summary}")

            return {
                "success": True,
                "data": order_summary
            }

        except Exception as e:
            logger.error(f"Order placement failed: {e}")
            return {
                "success": False,
                "error": str(e)
            }