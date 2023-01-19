from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time


class LinkedInBot:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get("https://www.linkedin.com/uas/login")
        time.sleep(2)
        email_input = self.driver.find_element(By.ID, "username")
        password_input = self.driver.find_element(By.ID, "password")
        email_input.send_keys(self.email)
        password_input.send_keys(self.password)
        password_input.send_keys(Keys.ENTER)
        time.sleep(10)

    def search_and_connect(self, search_term):
        self.driver.get("https://www.linkedin.com/search/results/people/")
        time.sleep(2)
        search_input = self.driver.find_element(
            By.XPATH, "//input[@placeholder='Search']")
        search_input.send_keys(search_term)
        search_input.send_keys(Keys.ENTER)
        time.sleep(5)
        next_button = self.driver.find_elements(By.TAG_NAME, 'div')
        # element = driver.find_element(By.XPATH, "//*[contains(@aria-label,'myLabel')]")
        # element = driver.find_element(By.CSS_SELECTOR, "[aria-label='myLabel']")

        for button in next_button:
            className = button.get_attribute('class')
            if className:
                print(className)
                break


        # while next_button:
        #     search_results = self.driver.find_elements(By.XPATH, "//div[contains(@class, 'entity-result')]")
        #     for result in search_results:
        #         try:
        #             # click on the connect button
        #             connect_button = result.find_element(
        #                 By.XPATH, ".//span[text()='Connect']")
        #             connect_button.click()
        #             recruiterName = result.find_element(
        #                 By.XPATH, "//span[@class='flex-1']//strong")
        #             print(recruiterName.text)
        #             try:
        #                 first_space_index = recruiterName.text.index(" ")
        #                 print(first_space_index)
        #             except:
        #                 first_space_index = len(recruiterName.text)
        #             recruiterName = recruiterName.text[:first_space_index]
        #             print(recruiterName)
        #             time.sleep(5)
        #             # add a note before connecting
        #             add_note_button = self.driver.find_element(
        #                 By.XPATH, "//span[text()='Add a note']")
        #             add_note_button.click()
        #             note_input = self.driver.find_element(
        #                 By.XPATH, "//textarea[@name='message']")
        #             note_input.send_keys(self.note(recruiterName))
        #             send_invitation_button = self.driver.find_element(
        #                 By.XPATH, "//span[text()='Send']")
        #             send_invitation_button.click()
        #             time.sleep(5)
        #         except Exception as e:
        #             print(e)
        #             continue
        #     try:
        #         print("try click")
        #         next_button.click()
        #         print("Clicked")
        #     except Exception as e:
        #         self.close()
            
    def close(self):
        self.driver.close()

    @classmethod
    def note(cls, recruiterName):
            return f"Hey {recruiterName}, \n Would love to connect with you and see if you have any junior position openings! I am a new Software Engineer and recently just completed a SE boot camp. I was in medical school for a year prior to transitioning into tech. Eager to learn anything and everything!"

print("hello")

bot = LinkedInBot("email@gmail.com", "password")
bot.login()
bot.search_and_connect("technical recruiter")
bot.close()
