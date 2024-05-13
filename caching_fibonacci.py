def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:  # Перевіряємо, чи число Фібоначчі вже є у кеші
            return cache[n]
        else:  # Обчислюємо число Фібоначчі
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)  # Зберігаємо обчислене значення у кеші
            return cache[n]

    return fibonacci


fib = caching_fibonacci()
