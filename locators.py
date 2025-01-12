from selenium.webdriver.common.by import By


# страница регистрации
class Locators:
    # страница регистрации
    NAME_FIELD_REG = (By.XPATH, './/label[text()="Имя"]/../input')  # поле "Имя"
    EMAIL_FIELD_REG = (By.XPATH, './/label[text()="Email"]/../input')  # поле "Email"
    PASSWORD_FIELD_REG = (By.XPATH, './/label[text()="Пароль"]/../input')  # поле "Пароль"
    REGISTRATION_BUTTON = (By.XPATH, './/button[text()="Зарегистрироваться"]')  # кнопка "Зарегистрироваться"
    PASSWORD_ERROR_MESSAGE = (By.XPATH, './/*[text()="Некорректный пароль"]')  # сообщение о вводе некорректного пароля
    LOGIN_LINK = (By.CLASS_NAME, 'Auth_link__1fOlj')  # ссылка на страницу входа с текстом "Войти"
    # Такой же для страницы восстановления пароля

    # страница входа
    EMAIL_FIELD_LOGIN = (By.XPATH, './/label[text()="Email"]/../input')  # поле "Email"
    PASSWORD_FIELD_LOGIN = (By.XPATH, './/label[text()="Пароль"]/../input')  # поле "Пароль"
    LOGIN_BUTTON = (By.XPATH, './/button[text()="Войти"]')  # кнопка "Войти"
    LOGIN_HEADER = (By.XPATH, './/*[text()="Вход"]')  # заголовок "Вход"

    # главная страница
    MAKE_ORDER_BUTTON = (By.XPATH, './/button[text()="Оформить заказ"]')  # кнопка "Оформить заказ"
    LOGIN_ACCOUNT_BUTTON = (By.XPATH, './/button[text()="Войти в аккаунт"]')  # кнопка "Войти в аккаунт"
    USER_ACCOUNT_LINK_BUTTON = (By.XPATH, './/p[text()="Личный Кабинет"]')  # кнопка ссылка для перехода в личный кабинет

    # конструктор бургеров
    MAKE_BURGER_HEADER = (By.XPATH, './/h1[text()="Соберите бургер"]')  # заголовок "Соберите бургер"
    BUNS_SECTION = (By.XPATH, './/span[text()="Булки"]/..') # раздел "Булки"
    SAUCES_SECTION = (By.XPATH, './/span[text()="Соусы"]/..') # раздел "Соусы"
    FILLINGS_SECTION = (By.XPATH, './/span[text()="Начинки"]/..') # раздел "Начинки"
    FILLINGS_HEADER = (By.XPATH, './/h2[text()="Начинки"]')


    # личный кабинет
    PROFILE_INFO_TEXT = (By.XPATH, ".//p[@class='Account_text__fZAIn text text_type_main-default']") # текст с информацией о разделе
    CONSTRUCTOR_LINK_BUTTON = (By.XPATH, './/p[text()="Конструктор"]') # кнопка ссылка "Конструктор"
    STELLAR_BURGERS_LOGO = (By.CSS_SELECTOR, '.AppHeader_header__logo__2D0X2') # логотип ссылка "Stellar Burgers"
    LOGOUT_BUTTON = (By.XPATH, './/button[text()="Выход"]') # кнопка "Выход"
