import os
from uuid import uuid4

def random_filename(instance,filename: str):
    upload_to = f'{instance.__class__.__name__}/'
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid4().hex, ext)
    return os.path.join(upload_to, filename)