from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver

#this is gonna be the function to help answer questions when prompted. when we first get to the questions it will ask us to enter email, phome number, name this part is already filled in when you create a profile so we can skip
#then will ask us to upload a resume/ people who use linkedin already have resume on their profile


#so we can skip the contact info page and resume page and hit next
# only thing is to create answers for the rest of the questions
# best would be to answer as many questions as possible then save the application and comback later to fill it

firefox_options = webdriver.FirefoxOptions()
#chrome_options.add_experimental_option("detach", True)
driver = webdriver.Firefox(options=firefox_options)


# idea: have webdriver search "jobs-easy-apply-form-section__grouping" and store the position of the elements
# iterate through finding different elements by adding a constant factor to the vertical position for each iteration
# if no more elements are found, then all of the questions have been searched and now we handle their processing

