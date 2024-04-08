import random
import string
import datetime


def generate_test_data(data_type, quantity):
    if data_type == 'numeric':
        return [random.randint(0, 100) for _ in range(quantity)]
    elif data_type == 'string':
        return [''.join(random.choices(string.ascii_letters, k=10)) for _ in range(quantity)]
    elif data_type == 'datetime':
        return [datetime.datetime.now() + datetime.timedelta(days=random.randint(-365, 365)) for _ in range(quantity)]
