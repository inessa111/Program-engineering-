from module.task_1 import sum_polinom
import pytest


# Одна функция проверяет один сценарий (одну ветвь кода)
def test_sum_polinom_3same():  # Имя функции описывает проверяемый сценарий
    # Подготовка данных
    a_data = {"x": 10, "y": 8, "xy": 9}
    b_data = {"x": 2, "y": 1, "xy": 6}
    answer = {"x": 12, "y": 9, "xy": 15}

    # Исполнение сценария
    result = sum_polinom(a_data, b_data)

    # Проверка результата
    assert result == answer


def test_sum_polinom_empty_filled():  # а пустая б нормальная
    a_data = dict()
    b_data = {"x": 10, "y": 19, "xy": 63}
    answer = {"x": 10, "y": 19, "xy": 63}
    # Исполнение сценария
    result = sum_polinom(a_data, b_data)

    # Проверка результата
    assert result == answer


def test_sum_polinom_empty_empty():
    a_data = dict()
    b_data = dict()
    answer = dict()
    # Исполнение сценария
    result = sum_polinom(a_data, b_data)

    # Проверка результата
    assert result == answer


def test_sum_polinom_full_diff():  # нет общих членов
    # Подготовка данных
    a_data = {"x^2": 10, "x^10": 8, "xy": 9}
    b_data = {"x^2": 2, "x^10": 1, "ab": 6}
    answer = {"x^2": 12, "x^10": 9, "xy": 9, "ab": 6}

    # Исполнение сценария
    result = sum_polinom(a_data, b_data)

    # Проверка результата
    assert result == answer


def test_sum_polinom_part_diff():  # частичное различие
    # Подготовка данных
    a_data = {"x": 10, "y": 8, "xy": 9}
    b_data = {"a": 2, "b": 1, "xy": 6}
    answer = {"x": 10, "y": 8, "xy": 15, "a": 2, "b": 1}

    # Исполнение сценария
    result = sum_polinom(a_data, b_data)

    # Проверка результата
    assert result == answer


@pytest.mark.xfail  # тест, который должен падать
def test_fail():  # дробные, строка-строка
    # Подготовка данных
    a_data = {"x": "c", "y": 8.6, "xy": "fafds"}
    b_data = {"x": 2, "y": 1, "xy": "sssss"}
    answer = {"x": 12, "y": 9, "xy": 15}

    # Исполнение сценария
    result = sum_polinom(a_data, b_data)

    # Проверка результата
    assert result != answer
