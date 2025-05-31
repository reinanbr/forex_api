from forex_python.converter import CurrencyRates
from datetime import datetime,timedelta
from kitano import puts

cr = CurrencyRates()
def convert_currency(amount, from_currency, to_currency,timepast:int=None):
    """
    Convert an amount from one currency to another.
    
    :param amount: The amount of money to convert.
    :param from_currency: The currency code to convert from (e.g., 'USD').
    :param to_currency: The currency code to convert to (e.g., 'EUR').
    :param timepast: Optional; if provided, the number of seconds in the past to use for conversion rate.
    :return: The converted amount in the target currency.
    """
    try:
        past_time = datetime.now()  # Ensure datetime is imported and used
        if timepast is not None:
            puts("timepast is",timepast)
            # Convert timepast from seconds to datetime
            past_time = datetime.now() - timedelta(seconds=timepast)
        converted_amount = cr.convert(from_currency, to_currency, amount,past_time)
        return converted_amount
    except Exception as e:
        print(f"Error converting currency: {e}")
        return None

print(convert_currency(100, 'USD', 'EUR', timepast=(3*3600)))  # Example usage with 1 hour in the past