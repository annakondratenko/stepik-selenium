"""
Есть второй способ для поиска элементов с помощью универсального метода find_element() и полей класса By из библиотеки selenium. Пример:

from selenium import webdriver

from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/simple_form_find_task.html")
button = browser.find_element(By.ID, "submit_button")
Можно использовать те же стратегии поиска, что и в первом способе.
Второй способ более удобен для оформления архитектуры тестовых сценариев с помощью подхода Page Object Model,
 о котором мы будем говорить далее. Пока же предлагаем пользоваться первым методом с явным указанием способа поиска,
  так как он кажется нам более удобным, но ничто не мешает вам пользоваться и тем, и другим. Поля класса By, которые можно использовать для поиска:

By.ID – поиск по уникальному атрибуту id элемента;
By.CSS_SELECTOR – поиск элементов с помощью правил на основе CSS;
By.XPATH – поиск элементов с помощью языка запросов XPath;
By.NAME – поиск по атрибуту name элемента;
By.TAG_NAME – поиск по названию тега;
By.CLASS_NAME – поиск по атрибуту class элемента;
By.LINK_TEXT – поиск ссылки с указанным текстом. Текст ссылки должен быть точным совпадением;
By.PARTIAL_LINK_TEXT – поиск ссылки по частичному совпадению текста.
!Важно. Вы можете столкнуться с ситуацией, когда на странице будет несколько элементов, подходящих под заданные вами параметры поиска.
 В этом случае WebDriver вернет вам только первый элемент, который встретит во время поиска по HTML. Если вам нужен не первый,
 а второй или следующие элементы, вам нужно либо задать более точный селектор для поиска, либо использовать методы find_elements_by,
 которые мы рассмотрим чуть позже.
"""
