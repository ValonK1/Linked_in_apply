# I believe on of the ways we can set the time posted by inspecting the individual job not by going through the date posted tab as this way we can get earlier jobs
from selenium import webdriver
from selenium.webdriver.common.by import By
firefox_options = webdriver.FirefoxOptions()
#firefox_options.add_experimental_option("detach", True)

#<span dir="ltr" class="job-details-jobs-unified-top-card__job-insight-view-model-secondary">
#                                <!---->Entry level<!---->
#                              </span>

driver = webdriver.Firefox(options=firefox_options)
def brand_new_jobs():
    time_elements = driver.find_elements(By.CSS_SELECTOR, ".tvm__text.tvm__text--low-emphasis span")#example: get all the text associated with this
    recent_posts = []       # Extract the text for each element
    for element in time_elements:
        post_time = element.text
        recent_posts.append(post_time)

    # Print out the most recent posts
    print("Most Recent Job Posts:")
    for post in recent_posts:
        print(post)

    return recent_posts