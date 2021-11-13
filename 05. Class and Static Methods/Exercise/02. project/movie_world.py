class MovieWorld:
    _DVD_CAPACITY = 15
    _CUSTOMER_CAPACITY = 10

    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return MovieWorld._DVD_CAPACITY

    @staticmethod
    def customer_capacity():
        return MovieWorld._CUSTOMER_CAPACITY

    def add_customer(self, customer):
        if len(self.customers) < MovieWorld._CUSTOMER_CAPACITY:
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < MovieWorld._DVD_CAPACITY:
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):

        for customer in self.customers:
            if customer.id == customer_id:
                for dvd in customer.rented_dvds:
                    if dvd.id == dvd_id:
                        return f"{customer.name} has already rented {dvd.name}"

        for dvd in self.dvds:
            if dvd.id == dvd_id:
                if dvd.is_rented:
                    return "DVD is already rented"
                for customer in self.customers:
                    if customer.id == customer_id:
                        if customer.age < dvd.age_restriction:
                            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
                        dvd.is_rented = True
                        customer.rented_dvds.append(dvd)
                        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        for customer in self.customers:
            if customer.id == customer_id:
                for dvd in customer.rented_dvds:
                    if dvd.id == dvd_id:
                        dvd.is_rented = False
                        customer.rented_dvds.remove(dvd)
                        return f"{customer.name} has successfully returned {dvd.name}"
                return f"{customer.name} does not have that DVD"

    def __repr__(self):
        result = []
        for customer in self.customers:
            result.append(repr(customer))
        for dvd in self.dvds:
            result.append(repr(dvd))
        return '\n'.join(result)




