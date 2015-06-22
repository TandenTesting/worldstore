import string
import random
import uuid

def id_generator(size=6, chars=string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))

def get_uuid1():
    return uuid.uuid1()    

