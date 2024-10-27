from random import randint, choice


def gen_house_list(n):
    houses=[]
    for _ in range (n):
        price = f'{randint(50000, 100000)}$'
        square = f'{ randint(50, 125)}m2'
        houses.append({'price': price, 'square': square})
    return houses


def gen_customer(n):
    names =  ['Ivan Ivanov',  'Pavel Pavlov']
    customers=[]
    for _ in range(n):
        account = f'{randint(50000, 125000)}$'
        customer_name=choice(names)
        customers.append({ 'full_name': customer_name, "account": account})
    return customers







