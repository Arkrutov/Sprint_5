from selenium.webdriver.common.by import By


class Locators:
    BUTTON_REG = (By.XPATH, "//button[contains(., 'Зарегистрироваться')]") #кнопка Регистрации
    INPUT_NAME = (By.XPATH, "//label[text()='Имя']/../input") #инпут имя
    INPUT_EMAIL = (By.XPATH, "//label[text()='Email']/../input") #инпут емейл
    INPUT_PWD = (By.XPATH, "//label[text()='Пароль']/../input") #инпут пароль
    ERR_VALIDATION = (By.XPATH, "//p[contains(@class, 'input__error text_type_main-default')]") #ошибка валидации
    BUTTON_ROLLS = (By.XPATH, "//div[contains(@class, 'noselect') and contains(., 'Булки')]") #кнопка Булки
    BUTTON_SAUCE = (By.XPATH, "//div[contains(@class, 'noselect') and contains(., 'Соусы')]") #кнопка Соусы
    BUTTON_FILLING = (By.XPATH, "//div[contains(@class, 'noselect') and contains(., 'Начинки')]") #кнопка Начинки
    BUTTON_LOG_IN_MAIN_PAGE = (By.XPATH, "//button[contains(., 'Войти в аккаунт')]") #Вход на главной
    BUTTON_ENTER = (By.XPATH, "//button[text()='Войти']") #кнопка Войти
    BUTTON_ORDER = (By.XPATH, "//button[text()='Оформить заказ']") #кнопка Оформить заказ
    BUTTON_ACCOUNT = (By.XPATH, "//p[contains(., 'Личный Кабинет')]")
    BUTTON_ENTER_FROM_PAGE = (By.XPATH, "//a[contains(., 'Войти')]") #кнопка Войти со страницы регистрации и забыли пароль
    BUTTON_PROFILE = (By.XPATH, "//a[contains(., 'Профиль')]") #профиль в ЛК
    BUTTON_DESIGNER = (By.XPATH, "//p[contains(., 'Конструктор')]") #кнопка Конструктор на главной
    LOGO = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo__2D0X2')]") #лого в хэдере
    TEXT_MAKE_BURGER = (By.XPATH, "//h1[contains(., 'Соберите бургер')]") #соберите бургер, текст на главной
    BUTTON_EXIT = (By.XPATH, "//button[contains(., 'Выход')]") #кнопка выйти со страницы аккаунта

class Urls:
    MAIN_PAGE = "https://stellarburgers.nomoreparties.site/"
    LOGIN_PAGE = "https://stellarburgers.nomoreparties.site/login"
    REG_PAGE = "https://stellarburgers.nomoreparties.site/register"
    FORGOT_PWD_PAGE = "https://stellarburgers.nomoreparties.site/forgot-password"

class Data:
    LOGIN = "artemkrutov17@gmail.com"
    PWD = "testpwd"
    NAME = "name"
    REG_EMAIL = "123@ya.ru"
    VALID_PWD = "123456"
    SHORT_PWD = "123"

class Errors:
    USER_ALREADY_EXIST = "Такой пользователь уже существует"
    WRONG_PWD = "Некорректный пароль"