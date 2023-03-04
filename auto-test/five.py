from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element(By.TAG_NAME, "button")
    button1.click()

    browser.switch_to.alert.accept()
    
    element = browser.find_element(By.ID, "input_value")
    x = element.text
    y = calc(x)
    element_1 = browser.find_element(By.ID, "answer")
    element_1.send_keys(y)


    # Отправляем заполненную форму
    button2 = browser.find_element(By.TAG_NAME, "button")
    button2.click()
    #.btn.btn-primary
finally:
    print(browser.switch_to.alert.text)
    # закрываем браузер после всех манипуляций
    browser.quit()
