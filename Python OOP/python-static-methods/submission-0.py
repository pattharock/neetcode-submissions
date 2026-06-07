class CurrencyConverter:
    rates = {  
        'EUR': 1.20,
        'JPY': 0.01 
    }

    @staticmethod
    def to_usd(foreign_amount: float, foreign_currency: str) -> float:
        for currency, factor in CurrencyConverter.rates.items():
            if currency == foreign_currency:
                return foreign_amount * factor
        raise ValueError("Unsupported currency")
    

print(f"100 EUR = {CurrencyConverter.to_usd(100, 'EUR')} USD")     # 120 USD
print(f"100 JPY = {CurrencyConverter.to_usd(100, 'JPY')} USD")     # 1 USD
