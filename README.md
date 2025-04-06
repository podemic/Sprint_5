
Проект по автоматизации тестов для Stellar Burgers 
https://stellarburgers.nomoreparties.site/

Проект написан с использованием менеджера вебдрайвера, т.е. драйвер не был установлен на устройстве.
Автотесты проходятся внутри браузера Chrome.
Фикстуры хранятся в файле conftest.py
Локаторы хранятся в файле locators.py
Тестовые данные юзера хранятся в файле data.py
Генераторы тестовых кредов описаны в файле creditsgenerator.py
Описание проекта в README.md

Проект содержит автотесты для
1.Страницы регистрации : test_user_registration.py
2.Аутентификации юзера с разных страниц : test_user_authentication.py
3.Логаут юзера из Личного кабинета : test_user_logout.py
4.Переход юзера в Личный кабинет : test_navigation_to_personal_account_page.py
5.Переход юзера из Личного кабинета на страницу конструктора : test_navigation_to_constructor_page.py
6.Переходы между блоками конструктора : test_constructor_page.py

Запуск всех тестов 
pytest -v

2025 год, 5 спринт, Яндекс Практикум, Планета Земля




