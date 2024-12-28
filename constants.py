
class Locators:
    button_reg = "//button[contains(., 'Зарегистрироваться')]" #кнопка Регистрации
    input_name = "//label[text()='Имя']/../input" #инпут имя
    input_email = "//label[text()='Email']/../input" #инпут емейл
    input_pwd = "//label[text()='Пароль']/../input" #инпут пароль
    err_validation = "//p[contains(@class, 'input__error text_type_main-default')]" #ошибка валидации
    button_rolls = "//div[contains(@class, 'noselect') and contains(., 'Булки')]" #кнопка Булки
    button_sauce = "//div[contains(@class, 'noselect') and contains(., 'Соусы')]" #кнопка Соусы
    button_filling = "//div[contains(@class, 'noselect') and contains(., 'Начинки')]" #кнопка Начинки
    cart_filling = "//p[text()='Кристаллы марсианских альфа-сахаридов']"
    button_log_in_main_page = "//button[contains(., 'Войти в аккаунт')]" #Вход на главной
    button_enter = "//button[text()='Войти']" #кнопка Войти
    button_order = "//button[text()='Оформить заказ']" #кнопка Оформить заказ
    button_account = "//p[contains(., 'Личный Кабинет')]" #кнопка ЛК
    button_enter_from_page = "//a[contains(., 'Войти')]" #кнопка Войти со страницы регистрации и забыли пароль
    button_profile = "//a[contains(., 'Профиль')]" #профиль в ЛК
    button_designer = "//p[contains(., 'Конструктор')]" #кнопка Конструктор на главной
    logo = "//div[contains(@class, 'AppHeader_header__logo__2D0X2')]" #лого в хэдере
    text_make_burger = "//h1[contains(., 'Соберите бургер')]" #соберите бургер, текст на главной
    button_exit = "//button[contains(., 'Выход')]" #кнопка выйти со страницы аккаунта

