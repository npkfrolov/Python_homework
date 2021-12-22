# Написать скрипт, автоматизирующий сохранение данных в файле YAML-формата.

import yaml

data = {
    'first_key': ['one', 'two', 'три'],
    'second_key': 4,
    'third_key': {
        'one': 405,
        'two': 689,
    }
}

with open('file.yaml', 'w') as file:
    yaml.dump(data, file, default_flow_style=False, allow_unicode=True)

with open('file.yaml') as file:
    print(file.read())


