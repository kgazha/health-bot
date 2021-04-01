# health-bot

### Использование ###
Для начала нужно в settings.py задать параметр **SOURCE_EXCEL_FILENAME** - путь до исходного excel-файла.
Затем необходимо выполнить скрипт **tools\data_initializer.py** для сохранения исходных данных в виде DataFrame в source_data.

В **analysis\base_nlp_scenario.py** реализована базовая нейронная сеть. Необходимо запустить этот скрипт, чтобы сохранить обученную модель и требуемые данные.
Для проверки работы алгоритма на реальных вопросах используется скрипт **predictor.py**.

**Пример запроса:**
```
# Можно ли отказаться от сдачи анализов на коронавирус? (вопрос в обучающей выборке)
question = "Что если я откажусь от сдачи анализов на covid?"
ints = predict_class(question, model)
print(ints)
```
**Результат:**
>[{'answer': 'Отказаться от сдачи анализов можно. Но только в том случае, если в отношении вас не было постановления санитарного врача о наблюдении и лечении.', 'probability': '0.9715737'}]
