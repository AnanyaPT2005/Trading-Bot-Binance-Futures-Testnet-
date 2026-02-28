# import argparse
# import logging

# from logging_config import setup_logging
# from validators import (
#     validate_symbol,
#     validate_side,
#     validate_order_type,
#     validate_quantity,
#     validate_price
# )
# from orders import OrderService


# def main():
#     setup_logging()
#     logger = logging.getLogger(__name__)
#     logger.info("Trading bot started")

#     parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

#     parser.add_argument("--symbol", required=True, help="Trading symbol (e.g., BTCUSDT)")
#     parser.add_argument("--side", required=True, help="BUY or SELL")
#     parser.add_argument("--type", required=True, help="MARKET or LIMIT")
#     parser.add_argument("--quantity", required=True, help="Order quantity")
#     parser.add_argument("--price", required=False, help="Price (required for LIMIT orders)")

#     args = parser.parse_args()

#     try:
#         symbol = validate_symbol(args.symbol)
#         side = validate_side(args.side)
#         order_type = validate_order_type(args.type)
#         quantity = validate_quantity(args.quantity)
#         price = validate_price(args.price)

#         service = OrderService()
#         result = service.place_order(symbol, side, order_type, quantity, price)

#         print("\n========= ORDER SUMMARY =========")
#         print(f"Symbol: {symbol}")
#         print(f"Side: {side}")
#         print(f"Type: {order_type}")
#         print(f"Quantity: {quantity}")
#         if order_type == "LIMIT":
#             print(f"Price: {price}")

#         print("\n========= RESPONSE =========")

#         if result["success"]:
#             data = result["data"]
#             print(f"Order ID: {data['orderId']}")
#             print(f"Status: {data['status']}")
#             print(f"Executed Qty: {data['executedQty']}")
#             print(f"Avg Price: {data['avgPrice']}")
#             print("\n✅ Order placed successfully!")
#         else:
#             print(f"\n❌ Order failed: {result['error']}")

#     except Exception as e:
#         logger.error(f"Validation or execution error: {e}")
#         print(f"\n❌ Error: {e}")


# if __name__ == "__main__":
#     main()

import logging

from logging_config import setup_logging
from validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)
from orders import OrderService


def get_user_input(order_type):
    symbol = input("Enter symbol (e.g., BTCUSDT): ")
    side = input("Enter side (BUY/SELL): ")
    quantity = input("Enter quantity: ")

    price = None
    if order_type == "LIMIT":
        price = input("Enter price: ")

    return symbol, side, quantity, price


def interactive_menu():
    service = OrderService()

    while True:
        print("\n===== Binance Futures Testnet Trading Bot =====")
        print("1. Place MARKET order")
        print("2. Place LIMIT order")
        print("3. Exit")

        choice = input("Select an option: ").strip()

        if choice == "3":
            print("Exiting...")
            break

        elif choice in ["1", "2"]:
            try:
                order_type = "MARKET" if choice == "1" else "LIMIT"

                symbol, side, quantity, price = get_user_input(order_type)

                # Validation
                symbol = validate_symbol(symbol)
                side = validate_side(side)
                order_type = validate_order_type(order_type)
                quantity = validate_quantity(quantity)
                price = validate_price(price)

                result = service.place_order(
                    symbol, side, order_type, quantity, price
                )

                print("\n========= ORDER SUMMARY =========")
                print(f"Symbol: {symbol}")
                print(f"Side: {side}")
                print(f"Type: {order_type}")
                print(f"Quantity: {quantity}")
                if order_type == "LIMIT":
                    print(f"Price: {price}")

                print("\n========= RESPONSE =========")

                if result["success"]:
                    data = result["data"]
                    print(f"Order ID: {data['orderId']}")
                    print(f"Status: {data['status']}")
                    print(f"Executed Qty: {data['executedQty']}")
                    print(f"Avg Price: {data['avgPrice']}")
                    print("\n✅ Order placed successfully!")
                else:
                    print(f"\n❌ Order failed: {result['error']}")

            except Exception as e:
                logging.getLogger(__name__).error(f"Error: {e}")
                print(f"\n❌ Error: {e}")

        else:
            print("Invalid option. Please select 1, 2, or 3.")


if __name__ == "__main__":
    setup_logging()
    interactive_menu()