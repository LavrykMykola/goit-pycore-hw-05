import re
from typing import Callable


def generator_numbers(text: str):
    pattern = r'\d+\.\d+'  # Шаблон для пошуку дійсних чисел
    for match in re.finditer(pattern, text):  # Пошук у тексті дійсних чисел
        yield float(match.group())


def sum_profit(text: str, func: Callable):
    numbers_generator = func(text)  # Викликаємо генератор, щоб отримати всі числа
    total = sum(numbers_generator)  # Підсумовуємо числа
    return total


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
