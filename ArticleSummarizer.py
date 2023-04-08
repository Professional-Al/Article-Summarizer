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


def search_wikipedia(driver, article_name):
    search_url = "https://en.wikipedia.org/wiki/Special:Search"
    driver.get(search_url)
    search_box = driver.find_element(By.ID, "searchInput")
    search_box.send_keys(article_name)
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)  # Wait for search results to load
    first_result = driver.find_element(By.CSS_SELECTOR, ".mw-search-result-heading a")
    first_result.click()
    time.sleep(2)  # Wait for the article to load


def scrape_wikipedia_article(article_name, browser_name="firefox"):
    # Set up the web driver for the specified browser
    driver = get_driver(browser_name)

    # Try to navigate directly to the specified article
    article_url = f"https://en.wikipedia.org/wiki/{article_name.replace(' ', '_')}"
    driver.get(article_url)

    # Check if the "no article" message is displayed
    no_article_msg = "Wikipedia does not have an article with this exact name."
    try:
        error_message_element = driver.find_element(By.ID, "mw-content-text")
        if no_article_msg in error_message_element.text:
            search_wikipedia(driver, article_name)
            print("Direct match not found. Using top search result instead.")
    except Exception:
        pass

    # Find the title element
    title_element = driver.find_element(By.ID, "firstHeading")

    # Extract the text from the title element
    title = title_element.text

    # Close the browser window
    driver.quit()

    return title


if __name__ == "__main__":
    article_name = input("Enter the name of the Wikipedia article: ")

    # Choose your desired browser: "chrome", "firefox", or "edge"
    browser = "chrome"

    title = scrape_wikipedia_article(article_name, browser_name=browser)
    print(f"Title of the Wikipedia article: {title}")
