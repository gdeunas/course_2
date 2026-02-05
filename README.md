# Project "course_2"

## Описание:

Проект course_2- это приложение на Python.

## О проекте

Создание приложения с выводом курса валюты, обработка XL и вывод json.
Разработан на IDE PyCharm 2025.2.5

## Шаги установки:

1. Как клонировать проект
````
clone https://github.com/gdeunas/course_2.git
cd course_2
````
2. Настройте виртуальное окружение и установите зависимости:
````
python -m venv env
source env/bin/activate  # Linux/MacOS
env\Scripts\activate     # Windows
````
Для dev:
````
poetry add isort
poetry add mypy
poetry add flake8
poetry add black
````

## Создать html файлы с покрытием
````
pytest --cov=src --cov-report=html 
````
Создаться папка htmlcov с покрытием.


## Структуры проекта
````
project_folder
├── data
├── src
├── tests
├── main.py
├── pyproject.toml
├── poetry.lock
└── README.md
````

## Документация:

Для получения дополнительной информации обратитесь к [документации] (docs/README.md).

## Лицензия:

Этот проект лицензирован по [лицензии MIT] (LICENSE).