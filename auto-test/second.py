from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("window.scrollBy(0, 100);")
button.click()
# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
 # закрываем браузер после всех манипуляций
browser.quit()
