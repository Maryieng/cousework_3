from src.functions import getting_data_from_file, filtering_sorting_list, card_number, date_converter

new = getting_data_from_file('..\data\operations.json')  # получение списка из файла
list_dict = filtering_sorting_list(new)                  # получение последних 5 завершенных операций

for dict in list_dict:                                   # цикл по списку и вывод информации в консоль
    if dict['description'] == 'Открытие вклада':
        print(f'''{date_converter(dict['date'])} {dict['description']}
{card_number(dict['to'])}
{dict['operationAmount']['amount']} {dict['operationAmount']['currency']['name']}
''')
    else:
        print(f'''{date_converter(dict['date'])} {dict['description']}
{card_number(dict.get('from'))} -> {card_number(dict['to'])}
{dict['operationAmount']['amount']} {dict['operationAmount']['currency']['name']}
''')
