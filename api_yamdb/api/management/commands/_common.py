import csv
# from django.shortcuts import get_object_or_404
# from reviews.models import Category

def find_relation(err_message):
    """ValueError: Cannot assign "'1'": "Title.category" must be a "Category" instance."""

    msg = err_message.split(':')

    relation_id = msg[0].replace('Cannot assign ','')
    relation_id = relation_id.replace('"', '')
    relation_id = relation_id.replace("'", '')

    msg = msg[1].split('"')

    field_name = msg[1].split('.')[1]

    model_name = msg[3]

    exec(f'from reviews.models import {model_name}')
    exec(f'from django.shortcuts import get_object_or_404')
    item = eval(f'get_object_or_404({model_name}, id={relation_id})')

    return item, field_name

def create_item(queryset, item):
    item, created = queryset.get_or_create(**item)
    if created:
        print(f'Создан элемент: {item}')

def create_items(file_name, queryset, encoding='UTF-8'):
    """Читает из файла и сохраняет в таблице элементы."""

    with (open(file_name, mode='r', encoding=encoding)) as file_csv:

        print(f'Обработка файла {file_name}')

        reader = csv.reader(file_csv)
        keys = next(reader)  # Advance past the header

        for row in reader:

            item = dict(zip(keys, row))

            try:
                create_item(queryset, item)
            except ValueError as err:
                relation, field_name = find_relation(str(err))
                if relation:
                    item[field_name] = relation
                    create_item(queryset, item)
