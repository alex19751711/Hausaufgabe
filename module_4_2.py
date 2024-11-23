def test_function():
    def inner_function():
      print('Я внутри функции test_function')
    inner_function()
    return
test_function()
#inner_function() не работает, так как выходит за пределы видимости
