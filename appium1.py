import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_cap = {
  "appium:deviceName": "Android Emulator",
  "platformName": "Android",
  "appium:appPackage": "com.walmart.android",
  "appium:appWaitActivity": "com.walmart.glass.onboarding.view.OnboardingActivity",
  "appium:app": "C:\\Users\\Pranshu Sharma\\Downloads\\walmart-22-18.apk"
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_cap)


driver.find_element_by_id("com.walmart.android:id/onboarding_get_started_button").click()
time.sleep(2)
driver.find_element_by_id("com.walmart.android:id/onboarding_zip_code_button").click()
time.sleep(2)
driver.find_element_by_id("com.walmart.android:id/onboarding_zip_code_textinput").send_keys("94088")
time.sleep(2)
driver.find_element_by_id("com.walmart.android:id/onboarding_zip_code_search_button").click()
#driver.find_element_by_id("com.walmart.android:id/error_button").click()

