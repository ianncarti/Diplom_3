# Проект автоматизации тестирования приложения для заказа космических бургеров
* Основа для написания автотестов — фреймворки pytest и selenium
* Команда для запуска тестов — pytest -v
* В webdriver_factory.py реализована возможность выбора браузера для тестов pytest --browser=chrome(или firefox)
* Собрать отчёт о тестировании - pytest tests*test_name.py --alluredir=allure_results
* Посмотреть наглядно отчёт можно с помощью команды allure serve allure_results
* в helpers.py реализован генератор кредов для аккаунта