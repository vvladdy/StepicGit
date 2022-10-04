class Product:

    def __init__(self, name, purchasing_price, amount=0):
        self.name = name
        self.purchasing_price = purchasing_price
        self.selling_price = round(purchasing_price * 1.2, 2)
        self.amount = amount

    def __str__(self):
        return f'{self.name} in stock {self.amount}, purchasing price:' \
               f' {self.purchasing_price}, ' \
               f'selling price: {self.selling_price}'

class ProductStore:
    # Склад товаров магазина

    def __init__(self):
        self.products = []
        self.income = 0
        self.profit = 0

    def add_product(self, product, amount):
        if product in self.products:
            product.amount += amount
        else:
            self.products.append(product)
            product.amount = amount
        print(f'{product.name} added to stock {amount} units')

    def _sell_product(self, product_name, amount):
        for product in self.products:
            if product.name == product_name and product.amount >= amount:
                product.amount -= amount
                self.income += product.selling_price * amount
                self.profit += ((product.selling_price -
                                 product.purchasing_price) * amount)
                print(f'{product.name} sell {amount} units')

    def _get_income(self):
        return f'Total income: {self.income}'

    def _get_profit(self):
        return f'Total profit: {self.profit}'

    def report(self):
        return self._get_income(), self._get_profit()

    def get_all_products(self):
        for product in self.products:
            print(f'{product.name}, price: {product.selling_price}, '
                  f'amount: {product.amount}')

class CartProducts:
    # Корзина

    def __init__(self):
        self.cart = []

    def add_to_cart(self, amount, *products):
        for product in products:
            if product.amount > amount:
                product_in_cart = {
                    'product name': product.name,
                    'amount': amount,
                    'price': product.selling_price,
                    'sum': product.selling_price * amount
                }
                self.cart.append(product_in_cart)
                print(
                    f'{product.name},{product_in_cart["amount"]} added to cart')
            elif product.amount == 0:
                print(f'{product.name} out of stock')
            else:
                print(f'Only {product.amount} units available in stock '
                      f'{product.name}, added to cart {product.amount} units')
                product_in_cart = {
                    'product name': product.name,
                    'amount': product.amount,
                    'price': product.selling_price,
                    'sum': product.selling_price * product.amount
                }
                self.cart.append(product_in_cart)
                print(f'{product.name},{product_in_cart["amount"]} added to cart')

    def correct_cart(self, product, amount):
        for prod in self.cart:
            if product.amount >= amount:
                if prod['product name'] == product.name:
                    prod['amount'] = amount
                    prod['sum'] = amount * prod['price']

    def check(self):
        total = 0
        print('\nYour purchase is:')
        for prod in self.cart:
            total += prod['sum']
            print('Product: {}, Amount: {}, Sum: {}'.format(
                prod['product name'], prod['amount'], prod['sum']))
        print('Total costs: {}\n'.format(total))
        return total

    def sell_by_check(self, store):
        for prod in self.cart:
            store._sell_product(prod['product name'], prod['amount'])
        self.cart.clear()

def main():

    p1 = Product('potato', 8)
    p2 = Product('banana', 40)

    store = ProductStore()

    store.add_product(p2, 300)
    print('*'*80)

    my_cart = CartProducts()
    my_cart.check()
    my_cart.add_to_cart(4, p1, p2)
    my_cart.check()
    my_cart.correct_cart(p1, 2)
    store.get_all_products()
    print('*'*80)

    my_cart.check()
    my_cart.sell_by_check(store)
    my_cart.check()
    store.get_all_products()
    print(store.report())

if __name__ == '__main__':
    main()