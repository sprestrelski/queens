import config
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('log-level=2')
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(options=options)

# login
driver.get("https://www.linkedin.com/login")
username = driver.find_element(By.XPATH, "//input[@name='session_key']")
password = driver.find_element(By.XPATH, "//input[@name='session_password']")

username.send_keys(config.username)
password.send_keys(config.password)

login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()
driver.implicitly_wait(1)

# navigate
driver.get("https://www.linkedin.com/games/queens/")
try:
    start_game = driver.find_element(By.XPATH, "//span[text()='Start game']")
    start_game.click()
except Exception as e:
    print("start game failed, trying resume game")
    resume_game = driver.find_element(By.XPATH, "//span[text()='Resume game']")
    resume_game.click()

# dimiss instructions
try:
    dismiss_button = driver.find_element(By.CSS_SELECTOR, "[aria-label='Dismiss']")
    dismiss_button.click()
except Exception as e:
    print("no need to dismiss")

# grab grid
cells = driver.find_elements(By.CLASS_NAME, "queens-cell")
colors = []
for cell in cells:
    class_attribute = cell.get_attribute('class')
    # Extract the color from the class attribute
    color = class_attribute.split('cell-color-')[1][0]
    colors.append(int(color))
print(colors)

# quit selenium
driver.quit()

# save grid to txt
today = datetime.today()
formatted_date = today.strftime("%m_%d_%Y")
file_path = f"grids/{formatted_date}.txt"

with open(file_path, 'w') as filehandle:
    json.dump(colors, filehandle)

print(f"saved to {file_path}")