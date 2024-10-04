import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
#notes) change constant to variabl after done
# LinkedIn credentials and job search parameters constant test
ACCOUNT_EMAIL = ('big.moe.moe.moe.moe.moe@gmail.com')
ACCOUNT_PASSWORD = ('moe12345678')
#JOB_SEARCH = input("Enter your desired job title: ")
JOB_SEARCH = ("Software Developer ")

LOCATION = "Hartford , CT" 

PHONE_NUMBER =  "860-301-1111 "

# Initialize WebDriver with Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# Function to wait and locate elements
def wait_and_find(by, value, timeout=5, click=False, send_keys=None):
    try:
        element = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))
        if click:
            element.click() == True
        if send_keys:
            element.send_keys(send_keys)
        return element
    except Exception as e:
        print(f"Error locating element by {by}='{value}': {e}")
        return None

#def clickable_and_click()



# Open LinkedIn login page and login
driver.get("https://www.linkedin.com/login")
wait_and_find(By.CSS_SELECTOR, 'button[action-type="DENY"]', timeout=4, click=True)
wait_and_find(By.ID, "username", send_keys=ACCOUNT_EMAIL)
wait_and_find(By.ID, "password", send_keys=ACCOUNT_PASSWORD)
wait_and_find(By.XPATH, "//button[@type='submit']", click=True)

# Pause for manual Captcha resolution
input("Press Enter once you've completed the CAPTCHA...")

# Search for desired job
# acces search field put in desired field and hit send in this enter

try:# Wait until the search input is present and clickable
    search_input = WebDriverWait(driver, 4).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@aria-label='Search' and @type='text']"))
    )
    # Try to click the search input
    search_input.click()
    # Optionally, you can send keys to the input
    search_input.send_keys(JOB_SEARCH)
    # Hit Enter to search
    search_input.send_keys(Keys.ENTER)
except:
    print("The search input was not found or not clickable.")
try:# to go to jobs section
    jobs_field = WebDriverWait(driver, 4).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'search-reusables__filter-pill-button') and @aria-pressed='false']"))
    )
    # Try to click the search input
    jobs_field.click()
except:
    print("The Job button was not found or not clickable.")

# select easy apply filter
wait_and_find(By.XPATH, "//button[@aria-label='Easy Apply filter.']", click=True)


# decided to ignore below dated posted filters to make it more simply

# go to the Date posted filter open it and pick past week
#try:
#    wait_and_find(By.XPATH, "//button[@aria-label='Date posted filter. Clicking this button displays all Date posted filter options.']", click=True)
#   past_week_radio = WebDriverWait(driver, 5).until(
#        EC.element_to_be_clickable((By.XPATH, "//label[@for='timePostedRange-r604800']"))
#    )
        # Try to click the "Past week" radio button
#    past_week_radio.click()
    # Try to click the button for date posted with past week filter

#    wait_and_find(By.XPATH, "//button[@id='ember1414' and class = rtdeco-button__text']", click=True)
    #element_1 = 
#    wait_and_find(By.XPATH, "//button[@id='ember1121' and class = artdeco-button artdeco-button--2 artdeco-button--primary ember-view ml2']", click=True)
#    wait_and_find(By.XPATH, "//button[@id='ember1183' and class = artdeco-button artdeco-button--2 artdeco-button--primary ember-view ml2']", click=True)#    print("The 'Past week' radio button was not found or not clickable.")




