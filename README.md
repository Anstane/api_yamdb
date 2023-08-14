# api_yamdb

Совместно созданное API для сервиса по написанию отзывов о фильмах, сериалах, музыке и книгах.

Стек технологий: Django 2.2.16 | DRF 3.12.4
Аутентификация была реализована с помощью - DRF Simple JWT

В ходе создания этого проекта удалось испробовать себя на роли куратора проекта, разделяя между участниками отвественность, а также курируя процесс merge`а веток.

## Установка проекта

Как установить проект:

```bash
git clone git@github.com:Anstane/api_yamdb.git

cd api_yamdb
```
Создаём и активируем виртуальное окружение:
```bash
python -m venv venv

source venv/Scripts/activate
```
Устанавливаем зависимости из файла requirements.txt:
```bash
pip install -r requirements.txt
```
Выполняем миграции:
```bash
python manage.py migrate
```
Активируем сам проект:
```bash
python manage.py runserver
```
## Документация проекта

`/redoc/`


## Авторы

- [@Anstane](https://github.com/Anstane)
- [@altvik2503](https://github.com/altvik2503)
- [@DianaKab](https://github.com/DianaKab)
