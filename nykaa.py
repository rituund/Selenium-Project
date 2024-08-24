from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up the Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

try:
    # Open Nykaa Fashion website
    driver.get("https://www.nykaafashion.com/")

    # Allow the page to load
    time.sleep(3)

    # Close the overlay if it appears
    try:
        overlay_close_button = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='wzrk-overlay']"))
        )
        overlay_close_button.click()
        print("Overlay closed.")
    except (TimeoutException, NoSuchElementException):
        print("Overlay not found or not clickable.")

    # Locate the search bar and perform the search
    search_bar = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, '//input[@aria-label="Search"]'))
    )
    search_bar.send_keys("TOPS FOR WOMEN")
    search_bar.send_keys(Keys.RETURN)

    # Wait for the search results to load
    time.sleep(3)
    print("Search results loaded.")

    # Locate the specific product using the provided XPath
    specific_product_xpath = "//div[@id='aria-label-12454694-1']"
    specific_product = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, specific_product_xpath))
    )
    specific_product.click()
    print("Specific product clicked.")

    # Switch to the new tab (product details page)
    WebDriverWait(driver, 15).until(lambda d: len(d.window_handles) > 1)
    driver.switch_to.window(driver.window_handles[1])
    print("Switched to product details tab.")

    # Wait for the size options to be visible and select size Medium
    size_option = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='M']"))
    )
    size_option.click()
    print("Size Medium selected.")

    # Wait for the add to cart button to be clickable
    add_to_cart_button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@class='addToBagButtonContainer css-osm75t']"))
    )
    add_to_cart_button.click()
    print("Product added to cart.")

    # Wait for the view bag button to be clickable
    view_bag_button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@class='addToBagButtonContainer css-1p7rtgz']"))
    )
    view_bag_button.click()
    print("View Bag button clicked.")

    # Wait to ensure the cart page is loaded
    time.sleep(3)
    print("Cart page loaded.")

except (TimeoutException, ElementClickInterceptedException, NoSuchElementException) as e:
    print(f"An error occurred: {e}")

finally:
    time.sleep(100)
    # Close the WebDriver
    driver.quit()
