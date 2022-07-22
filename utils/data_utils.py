import datetime


def generate_datetime():
    return f'"{datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ")}"'


def format_list_input_with_string_values(list_input):
    """
    Функция для форматирования значений словаря в списке, все значения которого типа string

    :param list_input: список словарей, в которых все значения имеют тип string
    """
    if isinstance(list_input, dict):
        return {key: f"'{value}'" for key, value in list_input.items()}
    return list_input
