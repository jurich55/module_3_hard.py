
def calculate_structure_sum(data_structure):
    sum_data_structure = 0
    if isinstance(data_structure, dict):            # если есть словарь (dict)
        for key, value in data_structure.items():   # применяем items()
            sum_data_structure += calculate_structure_sum(key)    # - добавляем ключ
            sum_data_structure += calculate_structure_sum(value)  # - добавляем значения
                                     # для других типов данных добавляем второй цикл
    elif isinstance(data_structure, (list, tuple, set)):
        for item in data_structure:
            sum_data_structure += calculate_structure_sum(item)

    elif isinstance(data_structure, (int, float)):   # если значение - число - (int или float)
        sum_data_structure += data_structure         # добавляем число

    elif isinstance(data_structure, str):            # если значение - строка
        sum_data_structure += len(data_structure)    # добавляем ее длину -(len)
    return sum_data_structure          # возврат результата выполнения функции


data_structure = [[1, 2, 3], {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}), "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])]
result = calculate_structure_sum(data_structure)
print(result)


