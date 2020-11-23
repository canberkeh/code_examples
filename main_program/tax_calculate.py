'''
Tax calculate. You can choose tax rate.
'''
class TaxCalculate():
    """Class of taxes"""
    tax_rates = {
        "1":0.18,
        "2":0.08,
        "3":0.01
    }

    def tax_rate(self):
        """Asking tax rate"""
        print("***** Tax Calculator *****")
        work_on = True
        while work_on:
            print("Choose the tax rate\n1- %18\n2- %8\n3- %1")
            tax = input()
            if tax in self.tax_rates:
                self.tax_calc(self.tax_rates.get(tax))
                break
            elif tax == "00":
                break
            elif tax == "99":
                raise SystemExit
            else:
                continue

    def tax_calc(self, tax_price):
        """main"""
        price = float(input("Enter the price : "))
        tax_price_is = price * tax_price
        price_without_tax = price - (price * tax_price)
        print(f"Tax : {tax_price}")
        print(f"Tax price : {tax_price_is}")
        print(f"Price without tax : {price_without_tax}\n")
        self.ask_run()

    def ask_run(self):
        """ask for continue"""
        ask_on=True
        while ask_on:
            print("Do you want to continue (Y/N) ? :  ")
            continue_ask = str(input().upper())
            if continue_ask == "Y":
                self.tax_rate()
            elif continue_ask == "N":
                break
            else:
                continue
