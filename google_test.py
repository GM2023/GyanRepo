from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_google():
    # Initialize the WebDriver (make sure to download the correct WebDriver for your browser)
    driver = webdriver.Chrome()  # Ensure that chromedriver is in your PATH or specify the path

    try:
        # Open google.com
        driver.get("https://www.google.com")

        # Check if the Google logo is present to ensure the page loaded
        logo = driver.find_element(By.ID, "hplogo")

        # Assert that logo is displayed (it means the page is working)
        assert logo.is_displayed(), "Google logo not found"

        print("Test Passed: Google.com is working!")

    except Exception as e:
        print(f"Test Failed: {str(e)}")

    finally:
        # Close the browser window
        driver.quit()

if __name__ == "__main__":
    test_google()
