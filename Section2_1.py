from selenium import webdriver
import time
import math

page = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(page)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    #find value x
    element = browser.find_element_by_xpath("//span[@id='input_value']").text

    #calculate function x
    function_x = calc(element)

    #type function x into text field
    text_field = browser.find_element_by_xpath("//input[@id='answer']").send_keys(function_x)

    #select checkbox and radiobutton
    browser.find_element_by_xpath("//input[@id='robotCheckbox']").click()
    browser.find_element_by_xpath("//input[@id='robotsRule']").click()

    #press Submit
    browser.find_element_by_xpath("//button").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

