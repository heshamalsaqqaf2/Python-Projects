# Dictionary containing exchange rates relative to USD
exchange_rates = {
    "USD": 1.0,
    "EUR": 0.85,
    "GBP": 0.75,
    "JPY": 110.0,
    "CAD": 1.25,
    "AUD": 1.3,
    "CHF": 0.92,
    "CNY": 6.47,
    "INR": 74.15,
    "SAR": 3.75,
}


# Function to display supported currencies
def display_supported_currencies():
    print("Supported currencies:")
    for currency in exchange_rates:
        print(currency)


# Function to validate the entered currency
def validate_currency(currency):
    return currency in exchange_rates


# Function to validate the entered amount
def validate_amount(amount):
    try:
        float(amount)
        return True
    except ValueError:
        return False


# Function to convert currencies
def convert_currency(amount, from_currency, to_currency):
    amount_in_usd = amount / exchange_rates[from_currency]
    converted_amount = amount_in_usd * exchange_rates[to_currency]
    return converted_amount


# Function to get user input
def get_user_input():
    while True:
        amount = input("Enter the amount you want to convert: ")
        if validate_amount(amount):
            amount = float(amount)
            break
        else:
            print("Invalid amount. Please enter a valid number.")

    while True:
        from_currency = input(
            "Enter the currency you want to convert from (e.g., USD, EUR): "
        ).upper()
        if validate_currency(from_currency):
            break
        else:
            print("Invalid currency. Please enter a supported currency.")

    while True:
        to_currency = input(
            "Enter the currency you want to convert to (e.g., USD, EUR): "
        ).upper()
        if validate_currency(to_currency):
            break
        else:
            print("Invalid currency. Please enter a supported currency.")

    return amount, from_currency, to_currency


# Main function
def main():
    display_supported_currencies()
    amount, from_currency, to_currency = get_user_input()
    result = convert_currency(amount, from_currency, to_currency)
    print(f"{amount} {from_currency} equals {result:.2f} {to_currency}")


# Call the main function
if __name__ == "__main__":
    main()
