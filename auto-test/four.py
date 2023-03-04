from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os


try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    element_1 = browser.find_element(By.NAME, "firstname")
    element_1.send_keys("Artem")
    element_2 = browser.find_element(By.NAME, "lastname")
    element_2.send_keys("gay")
    element_3 = browser.find_element(By.NAME, "email")  
    element_3.send_keys("Artem")
    filee = browser.find_element(By.ID, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    filee.send_keys(file_path)
    
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text)
    # закрываем браузер после всех манипуляций
    browser.quit()
