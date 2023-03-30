import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.keys import Keys


def get_driver(browser_name):
    if browser_name.lower() == "chrome":
        service = ChromeService(executable_path="/Webdrivers/Chromedriver/chromedriver.exe")
        return webdriver.Chrome(service=service)
    elif browser_name.lower() == "firefox":
        service = FirefoxService(executable_path="/Webdrivers/Edgedriver/msedgedriver.exe")
        return webdriver.Firefox(service=service)
    elif browser_name.lower() == "edge":
        service = EdgeService(executable_path="/Webdrivers/Firefoxdriver/geckodriver.exe")
        return webdriver.Edge(service=service)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")


# Function to scrape the title of a Wikipedia article
def scrape_wikipedia_article(url, browser_name="chrome"):
    # Set up the web driver for the specified browser
    driver = get_driver(browser_name)

    # Navigate to the specified URL
    driver.get(url)

    # Find the title element
    title_element = driver.find_element(By.ID, "firstHeading")

    # Extract the text from the title element
    title = title_element.text

    # Close the browser window
    driver.quit()

    return title


# Example usage
if __name__ == "__main__":
    wiki_url = "https://en.wikipedia.org/wiki/Web_scraping"

    # Choose your desired browser: "chrome", "firefox", or "edge"
    browser = "chrome"

    title = scrape_wikipedia_article(wiki_url, browser_name=browser)
    print(f"Title of the Wikipedia article: {title}")
