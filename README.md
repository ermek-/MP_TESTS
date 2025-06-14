# MP_TESTS

## Описание

Этот репозиторий содержит пример тестов API на Python. Код организован 
в виде эндпоинтов в папке `endpoints` и тестов на `pytest` в папке `tests`.

## Быстрый старт

1. Создайте виртуальное окружение:
   ```bash
   python3 -m venv .venv
   ```
2. При необходимости повторите команду:
   ```bash
   python3 -m venv .venv
   ```
   (например, если нужно пересоздать окружение).
3. Активируйте окружение:
   ```bash
   source .venv/bin/activate
   ```
4. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
5. Укажите значения переменных `USERNAME` и `PASSWORD` в файле `.env` или
   в переменных окружения. Пример в .env.example
6. Запустите тесты:
   ```bash
   pytest
   ```

7. Для генерации Allure-репорта убедитесь, что установлен [Allure CLI](https://docs.qameta.io/allure/), затем запустите тесты:
   ```bash
   pytest --alluredir=allure-results
   ```
   После завершения тестов откройте отчет командой:
   ```bash
   allure serve allure-results
   ```

## Структура проекта

- `endpoints/` – классы для работы с API.
- `tests/` – автотесты, использующие `pytest`.

