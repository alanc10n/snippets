""" A snippet to remind me how decorators work in python """

def instrument(f):
    """ This is the definition for the decorator """

    def wrapper():
        print "Before {}".format(f.__name__)
        f()
        print "After {}".format(f.__name__)

    return wrapper

@instrument
def some_func():
    print "This is some function"

def main():
    some_func()

if __name__ == '__main__':
    main()
