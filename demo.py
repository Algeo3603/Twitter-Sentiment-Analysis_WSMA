import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
# import requests

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
time.sleep(5)
search_field = driver.find_element(By.XPATH, "//input[@placeholder='Search']")
search_field.send_keys('#summer')
search_field.submit()
time.sleep(5)


# fetch url for bs4
# target_url = driver.current_url
# response = requests.get(target_url)
# while response.status_code != 200:
#     time.sleep(5)
#     response = requests.get(target_url)
# html_data = response.text
# soup = BeautifulSoup(html_data, 'html.parser')
# print(soup)



# time.sleep(5)
# # get html structure of tweets
# tweets = driver.find_elements(By.XPATH, "//article[@data-testid='tweet']")
# print(tweets)
# print(len(tweets))

# for _ in range(5):
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(5)

html_content = driver.page_source
soup = BeautifulSoup(html_content, "html.parser")
# print(soup)
articles = soup.find_all('article', {'data-testid':"tweet"})

tweet_text_content =[]
for article in articles:
    text_div = article.find('div', {'data-testid':'tweetText'})
    text = text_div.find('span', class_="css-1qaijid r-bcqeeo r-qvutc0 r-poiln3").get_text()
    # text = text.get_text(strip=True)
    tweet_text_content.append(text)

print(len(articles))
print(tweet_text_content)
# print(articles[0])

# tweet_text_content =[]
# for article in articles:
#     for div in article:
#         div_content = div.find('div', {'data-testid':'tweetText'})
#         for span in div_content:
#             text_span = span.find('span', class_='css-1qaijid r-bcqeeo r-qvutc0 r-poiln3')
#             # text = text_span.get_text(strip=True)
#             tweet_text_content.append(text_span)
# print(len(articles))
# print(tweet_text_content)
# # print(articles[0])


# for article in articles:
#     text_div = article.find('div', class_="css-175oi2r")
#     text = text_div.find('span', class_="css-1qaijid r-bcqeeo r-qvutc0 r-poiln3").get_text(strip=True)