from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_cap = {
    "appium:deviceName": "Android Emulator",
    "platformName": "Android",
    "appium:appPackage": " com.instagram.android",
    "appium:appActivity": "com.instagram.mainactivity.MainActivity",
    "appium:app": "C:\\Users\\Pranshu Sharma\\Downloads\\instagram-234-0-0-19-113.apk",
    "appium:appWaitForLaunch": "false"
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_cap)
#driver.set_page_load_timeout(5000)

driver.implicitly_wait(20)
el1 = driver.find_element(by=AppiumBy.ID, value="com.instagram.android:id/tab_avatar")
el1.click()
driver.implicitly_wait(20)
el2 = driver.find_element(by=AppiumBy.ID, value="com.instagram.android:id/action_bar_title_chevron")
el2.click()

el4 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[5]/android.widget.LinearLayout/android.widget.TextView")
el4.click()


el7 = driver.find_element(by=AppiumBy.ID, value="com.instagram.android:id/secondary_button")
el7.click()


el11 = driver.find_element(by=AppiumBy.ID, value="com.instagram.android:id/username")
el11.send_keys("appiumTesting5")


el13 = driver.find_element(by=AppiumBy.ID, value="com.instagram.android:id/button_text")
el13.click()


el14 = driver.find_element(by=AppiumBy.ID, value="com.instagram.android:id/password")
el14.send_keys("appiumTesting123@")


el15 = driver.find_element(by=AppiumBy.ID, value="com.instagram.android:id/button_text")
el15.click()


el16 = driver.find_element(by=AppiumBy.ID, value="com.instagram.android:id/button_text")
el16.click()


el17 = driver.find_element(by=AppiumBy.ID, value="com.instagram.android:id/skip_button")
el17.click()


el18 = driver.find_element(by=AppiumBy.ID, value="com.instagram.android:id/negative_button")
el18.click()


el19 = driver.find_element(by=AppiumBy.ID, value="com.instagram.android:id/skip_button")
el19.click()
