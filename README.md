# djangodemo
## Проект для подготовки к демо экзамену (Python/Django)

### Разработка интернет-магазина

## Использованные технологии:
- Python 3.11
- Django 4.2.3
- PostgreSQL 14

## Инструменты:
- PgAdmin 4 v6
- pip 23.2
- PyCharm 2022.1 (Community Edition)

## venv (pip list)  
- asgiref    3.7.2  
- Django     4.2.3
- Pillow     10.0.0
- pip        23.2   
- psycopg2   2.9.6  
- setuptools 65.5.0 
- sqlparse   0.4.4  
- tzdata     2023.3 


## Использованный материал
- [Документация (Официальный сайт)](https://www.djangoproject.com/)
- [Документация на русском языке](https://django.fun/ru/)
- [Сайт metanit](https://metanit.com/python/django/1.1.php)
- [Сайт Django Girls](https://tutorial.djangogirls.org/ru/) (:smile:)

## Helper (Набор команд и настроек для разработки проекта)

#### Установка виртуальной среды
python -m venv venv

#### Активация виртуальной среды
venv\Scripts\activate.bat

#### Установка Django
python -m pip install Django

#### Создание проекта
django-admin startproject __root__

#### Создание приложения
python manage.py startapp __shop__

#### Установка пакета для работы с PostgreSQL в  Django
pip install psycopg2

#### Установка пакета для работы с изображениями
python -m pip install Pillow

#### Запуск сервера разработки
##### С начало необходимо перейти в папку проекта __root__
python manage.py runserver

## Внимание settings.info
В целях безопасности файл перименован и изменен. Удален секретный ключ приложения, пармаетры доступа в БД 
