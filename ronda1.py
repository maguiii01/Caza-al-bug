from selenium import webdriver
from selenium.webdriver.common.by import By

def test_buscar_libro():
    driver = webdriver.Chrome()
    driver.get("https://books.toscrape.com")
    assert "Books" in driver.title
    titulo = driver.find_element(By.TAG_NAME, "h1")
    assert "All products" in titulo.text
    driver.quit()