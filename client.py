from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceOrderException
from dotenv import load_dotenv
import os
import logging

logger = logging.getLogger(__name__)

class BinanceFuturesClient:
    def __init__(self):
        load_dotenv()

        self.api_key = os.getenv("BINANCE_API_KEY")
        self.secret_key = os.getenv("BINANCE_SECRET_KEY")
        

        if not self.api_key or not self.secret_key:
            raise ValueError("API key or Secret key not found in environment variables")

        try:
            self.client = Client(self.api_key, self.secret_key, testnet=True)
            self.client.FUTURES_URL = "https://testnet.binancefuture.com"

            logger.info("Binance Futures Testnet client initialized successfully")

        except Exception as e:
            logger.error(f"Failed to initialize Binance client: {e}")
            raise

    def create_order(self, symbol, side, order_type, quantity, price=None):
        try:
            logger.info(
                f"Placing order | Symbol: {symbol} | Side: {side} | "
                f"Type: {order_type} | Quantity: {quantity} | Price: {price}"
            )

            if order_type == "MARKET":
                response = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type=order_type,
                    quantity=quantity
                )

            elif order_type == "LIMIT":
                response = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type=order_type,
                    quantity=quantity,
                    price=price,
                    timeInForce="GTC"
                )

            else:
                raise ValueError("Unsupported order type")

            logger.info(f"Order response received: {response}")
            return response

        except BinanceAPIException as e:
            logger.error(f"Binance API error: {e.message}")
            raise

        except BinanceOrderException as e:
            logger.error(f"Binance order error: {e.message}")
            raise

        except Exception as e:
            logger.error(f"Unexpected error while placing order: {e}")
            raise