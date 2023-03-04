from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import math
def calc(x):
    return math.log(abs(12*math.sin(x)))

    
try:
    browser = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течение 5 секунд

    browser.implicitly_wait(5)
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    price = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )

    button = browser.find_element(By.ID, "book")
    button.click()

    


    xfo = browser.find_element(By.ID, "input_value")
    x = int(xfo.text)
    y = str(calc(x))
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)

    button2 = browser.find_element(By.ID, "solve")
    button2.click()
    
    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text)
finally:
    browser.quit()
