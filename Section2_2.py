from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

page = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(page)

try:
    #find value xx
    x = int(browser.find_element_by_xpath("//span[@id='num1']").text)
    y = int(browser.find_element_by_xpath("//span[@id='num2']").text)

    #calculate sum
    sum = str(x + y)
    print(sum)

    #select value from drop_down
    select = Select(browser.find_element_by_xpath("//select"))
    select.select_by_value(sum)

    #press Submit
    browser.find_element_by_xpath("//button").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()

