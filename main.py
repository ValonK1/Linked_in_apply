import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# LinkedIn credentials and job search parameters
ACCOUNT_EMAIL = print(input("Enter your LinkedIn account email: "))
ACCOUNT_PASSWORD = print(input("Enter your LinkedIn account password: "))
JOB_SEARCH = print(input("Enter your desired job title: "))
LOCATION = print(input("Enter your desired Location : "))
PHONE_NUMBER =  print(input("Enter your phone number with dashes(example: 123-456-7890) "))

# Initialize WebDriver with Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# Function to wait and locate elements
def wait_and_find(by, value, timeout=10, click=False, send_keys=None):
    try:
        element = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))
        if click:
            element.click()
        if send_keys:
            element.send_keys(send_keys)
        return element
    except Exception as e:
        print(f"Error locating element by {by}='{value}': {e}")
        return None



# Open LinkedIn login page and login
driver.get("https://www.linkedin.com/login")
wait_and_find(By.CSS_SELECTOR, 'button[action-type="DENY"]', timeout=4, click=True)
wait_and_find(By.ID, "username", send_keys=ACCOUNT_EMAIL)
wait_and_find(By.ID, "password", send_keys=ACCOUNT_PASSWORD)
wait_and_find(By.XPATH, "//button[@type='submit']", click=True)

# Pause for manual Captcha resolution
input("Press Enter once you've completed the CAPTCHA...")

# Search for jobs
search_input = wait_and_find(By.XPATH, "//input[@type='text' and @placeholder='Search']")
if search_input:
    search_input.send_keys(JOB_SEARCH, Keys.ENTER)

# Apply location filter if necessary
# Ensure job search results are loaded first
first_job = wait_and_find(By.CLASS_NAME, 'reusable-search__result-container', click=True)

# Set location filter (optional, adjust as needed)
# Activate "Easy Apply" filter
wait_and_find(By.XPATH, "//button[@aria-label='Easy Apply filter.']", click=True)

wait_and_find(By.XPATH, "//button[@aria-label='Date posted filter. Clicking this button displays all Date posted filter options.']", click=True)


