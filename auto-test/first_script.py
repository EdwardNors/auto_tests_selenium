from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


try: 
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    element = browser.find_element(By.ID, "num1")
    element2 = browser.find_element(By.ID, "num2")
    
    x = int(element.text) + int(element2.text)
    print(x)
    select = Select(browser.find_element(By.TAG_NAME, "select"))

    select.select_by_visible_text(str(x))
    


    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()