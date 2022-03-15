def add_protocol(secure=False):

    print('1. Я обертка над декоратором. Называй меня Главная обертка. Я буду создавать декоратор. У меня есть параметр secure =', secure)

    def decorator(decorated_function):

        print('2. Я сам декоратор. Я подчиняюсь Главной обертке. Я вижу все, что есть у Главной обертки. Я тоже вижу параметр secure =', secure)

        def wrapper(*args, **kwargs):
            print(f"""3. Я обертка над декорируемой функцией. Я подчиняюсь декоратору и Главной обертке, поэтому я вижу все, что есть у них:
                  - параметр secure: {secure};
                  - функцию, которая есть у декоратора decorated_function: {decorated_function};
                  - все аргументы, которые переданы при вызове декорируемой функции *args, **kwargs: {args}, {kwargs}."""
                  )
            result_url = decorated_function(*args, **kwargs)
            if secure:
                result_url = 'https://' + result_url
            else:
                result_url = 'http://' + result_url
            return result_url

        return wrapper

    return decorator


@add_protocol(True)
def get_absolute_url(domain, *args, **kwargs):
    for i in args:
        domain += f'/{i}'

    if kwargs:
        domain += '/?'
        for k, v in kwargs.items():
            domain += f'{k}={v}&'
        domain = domain[:-1]
    return domain


print(get_absolute_url('yandex.ru'))
print(get_absolute_url('yandex.ru', 'news', 'football', person='Messi'))