import config
import json
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
# import chromedriver_autoinstaller
# from pyvirtualdisplay import Display

today = datetime.today()
formatted_date = today.strftime("%m_%d_%Y")

# display = Display(visible=0, size=(800, 800))  
# display.start()

# chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
#                                       # and if it doesn't exist, download it automatically,
#                                       # then add chromedriver to path

chrome_options = webdriver.ChromeOptions()    
options = [
  # Define window size here
   "--window-size=1200,1200",
    "--ignore-certificate-errors",
 
    "--headless"
    #"--disable-gpu",
    #"--window-size=1920,1200",
    #"--ignore-certificate-errors",
    #"--disable-extensions",
    #"--no-sandbox",
    #"--disable-dev-shm-usage",
    #'--remote-debugging-port=9222'
]

for option in options:
    chrome_options.add_argument(option)

    
driver = webdriver.Chrome(options = chrome_options)

# login
driver.get("https://www.linkedin.com/login")
username = driver.find_element(By.XPATH, "//input[@name='session_key']")
password = driver.find_element(By.XPATH, "//input[@name='session_password']")

username.send_keys(config.username)
password.send_keys(config.password)
driver.save_screenshot('debug/nav.png')

login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()
driver.implicitly_wait(1)
driver.save_screenshot('debug/login.png')
# navigate
driver.get("https://www.linkedin.com/games/queens/")
driver.save_screenshot('debug/queens.png')
# with open("debug/{formatted_date}.html", "w", encoding='utf-8') as f:
#     f.write(driver.page_source)

# try:
#     start_game = driver.find_element(By.XPATH, "//span[text()='Start game']")
#     start_game.click()
# except Exception as e:
#     print(e)
#     print("start game failed, trying resume game")
#     resume_game = driver.find_element(By.XPATH, "//span[text()='Resume game']")
#     resume_game.click()
# finally:
#     print("man")

# # dimiss instructions
# try:
#     dismiss_button = driver.find_element(By.CSS_SELECTOR, "[aria-label='Dismiss']")
#     dismiss_button.click()
# except Exception as e:
#     print("no need to dismiss")

# # grab grid
# cells = driver.find_elements(By.CLASS_NAME, "queens-cell")
# colors = []
# for cell in cells:
#     class_attribute = cell.get_attribute('class')
#     # Extract the color from the class attribute
#     color = class_attribute.split('cell-color-')[1][0]
#     colors.append(int(color))
# print(colors)

# # quit selenium
# driver.quit()

# # save grid to txt
# file_path = f"grids/{formatted_date}.txt"

# with open(file_path, 'w') as filehandle:
#     json.dump(colors, filehandle)

# print(f"saved to {file_path}")