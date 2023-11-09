from src.functions import card_number, date_converter, filtering_sorting_list, getting_data_from_file

new = getting_data_from_file('..\\data\\operations.json')
list_dict = filtering_sorting_list(new)

for dict in list_dict:
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
