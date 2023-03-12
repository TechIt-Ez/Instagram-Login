from selenium import webdriver
# If we want to use another browser, we must change the webdriver import
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
# We import our username and password
import config

# We can add as many options as we want
options = Options()
options.add_argument('start-maximized')

driver = webdriver.Chrome(options=options)
login_url = 'https://www.instagram.com/accounts/login/'

def connexion():
    driver.get(login_url)
    time.sleep(5)
    accept_cookies()
    time.sleep(5)

    # We search for the username input
    login = driver.find_element(By.NAME, 'username')
    login.send_keys(config.USERNAME)

    # We search for the username input
    password = driver.find_element(By.NAME, 'password')
    password.send_keys(config.PASSWORD)
    password.send_keys(Keys.ENTER)

    time.sleep(5)
    decline_notification()

    if driver.current_url == login:
        print("Impossible to connect")
        return False
    else:
        return True
    
def accept_cookies():
    if driver.find_elements(By.CSS_SELECTOR, "button[class='_a9-- _a9_1']") != []:
        cookies = driver.find_element(By.CSS_SELECTOR, "button[class='_a9-- _a9_1']")
        cookies.click()
    else:
        print('No cookies')

def decline_notification():
    if driver.find_elements(By.CSS_SELECTOR, "button[class='_a9-- _a9_1']") != []:
        notif = driver.find_element(By.CSS_SELECTOR, "button[class='_a9-- _a9_1']")
        notif.click()
    else:
        print('No notification')

if connexion():
    time.sleep(3)
    driver.quit()
else:
    print('Connexion error')