from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

#upto 100 new users can be followed per day due to quora's policy.....

email = str(input("Enter your Email\n"))
password = str(input("Please Enter your password\n"))


name_of_user = str(input("Enter name of user whose following you would like to duplicte into yours\n"))
index_in_quora_search = int(input("Enter index of user in quora search\n"))

#initializes driver for further interactions with web browser....
driver = webdriver.Chrome('/home/gauhar/Desktop/Documents/selenium/chromedriver')

#opens quora.com in web browser with get request....
driver.get('https://www.quora.com/')

#maximizes browser window...
driver.maximize_window()

user_name = driver.find_elements_by_class_name('header_login_text_box')
user_name[0].click()
user_name[0].send_keys(email)
user_name[1].click()
user_name[1].send_keys(password)
login = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div[2]/div/div/div/form/div[2]/div[3]/input')

#sleep time can be adjusted everywhere according to speed of internet connection.....
time.sleep(4)

login.click()
time.sleep(4)
search = driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div[2]/div[2]/div[1]/div[1]/div[1]/input')
search.click()
search.send_keys(name_of_user)
time.sleep(4)
user = driver.find_element_by_xpath('/html/body/div[4]/div[1]/div/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[2]/div[2]/ul/li['+str(index_in_quora_search+1)+']')
time.sleep(3)
user.click()
time.sleep(2)
following = driver.find_element_by_xpath('/html/body/div[3]/div[5]/div/div/div[2]/div[1]/div[2]/div/div/ul/div[7]/div/li/a')
time.sleep(2)
following.click()
time.sleep(2)


#scroll_pause_time can be adjusted according to speed of internet connection
SCROLL_PAUSE_TIME = 3.5

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

#list of all users in the following of target user......
following_of_user = driver.find_elements_by_class_name('PagedListItem')

following_of_user.reverse()
#Follows all those users which are not in your following list....

for user in following_of_user:
 #move to header of user card
 try:
    header = user.find_element_by_class_name('ObjectCard-header')
    time.sleep(2)
    action = ActionChains(driver)
    action.move_to_element(header)
    time.sleep(3)
    action.perform()
    time.sleep(3)
    element = user.find_element_by_class_name('ui_button_label')
    time.sleep(2)
#check if user is already followed or not
    if element.get_attribute('innerHTML') != "Following":
        time.sleep(3)
        icon_button = user.find_element_by_class_name('ui_button_icon_wrapper')
        time.sleep(3)
#follow those users which are yet to be followed......
        icon_button.click()
 except:
     continue
