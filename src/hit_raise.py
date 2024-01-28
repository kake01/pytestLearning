class MyError(Exception):
    pass

def my_raise():
    raise MyError('MyErrorが発生')
