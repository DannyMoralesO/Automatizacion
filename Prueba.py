import unittest, time, random
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class PruebaTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path= './drivers/chrome/chromedriver.exe')
        #cls.driver = webdriver.Firefox(executable_path= './drivers/firefox/geckodriver.exe')
        #cls.driver = webdriver.Firefox()
        cls.driver.get("http://automationpractice.com/index.php")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(15)
        time.sleep(5)

    # TestCase: Register
    def test_0001(self):
        time.sleep(3)
        driver = self.driver
        randomx = random.randint(3, 999)
        button = driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/nav/div[1]/a')
        button.click()
        mail = driver.find_element_by_xpath('//*[@id="email_create"]')
        mail.send_keys('prueba@prueba'+repr(randomx)+'.com.co')
        create_button = driver.find_element_by_xpath('//*[@id="SubmitCreate"]')
        create_button.click()
        check = driver.find_element_by_xpath('//*[@id="id_gender1"]').click()
        driver.execute_script("window.scrollTo(0, 400);")
        Firstname = driver.find_element_by_xpath('//*[@id="customer_firstname"]')
        Firstname.send_keys('First')
        Lastname = driver.find_element_by_xpath('//*[@id="customer_lastname"]')
        Lastname.send_keys('Last')
        password = driver.find_element_by_xpath('//*[@id="passwd"]')
        password.send_keys('12345678')
        driver.execute_script("window.scrollTo(0, 400);")
        daysSelect = Select(self.driver.find_element_by_xpath("//*[@id='days']"))
        daysSelect.select_by_index(1)
        monthSelect = Select(self.driver.find_element_by_xpath("//*[@id='months']"))
        monthSelect.select_by_index(2)
        yearSelect = Select(self.driver.find_element_by_xpath("//*[@id='years']"))
        yearSelect.select_by_index(3)
        check_2= driver.find_element_by_xpath('//*[@id="newsletter"]').click()
        check_3= driver.find_element_by_xpath('//*[@id="optin"]').click()
        driver.execute_script("window.scrollTo(0, 700);")
        Firstname2 = driver.find_element_by_xpath('//*[@id="firstname"]')
        Firstname2.send_keys('First')
        Lastname2 = driver.find_element_by_xpath('//*[@id="lastname"]')
        Lastname2.send_keys('Last')
        company = driver.find_element_by_xpath('//*[@id="company"]')
        company.send_keys('Last')
        address = driver.find_element_by_xpath('//*[@id="address1"]')
        address.send_keys('Adress')
        address2 = driver.find_element_by_xpath('//*[@id="address2"]')
        address2.send_keys('Adress')
        city = driver.find_element_by_xpath('//*[@id="city"]')
        city.send_keys('City')
        stateSelect = Select(self.driver.find_element_by_xpath("//*[@id='id_state']"))
        stateSelect.select_by_index(1)
        postal = driver.find_element_by_xpath('//*[@id="postcode"]')
        postal.send_keys('00000')
        countrySelect = Select(self.driver.find_element_by_xpath("//*[@id='id_country']"))
        countrySelect.select_by_index(1)
        other = driver.find_element_by_xpath('//*[@id="other"]')
        other.send_keys('Other Example')
        phone = driver.find_element_by_xpath('//*[@id="phone"]')
        phone.send_keys('2345678')
        phone_mobile = driver.find_element_by_xpath('//*[@id="phone_mobile"]')
        phone_mobile.send_keys('2345678')
        alias = driver.find_element_by_xpath('//*[@id="alias"]')
        alias.send_keys('sdfgh')
        buttonSubmit = driver.find_element_by_xpath('//*[@id="submitAccount"]').click()
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


    # TestCase: Add to car
    def test_0002(self):
        time.sleep(3)
        driver = self.driver
        wait = WebDriverWait(driver, 15)
        product_list = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div/div[1]/header/div[3]/div/div/div[6]/ul/li[2]/a')))
        product_list.click()
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, 700);")
        addtocar = driver.find_element_by_xpath('//*[@id="center_column"]/ul/li[1]/div/div[2]/div[2]/a[1]/span')
        addtocar.click()
        
