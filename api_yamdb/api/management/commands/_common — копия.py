def create_items(file_name, queryset):
    """Читает из файла и сохраняет в таблице элементы."""

    with (open(file_name, mode='r', encoding='UTF-8')) as f:
        names = f.readline().split('\n')[0].split(',')

        for values in f:
            values = values.split('\n')[0].split(',')
            item = dict(zip(names, values))
            # queryset.create(**item)

            print(item)
