import random
import string

def generate_login(name="test", surname="testov", cohort=6, domain="yandex.ru"):

    random_numbers = ''.join(random.choices(string.digits, k=3))
    return f"{name}_{surname}_{cohort}_{random_numbers}@{domain}"

def generate_valid_password(min_length=6, max_length=20):

    length = random.randint(min_length, max_length)
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(chars, k=length))

def generate_invalid_password(max_length=5):

    length = random.randint(1, max_length)
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(chars, k=length))