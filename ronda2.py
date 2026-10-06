from selenium.webdriver.common.by import By

def test_login_valido(driver):
    driver.get("https://the-internet.herokuapp.com/login")

    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    mensaje = driver.find_element(By.ID, "flash")
    assert mensaje.is_displayed()
    assert "You logged into a secure area!" in mensaje.text

    driver.find_element(By.CSS_SELECTOR, "a[href='/logout']").click()
    assert driver.current_url.endswith("/login")
    assert "You logged out of the secure area!" in driver.find_element(By.ID, "flash").text