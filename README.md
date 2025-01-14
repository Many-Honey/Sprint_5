# Sprint_5_qa_python
### Описание
Проект тестирования сайта Stellar Burgers
### Использование
- Для запуска тестов должен быть установлен пакет `pytest` и `selenium`
- Запуск всех тестов с подробным выводом результатов выполняется командой `pytest -v tests.py`
### Содержание проекта
- locators.py - локаторы объединенные в класс Locators
- README.md - описание проекта
- папка tests:
  - conftest.py - фикстуры для тестов
  - test_burger_constructor_navigation.py - класс TestBurgerConstructorNavigation объединяющий набор тестов, покрывающих функцию конструктора бургеров
    - `test_go_to_fillings_section_by_click_on_fillings` - переход в раздел "Начинки"
    - `test_go_to_buns_section_by_click_on_buns` - переход в раздел "Булки"
    - `test_go_to_sauces_section_by_click_on_sauces` - переход в раздел "Соусы"
  - test_login_page.py - класс TestLoginPage объединяющий набор тестов входа в личный кабинет
    - `test_log_in_by_log_in_to_account_button_main_page` - вход по кнопке «Войти в аккаунт» на главной
    - `test_log_in_by_profile_link_button_main_page` - вход через кнопку «Личный кабинет»
    - `test_log_in_by_log_in_link_registration_page` - вход через кнопку в форме регистрации
    - `test_log_in_by_log_in_link_password_recovery_page` - вход через кнопку в форме восстановления пароля
  - test_registration_page.py - класс TestRegistrationPage объединяющий набор тестов регистрации пользователя
    - `test_successful_registration` - успешная регистрация
    - `test_input_password_less_than_6_characters_error_message` - ошибка при вводе некорректного пароля
  - test_user_account_navigation.py - класс TestUserAccountNavigation объединяющий набор тестов навигации в личном кабинете
    - `test_go_to_user_account_by_user_account_link_from_main_page` - переход по клику на «Личный кабинет»
    - `test_go_to_burger_constructor_by_constructor_link_button` - переход на главную страницу по клику на «Конструктор»
    - `test_go_to_burger_constructor_by_stellar_burgers_logo` - переход на главную страницу по клику на логотип Stellar Burgers
    - `test_logout_from_user_account` - выход из аккаунта по кнопке «Выйти» в личном кабинете.