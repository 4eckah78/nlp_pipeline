## Установка

В корне проекта выполните команду
```bash
pip install -r requirements.txt
```

Для работы программы необходимо **загрузить модель**

В корне проекта выполните команду
```bash
python -m spacy download ru_core_news_sm
```


## Описание API

### 127.0.0.1:5000/nlp_pipeline
Возвращает токены 
- **method** - POST
- **body** - {"text": str} (словарь с ключом text)
- **response** - {"tokens": список токенов}

### 127.0.0.1:5000/search
Ищет топ 3 релевантных документа по запросу
- **method** - POST
- **body** - {"query": str} (словарь с ключом query и типом str)
- **response** - {"results": список документов}


## Пример запроса к /nlp_pipeline
Для обращения к API можно использовать код
```python
import requests

url = "http://127.0.0.1:5000/nlp_pipeline"
data = {"text": "Ваш текст"}
response = requests.post(url, json=data)
print(response.json())
```
## Пример запроса к /search
```python
import requests

url = "http://127.0.0.1:5000/search"
data = {"query": "Ваш текст"}
response = requests.post(url, json=data)
print(response.json())
```
