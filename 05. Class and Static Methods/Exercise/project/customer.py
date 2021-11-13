class Customer:
    _ID = 0

    def __init__(self, name, address, email):
        self.name = name
        self.address = address
        self.email = email
        self.id = Customer.get_next_id()

    @staticmethod
    def get_next_id():
        Customer._ID += 1
        return Customer._ID

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"


c1 = Customer('Pete', 'asd', 'email1@gbg.bg')
c2 = Customer('John', 'pdd', 'email2@gbg.bg')
c3 = Customer('Toni', 'xsd', 'email3@gbg.bg')
print(c1)
print(c2)
print(c3)
