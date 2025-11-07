# Weather
## О проекте
Сервис по получении погоды по городам, с сохранение и фильтрацией запросов
## Требования
- python 3.10+ (+ pip)
- postgres 14
## Уставонка
- запустить сервер postgres на localhost:5432 и создать базу данных weather
- скачать репозиторий
- запустить терминал в папке `/backend`
- запустить виртуальное окружение python
  `python3 -m venv .venv`
  `source .venv/bin/activate`
- установить зависимости `pip install -r requirements.txt`
- запустить сервер `uvicorn src.app:app --reload`
- интерфейс в сервису доступен по адресу `http://127.0.0.1:8000/doc`
