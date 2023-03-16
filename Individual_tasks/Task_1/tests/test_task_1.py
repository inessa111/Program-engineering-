from module.task_1 import sum_polinom
import pytest

#Одна функция проверяет один сценарий (одну ветвь кода)
def test_sum_polinom_3same(): #Имя функции описывает проверяемый сценарий
    #Подготовка данных
    a_data={'x':10,
            'y':8,
            'xy':9}
    b_data={'x':2,
            'y':1,
            'xy':6}
    answer={'x':12,
            'y':9,
            'xy':15}
            
    #Исполнение сценария
    result=sum_polinom(a_data,b_data)

    #Проверка результата
    assert result==answer

def test_sum_polinom_empty_filled(): #а пустая б норм

def test_sum_polinom_empty_empty():

def test_sum_polinom_commutative_property(): #а+б=б+а

def test_sum_polinom_full_diff(): #нет общих членов

def test_sum_polinom_part_diff():  #частичное различие


@pytest.mark.xfail  #тест, который должен падать
def test_fail(): #дробные, строка-строка
    