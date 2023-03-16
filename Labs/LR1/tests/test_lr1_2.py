from module.lr1_2 import stringing
import pytest

#Одна функция проверяет один сценарий (одну ветвь кода)
def test_stringing_equal(): #Имя функции описывает проверяемый сценарий
    #Подготовка данных
    data='abcdefghijklmnopqrstuv18340'
    answer=True

    #Исполнение сценария
    result=stringing(data)

    #Проверка результата
    assert result==answer


#Одна функция проверяет один сценарий (одну ветвь кода)
def test_stringing_not_equal(): #Имя функции описывает проверяемый сценарий
    #Подготовка данных
    data='abcdefghijklmnoasdfasdpqrstuv18340'
    answer=False

    #Исполнение сценария
    result=stringing(data)

    #Проверка результата
    assert result==answer    


#Одна функция проверяет один сценарий (одну ветвь кода)
def test_stringing_equal_with_spaces(): #Имя функции описывает проверяемый сценарий
    #Подготовка данных
    data=' abcdefghijklmnopqrstuv18340 '
    answer=False

    #Исполнение сценария
    result=stringing(data)

    #Проверка результата
    assert result==answer    
   

def test_stringing_none(): #Имя функции описывает проверяемый сценарий
    #Подготовка данных
    data=None
    answer=False

    #Исполнение сценария
    result=stringing(data)

    #Проверка результата
    assert result==answer    


@pytest.mark.xfail  #тест, который должен падать
def test_fail(): #Имя функции описывает проверяемый сценарий
    #Подготовка данных
    data='abcdefghijklmnopqrstuv18340'
    answer=True

    #Исполнение сценария
    result=stringing(data)

    #Проверка результата
    assert result!=answer


#Одна функция проверяет один сценарий (одну ветвь кода)
def test_stringing_int(): #Имя функции описывает проверяемый сценарий
    #Подготовка данных
    data=123
    answer=False

    #Исполнение сценария
    #Тест считается успешным,если и только если будет выброшено исключение соответсвующего типа
    with pytest.raises(TypeError):
        result=stringing(data)


def test_stringing_double(): #Имя функции описывает проверяемый сценарий
    #Подготовка данных
    data='abcdefghijklmnopqrstuv18340abcdefghijklmnopqrstuv18340'
    answer=False

    #Исполнение сценария
    result=stringing(data)

    #Проверка результата
    assert result==answer  


def test_stringing_pre(): #Имя функции описывает проверяемый сценарий
    #Подготовка данных
    data='ffffffabcdefghijklmnopqrstuv18340'
    answer=False

    #Исполнение сценария
    result=stringing(data)

    #Проверка результата
    assert result==answer 
    

def test_stringing_post(): #Имя функции описывает проверяемый сценарий
    #Подготовка данных
    data='abcdefghijklmnopqrstuv18340fffff'
    answer=False

    #Исполнение сценария
    result=stringing(data)

    #Проверка результата
    assert result==answer
#pytest --cov-report html --cov=module tests/
#pytest --cov-report term --cov=module tests/