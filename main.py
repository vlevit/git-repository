def function(*args, **kwargs):
    list = []
    for arg in args:
        list.append(arg)
    dictionary = {}
    for kwarg in kwargs:
        dictionary[kwarg] = kwargs[kwarg]
    return list, dictionary


def main(*args, **kwargs):
    if args and not kwargs:
        variable = function(*args)
    elif not args and kwargs:
        variable = function(**kwargs)
    elif not args and not kwargs:
        variable = function()
    else:
        variable = function(*args, **kwargs)
    return variable


def not_main():
    return not main()


if __name__ == '__main__':
    main()
else:
    not_main()
