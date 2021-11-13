
class ProductRepository:

    def __init__(self):
        self.products = []

    def add(self, product):
        self.products.append(product)

    def find(self, product):
        for p in self.products:
            if p.name == product.name:
                return p

    def remove(self, product_name):
        for p in self.products:
            if p.name == product_name:
                self.products.remove(p)

    def __repr__(self):
        result = []
        for p in self.products:
            result.append(f'{p.name}: {p.quantity}')
        return '\n'.join(result)



