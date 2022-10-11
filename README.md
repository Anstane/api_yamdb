# api_yamdb

API проекта api_yamdb.


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
