# Декоратор - это функция, которая добавляет новую
# функциональность к другой функции без изменения её кода.
# Он как бы оборачивает, декорирует функцию, тем самым
# расширяя её возможности.

# Программа, которая меняет регистр с помощью декоратора


def uppercase_decorator(
    function,
):  # указываем имя декоратора и то, что он принимает  function в качестве своей переменной
    def wrapper():  # объявление функции-обёртки wrapper ().
        func = (
            function()
        )  # записываем входящую переменную function () в локальную  переменную func.  «локальная» т.к. она действует только  в рамках функции wrapper ()
        make_uppercase = (
            func.upper()
        )  # применяем к func строковый метод upper и записываем результат в другую локальную переменную make_uppercase.
        return make_uppercase  # функция wrapper() возвращает переменную make_uppercase, то есть строку от function (), но уже прописными буквами.

    return wrapper  # декоратор возвращает нам уже саму функцию wrapper, точнее, результат её работы над функцией function.


@uppercase_decorator
def say_myName():
    return "hello, my name is Inessa!"


print(say_myName())
