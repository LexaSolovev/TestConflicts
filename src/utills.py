def summ(a: int, b: int) -> int:
    """Функция суммирует 2 числа"""
    if type(a) != int or type(b) != int:
       raise TypeError("Неверный тип входящего аргумента")
    return a + b
