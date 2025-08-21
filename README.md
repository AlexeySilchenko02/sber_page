# Калькулятор эпизодов Flask

Веб-приложение на Flask с калькулятором эпизодов.

## Структура проекта

```
project/
├── app.py                    # Основной Flask файл
├── requirements.txt          # Зависимости Python
├── templates/
│   └── string_sum.html      # HTML шаблон калькулятора
└── README.md               # Этот файл
```

## Установка и запуск

1. **Создайте папку проекта и перейдите в неё:**
   ```bash
   mkdir flask_calculator
   cd flask_calculator
   ```

2. **Создайте папку templates:**
   ```bash
   mkdir templates
   ```

3. **Скопируйте файлы:**
   - `app.py` в корень проекта
   - `string_sum.html` в папку `templates/`
   - `requirements.txt` в корень проекта

4. **Установите зависимости:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Запустите приложение:**
   ```bash
   python app.py
   ```

## Использование

После запуска приложение будет доступно по адресу:

- **Главная страница:** http://localhost:5000/ (отобразит "Hello")
- **Калькулятор эпизодов:** http://localhost:5000/string-sum