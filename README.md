# Домашняя работа 12.2
```
╭══ made by ══╮╭═ version ═╮
│    YuZu     ││   0.0.1   │
╰─────────────╯╰───────────╯
```


## Содержание
* [Как использовать](#how-to-use)
* [Краткое описание](#description)



<a id="how-to-use"></a>
## Как использовать

### Минимальные требования:
* Python 3.10 и выше.
* Браузер

### Как запустить проект?
1. Скачать
2. Открыть консоль
3. Перейти в папку проекта (через консоль)
4. Ввести: `pip install -r requirements.txt` (установка нужных библиотек)
5. Ввести: `python run.py` (запуск программы)

При повторном запуске `pip install -r requirements.txt` можно не прописывать :)

### Примечания
После запуска, нужно перейти в браузере по адресу <a href="http://127.0.0.1:5000/" target="_blank">http://127.0.0.1:5000/</a>.



<a id="description"></a>
##  Краткое описание:


| Название | URL | Описание |
|--|:--:|--|
| Главная | `/` | Главная страница + поиск постов по вхождению слова|
| Результаты поиска |`/search/?s=...`| Все посты с найденой строкой |
| Добавление поста | GET `/post` | Страница где можно добавлять новый пост (с загрузкой фотографии и печатью текста) |
| Просмотр добавленного поста | POST `/post` | Можно посмотреть на свой новый пост :) |
