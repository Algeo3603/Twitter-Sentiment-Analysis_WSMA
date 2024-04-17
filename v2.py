import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


chrome_options = Options()
chrome_options.add_experimental_option("detach", True) # keeps the window open after execution
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://twitter.com/i/flow/login')


# enter username
time.sleep(5)
input_field = driver.find_element(By.CSS_SELECTOR, ".r-30o5oe.r-1dz5y72")
input_field.send_keys("Algeo_testing")
next_button = driver.find_element(By.XPATH, "//div[@role='button'][contains(.,'Next')]")
next_button.click()
time.sleep(3)


# enter password
password_field = driver.find_element(By.XPATH, "//input[@name='password']")
password_field.send_keys('Algeo-testing123')
login_button = driver.find_element(By.XPATH, "//div[@role='button'][contains(.,'Log in')]")
login_button.click()
time.sleep(5)


# enter hashtag
driver.maximize_window()
time.sleep(10)
search_field = driver.find_element(By.XPATH, "//input[@placeholder='Search']")
search_field.send_keys('#quotes')
search_field.submit()
time.sleep(5)


tweet_text_content =[]
# scroll the page to load more tweets
for _ in range(5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)

    # fetch html source code
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, "html.parser")

    # bs4 magic
    articles = soup.find_all('article', {'data-testid':"tweet"})
    for article in articles:
        text_div = article.find('div', {'data-testid':'tweetText'})
        text = text_div.find('span', class_="css-1qaijid r-bcqeeo r-qvutc0 r-poiln3").get_text()
        tweet_text_content.append(text)


# print(len(articles))
print(tweet_text_content)
print(len(tweet_text_content))
