from selenium.webdriver.common.by import By

def test_quotes_flujo(driver):
    # 1. Entrar al login
    driver.get("https://quotes.toscrape.com/login")

    # 2. Credenciales falsas
    driver.find_element(By.ID, "username").send_keys("usuario_falso")
    driver.find_element(By.ID, "password").send_keys("clave_falsa")
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

    # 3. El sitio acepta cualquier credencial: aparece el link Logout
    assert driver.find_element(By.LINK_TEXT, "Logout").is_displayed()

    # 4. Volver al inicio y contar citas
    driver.get("https://quotes.toscrape.com/")
    citas = driver.find_elements(By.CLASS_NAME, "quote")
    assert len(citas) == 10

    # 5. Click en el autor de la primera cita
    url_inicial = driver.current_url
    driver.find_element(By.CSS_SELECTOR, ".quote a[href^='/author']").click()
    assert driver.current_url != url_inicial
    assert "/author/" in driver.current_url