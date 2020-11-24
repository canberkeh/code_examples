'''
Exchange office. You can convert currencies or check prices.
Check BTC price and convert to currencies.
'''
from forex_python.converter import CurrencyRates
from forex_python.bitcoin import BtcConverter
from forex_python.converter import CurrencyCodes
currency = CurrencyRates()
bitcoin = BtcConverter()
currency_codes = CurrencyCodes()
class ExchangeRates():
    """I used currency/btc name,prices,symbols and full names with forex lib"""
    currency_name_list = ["TRY", "USD", "EUR", "GBP", "THB", "JPY", "RUB", "HKD", "IDR", "ILS", "DKK", "INR", "CHF", "MXN", "CZK", "SGD", "HRK", "MYR", "NOK", "CNY", "BGN", "PHP", "PLN", "ZAR", "CAD", "ISK", "BRL", "RON", "NZD", "KRW", "AUD", "HUF", "SEK"]
    def continue_ask(self):
        """Ask if you want to continue"""
        continue_on = True
        while continue_on:
            print("Do you want to continue menu (Y/N) ? :")
            selection = str(input().upper())
            if selection == "Y":
                self.exchange_main()
            elif selection == "N":
                self.quit()
            else:
                print("INVALID INPUT. PLEASE CHOOSE Y OR N ")
                continue

    def exchange_list(self, currency_name):
        """Exchange list by number,name,price"""
        j = 1
        for key, value in currency.get_rates(currency_name).items():
            if currency_name != key:
                print(j, "->", key, "-> ", round(value, 2))
                j = j + 1
        self.continue_ask()

    def exchange_rate(self, currency_name, currency_name_2):
        """Take a look at rates"""
        print("1", currency_codes.get_currency_name(currency_name), " = ", round(currency.get_rate(currency_name, currency_name_2), 2), currency_codes.get_currency_name(currency_name_2), "\n")
        self.continue_ask()

    def currency_converter(self, currency_name, currency_name_2, amount):
        """Change office ! """
        print(currency_codes.get_currency_name(currency_name), " / ", currency_codes.get_currency_name(currency_name_2))
        print(amount, currency_name, currency_codes.get_symbol(currency_name), " = ", round(currency.convert(currency_name, currency_name_2, amount), 2), currency_name_2, currency_codes.get_symbol(currency_name_2), "\n")
        self.continue_ask()

    def bitcoin(self, currency_name):
        """BTC Price"""
        print("BITCOIN", bitcoin.get_symbol(), " / ", currency_codes.get_currency_name(currency_name))
        print("BTC", bitcoin.get_symbol(), "/", currency_name, currency_codes.get_symbol(currency_name), round(bitcoin.get_latest_price(currency_name), 2), "\n")
        self.continue_ask()

    def to_bitcoin(self, currency_name, amount):
        """Changes currencies to BTC"""
        print(amount, currency_name, " = ", round(bitcoin.convert_to_btc(amount, currency_name), 2), "BITCOIN", bitcoin.get_symbol(), "\n")
        self.continue_ask()

    def from_bitcoin_to(self, currency_name, amount):
        """Changes BTC to wanted currency"""
        print(amount, "BITCOIN", bitcoin.get_symbol(), " = ", round(bitcoin.convert_btc_to_cur(amount, currency_name), 2), currency_name, "\n")
        self.continue_ask()

    @classmethod
    def quit(cls):
        """My standart quit func"""
        raise SystemExit

    def exchange_main(self):
        """Main def for making selections"""
        work_on = True
        while work_on:
            print("***** Exchanges *****")
            print("1- Exchange List\n2- Check Selected Exchange Rate")
            print("3- Currency Converter\n4- Bitcoin Price <3")
            print("5- Convert to Bitcoin", bitcoin.get_symbol())
            print("6- Convert Bitcoin to Currencies")
            print("00- EXIT to Main Menu\n99- EXIT")
            select = input("Make selection: ")
            if select == "1":
                print("Currency List : ", self.currency_name_list)
                currency_name = input("Select currency base : ").upper()
                self.exchange_list(currency_name)

            elif select == "2":
                print("Select currencies")
                print(self.currency_name_list)
                currency_name = input("From : ").upper()
                currency_name_2 = input("To : ").upper()
                self.exchange_rate(currency_name, currency_name_2)

            elif select == "3":
                print("Select currencies and amount")
                print(self.currency_name_list)
                currency_name = input("From : ").upper()
                currency_name_2 = input("To : ").upper()
                amount = float(input("Enter amount : "))
                self.currency_converter(currency_name, currency_name_2, amount)

            elif select == "4":
                print("***** Currency List ******")
                print(self.currency_name_list)
                print("Select currency to see BTC price", bitcoin.get_symbol())
                currency_name = input("To : ").upper()
                self.bitcoin(currency_name)

            elif select == "5":
                print("***** Currency List ******")
                print(self.currency_name_list)
                print("Select currency to convert Bitcoin : ", bitcoin.get_symbol())
                currency_name = input("From : ").upper()
                amount = float(input("Enter amount : "))
                self.to_bitcoin(currency_name, amount)

            elif select == "6":
                print("***** Currency List *****")
                print(self.currency_name_list)
                print("Select currency to convert from Bitcoin", bitcoin.get_symbol(), ": ")
                currency_name = input("To : ").upper()
                amount = float(input("Enter BTC amount : "))
                self.from_bitcoin_to(currency_name, amount)

            elif select == "00":
                break

            elif select == "99":
                self.quit()
