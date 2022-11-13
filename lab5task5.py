import string
from random import sample


def get_random_password(n=8) -> str:
    uppr = string.ascii_uppercase
    lwr = string.ascii_lowercase
    dgts = string.digits
    rand_pass_list = sample((uppr + lwr + dgts), n)
    return ''.join([v for v in rand_pass_list])


print(get_random_password())
