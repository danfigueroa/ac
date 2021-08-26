pessoas = list()

def cadastrar_pessoa(pessoa):
    global pessoas
    pessoas = pessoa


def create_item(name, price, quantity):
    global items
    items.append({'name': name, 'price': price, 'quantity': quantity})