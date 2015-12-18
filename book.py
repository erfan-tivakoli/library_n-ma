__author__ = 'Rfun'


class Book():
    def __init__(self, id, name, quantity):
        self.id = id
        self.name = name
        self.quantity = quantity

    def update_id(self, id):
        self.id = id

    def update_name(self, name):
        self.name = name

    def update_quantity(self, quantity):
        self.quantity = quantity

    def __str__(self):
        result = ''
        result += 'the book is:\n'
        result += 'id: ' + self.id +'\n'
        result += 'name: ' + self.name + '\n'
        result += 'quantitiy: ' + self.quantity + '\n'
        return result



