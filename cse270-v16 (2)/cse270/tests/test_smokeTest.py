import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pytest

@pytest.fixture(scope="module")
def browser():
    # Headless mode (optional for CI environments)
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_smokeTest(browser):
    # Step 1: Go to the website
    browser.get("https://lit-caverns-51357-28f7fd6f5f4b.herokuapp.com/")

    # Step 2: Click the "Create" link
    browser.find_element(By.LINK_TEXT, "Create").click()

    # Step 3: Fill in the form
    browser.find_element(By.ID, "make").click()
    browser.find_element(By.ID, "make").send_keys("TestMake")

    browser.find_element(By.ID, "model").click()
    browser.find_element(By.ID, "model").send_keys("TestModel")

    browser.find_element(By.ID, "year").click()
    browser.find_element(By.ID, "year").send_keys("2023")

    # Step 4: Click the "Create" button
    browser.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

    # Step 5: Verify the car was created
    body_text = browser.find_element(By.TAG_NAME, "body").text
    assert "TestMake" in body_text
    assert "TestModel" in body_text
