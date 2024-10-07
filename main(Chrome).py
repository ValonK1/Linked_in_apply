import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from Questions import *
from Date_posted import *
#notes) change constant to variabl after done
# LinkedIn credentials and job search parameters constant test
ACCOUNT_NAME = ("Big Moe")
ACCOUNT_EMAIL = ('big.moe.moe.moe.moe.moe@gmail.com')
ACCOUNT_PASSWORD = ('moe12345678')
#JOB_SEARCH = input("Enter your desired job title: ")
JOB_SEARCH = ("Software Developer ")

LOCATION = "Hartford County, Connecticut, United States" 

PHONE_NUMBER =  "860-301-1111 "

# Initialize WebDriver with Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# Function to wait and locate elements
def wait_and_find(by, value, timeout=5, click=False, send_keys=None, clear=False, enter=False):
    try:
        element = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))
        if clear:
            element.clear()
        if enter:
            element.send_keys(Keys.ENTER) == True
        if click:
            element.click() == True
        if send_keys:
            element.send_keys(send_keys)
        return element
    except Exception as e:
        print(f"Error locating element by {by}='{value}': {e}")
        return None




#def entry_level(by, value, timeout=5, click=False):
#    # Get all job listings (adjust selector if needed)
#        try:
#            # Check if the entry level span is present
#            entry_level_element = job.find_element(By.CSS_SELECTOR, ".//span[contains(@class, 'job-details-jobs-unified-top-card__job-insight-view-model-secondary') and contains(text(), 'entry level')]",10)
#            
#            if entry_level_element:
#                # If the entry level text is found, click the apply button
#                time.sleep(5)  # Wait for any loading or animations
#                apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button")
#                apply_button.click()
#                print("Applied to entry-level job.")
#                return  # Exit after applying to one job
#        except Exception as e:
#           print(f"Error processing job: {e}")
#            continue  # Move to the next job listing

# Make sure to call the function after setting up the driver
# apply_to_entry_level_jobs(driver)
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
    search_input = WebDriverWait(driver, 10).until(
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

# select all location and set to desired location
wait_and_find(By.XPATH, "//input[@aria-label='City, state, or zip code' and @type='text']", click=True, clear=True, send_keys=LOCATION, enter=True)

# function to apply for entry level jobs
#job_listings = driver.find_elements(By.CSS_SELECTOR, '.display-flex.job-card-container.relative.job-card-list')  # Adjust as needed

#entry_level(By.CSS_SELECTOR, '.display-flex.job-card-container.relative.job-card-listjob-card-container--clickable')
# click on the job
time.sleep(5)
apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
apply_button.click()

#solve questions 1) skip contact page and resume page
wait_and_find(By.XPATH, "//button[@aria-label='Continue to next step']", click=True)
wait_and_find(By.XPATH, "//button[@aria-label='Continue to next step']", click=True, timeout=10)