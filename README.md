# AQA_qatest_606ep_ru
### Предназначен для оценки качества сайта https://qatest.606ep.ru/ в автоматизированном режиме. Автотесты  написаны  с применением  языка программитрования Python, а также фреймворков Pytest и Selenium. 
________________________________________________________________________
## Инструкция по развертыванию проекта
1. Создать виртуальное окружение `python -m venv venv`
2. Активировать виртуальное окружение на git bash `source ./venv/Scripts/activete`
3. Установить зависимости из файла requirements.txt `pip install -r requirements.txt`
4. Скачать и сохранить в корневой папке проекта [chromedriver](https://chromedriver.chromium.org/downloads) или [geckodriver](https://github.com/mozilla/geckodriver/releases)
5. В случаи возникновения трудностей с установкой драйверов прочитайте [Инструкцию по установке chromedriver](https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/) или [Инструкцию по установке geckodriver](https://selenium-python.com/install-geckodriver)
________________________________________________________________________
## Запуск проекта 
1. Запустить автотесты  в браузере chrome с помощью git bash `pytest -rx test_enter_page.py`
2. Запустить автотесты в браузере firefox с помощью git bash `pytest -rx --browser_name=firefox test_enter_page.py`
________________________________________________________________________

## Документация проекта
[Тестовая документация](https://drive.google.com/drive/folders/1W467_aNik1rMmM1jm3IaXzI02v6DqqhP?usp=sharing)