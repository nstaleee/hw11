def live(age: int) -> str:
    if age < 0:
        return 'неможливо'
    elif age <= 18:
        return 'Ви дитина'
    elif age <= 65:
        return 'працюйте більше'
    else:
        return 'Гарноґ пенмії'
