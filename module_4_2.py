def test_function():
    print('Работает функция: test_function')

    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()


inner_function()
# Результат: NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?
