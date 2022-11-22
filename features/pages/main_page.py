from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_cap = {
        "platformName": "Android",
        "automationName": "uiautomator2",
        "app": "\\mobile\\apk\\calculator.apk",
        "appPackage": "com.android.calculator",
        "appActivity": "com.android.calculator.Calculator"
    }

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)

def Click_calc(btn):
    driver.find_element_by_accessibility_id(btn).click()

def Result():
    result = driver.find_element_by_id("com.android.calculator:id/result").text
    driver.quit()
    return result

class MainPage():

    def do_calculation(operator,FIRST_NUM,SECOND_NUM):
        carac1 = FIRST_NUM[0]
        carac2 = FIRST_NUM[1]
        carac3 = SECOND_NUM[0]
        carac4 = SECOND_NUM[1]
        if operator == 'sum':
            oper = 'plus'
        elif operator == 'sub':
            oper = 'minus'

        Click_calc(carac1)
        Click_calc(carac2)
        Click_calc(oper)
        Click_calc(carac3)
        Click_calc(carac4)
        Click_calc('equals')

        return Result()

        
  
  