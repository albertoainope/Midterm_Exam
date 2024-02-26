def birthday_days(birthday):
    """

    :param birthday:
    :return: Days on whole years passed since birthday
    """
    current_year = 2024
    birthday_year = birthday[6:]
    diff_years = current_year - int(birthday_year) - 2
    return diff_years * 365
print(birthday_days("01-01-2000"))