from time import sleep
from selenium import webdriver
import random
import math
import string
overall_counter = 0

account_number = input("Which Account do you want to use? 1/2: ")
loops_number = input("How Many Comments do you want to do? ")
while int(loops_number) > overall_counter:
    counter = 0
    browser = webdriver.Firefox()
    browser.implicitly_wait(5)

    browser.get('https://www.instagram.com/')

    # login_link = browser.find_element_by_xpath("//a[text()='Log in']")
    # login_link.click()

    sleep(2)

    username_input = browser.find_element_by_css_selector("input[name='username']")
    password_input = browser.find_element_by_css_selector("input[name='password']")
    #Enter your own username and password
    if int(account_number) == 1:
        username_input.send_keys("Username1")
        password_input.send_keys("Password1")
    elif int(account_number) == 2:
        username_input.send_keys("Username2")
        password_input.send_keys("Password2")

    login_button = browser.find_element_by_xpath("//button[@type='submit']")
    login_button.click()
    sleep(5)

    if int(account_number) == int(account_number):
        notSave_button = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
        notSave_button.click()
    sleep(5)

    notNow_button = browser.find_element_by_css_selector("button.aOOlW:nth-child(2)")
    notNow_button.click()
    sleep(3)

    browser.execute_script("window.scrollTo(0, 1100)")
    sleep(5)    

    while counter <= random.randint(7,10):
        comment_button = browser.find_element_by_css_selector("article._8Rm4L:nth-child(1) > div:nth-child(4) > section:nth-child(5) > div:nth-child(1) > form:nth-child(1) > textarea:nth-child(1)")
        comment_button.click()
        sleep(random.randint(5,6))

        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(random.randint(4,6)))

        comment_choice = random.randint(1,4)

        comment_input = browser.find_element_by_css_selector(".focus-visible")
        if comment_choice == 1:
            comment_input.send_keys("Hello" + result_str)
        elif comment_choice == 2:
            comment_input.send_keys("Hi" + result_str)
        elif comment_choice == 3:
            comment_input.send_keys("Whats Up" + result_str + "Good post!")
        elif comment_choice == 4:
            comment_input.send_keys("I love what you did here" + result_str)

        sleep(random.randint(10,15))

        post_button = browser.find_element_by_xpath("//button[@type='submit']")
        post_button.click()
        sleep(random.randint(9,20))

        counter = counter + 1
        overall_counter = overall_counter + 1
        print("Counter = " + str(counter) + " Overall Counter = " + str(overall_counter))

    browser.close()

    print("Cycle Done")
    sleep(random.randint(190,300))
    #/html/body/div[1]/section/main/section/div[1]/div[3]/div/article[1]/div[3]/section[3]/div/form/textarea

# account_button = browser.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[1]/div/div/div[2]/div[1]/div/div/a")
# account_button.click()
# sleep(5)

# saved_button = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/a[3]/div")
# saved_button.click()
# sleep(500)

# bazelspost_button = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div[2]/article/div/div/div/div[1]/a")
# bazelspost_button.click())

