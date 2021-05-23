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

    # TestCase: Login
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
        




    # TestCase: Navigate to Create parameter
    def est_0002(self):
        time.sleep(5)
        driver = self.driver
        wait = WebDriverWait(driver, 15)
        parameters = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/app-root/app-pages/div/div/div[1]/app-bar-nav/ul/li/div/div/app-menu/ul/li[5]/div[1]/button')))
        parameters.click()
        parameter = wait.until(EC.element_to_be_clickable((By.XPATH,'//a[contains(text(),"Parametro de cuota")]')))
        parameter.click()
        time.sleep(3)
        

    #TestCase: Create Parameter
    def est_0003(self):
        driver = self.driver
        create_parameter = driver.find_element_by_xpath("/html/body/app-root/app-pages/div/div/div[2]/div[2]/div/app-dues-parameter-list/div[1]/div/button")
        create_parameter.click()
        time.sleep(3)
        #create = driver.find_element_by_xpath("/html/body/app-root/app-pages/div/div/div[2]/div[2]/div/app-dues-parameter/button").click()
        driver.find_element_by_id("name").send_keys("   TEST Automatico JSVS")
        driver.find_element_by_xpath("/html/body/app-root/app-pages/div/div/div[2]/div[2]/div/app-dues-parameter/app-general-values/div/div/div[2]/div[1]/input").send_keys("#484646")
        driver.find_element_by_xpath("/html/body/app-root/app-pages/div/div/div[2]/div[2]/div/app-dues-parameter/app-general-values/div/div/div[2]/div[2]/input").send_keys("JSQA")
        parameterType = Select(self.driver.find_element_by_xpath("/html/body/app-root/app-pages/div/div/div[2]/div[2]/div/app-dues-parameter/app-general-values/div/div/div[2]/div[3]/select"))
        parameterType.select_by_index(1)
        parameterType.select_by_index(2)
        parameterType.select_by_index(3)
        parameterType.select_by_index(0)
        applicationType1 = driver.find_element_by_xpath("/html/body/app-root/app-pages/div/div/div[2]/div[2]/div/app-dues-parameter/app-general-values/div/div/div[3]/div/div[1]/label/input")
        applicationType1.click()
        applicationType2 = driver.find_element_by_xpath("/html/body/app-root/app-pages/div/div/div[2]/div[2]/div/app-dues-parameter/app-general-values/div/div/div[3]/div/div[2]/label/input")
        applicationType2.click()
        applicationType3 = driver.find_element_by_xpath("/html/body/app-root/app-pages/div/div/div[2]/div[2]/div/app-dues-parameter/app-general-values/div/div/div[3]/div/div[3]/label/input")
        applicationType3.click()
        ValueType_2 = driver.find_element_by_xpath("//*[@id='2']")
        ValueType_2.click()
        ValueType_1 = driver.find_element_by_xpath("//*[@id='1']")
        ValueType_1.click()
        ivaType_2 = driver.find_element_by_xpath('//*[@id="2" and @name="ivaType"]').click()
        ivaType_1 = driver.find_element_by_xpath('//*[@id="1" and @name="ivaType"]').click()
        ivaType_3 = driver.find_element_by_xpath('//*[@id="3" and @name="ivaType"]').click()
        fixedValue_2 = driver.find_element_by_xpath("/html/body/app-root/app-pages/div/div/div[2]/div[2]/div/app-dues-parameter/app-general-values/div/div/div[7]/div/div[2]/label/input").click()
        fixedValue_1 = driver.find_element_by_xpath("/html/body/app-root/app-pages/div/div/div[2]/div[2]/div/app-dues-parameter/app-general-values/div/div/div[7]/div/div[1]/label/input").click()
        optradioMora_1 = driver.find_element_by_xpath("/html/body/app-root/app-pages/div/div/div[2]/div[2]/div/app-dues-parameter/app-general-values/div/div/div[8]/div/div[2]/div[1]/div/label/input").click()
        optradioMora_2 = driver.find_element_by_xpath("/html/body/app-root/app-pages/div/div/div[2]/div[2]/div/app-dues-parameter/app-general-values/div/div/div[8]/div/div[1]/div/div/label/input").click()
        driver.find_element_by_xpath('/html/body/app-root/app-pages/div/div/div[2]/div[2]/div/app-dues-parameter/app-general-values/div/div/div[5]/div/input').send_keys('(X + Y / Z)')
        checkTerceros = driver.find_element_by_xpath("/html/body/app-root/app-pages/div/div/div[2]/div[2]/div/app-dues-parameter/app-general-values/div/div/div[9]/div/div[1]/label/input").click()
        checkExclusiva = driver.find_element_by_xpath("/html/body/app-root/app-pages/div/div/div[2]/div[2]/div/app-dues-parameter/app-general-values/div/div/div[9]/div/div[2]/label/input").click()
        #checkVisible = driver.find_element_by_xpath("/html/body/app-root/app-pages/div/div/div[2]/div[2]/div/app-dues-parameter/app-general-values/div/div/div[9]/div/div[3]/label/input").click()
        driver.find_element_by_xpath("/html/body/app-root/app-pages/div/div/div[2]/div[2]/div/app-dues-parameter/app-general-values/div/div/div[10]/div/textarea").send_keys("Cuañtos caracteres recibe este campo 1234567890°!''$%&/()=?¡*¨[_:;,-.}{+\")")
        ahorradorFactu = driver.find_element_by_xpath("/html/body/app-root/app-pages/div/div/div[2]/div[2]/div/app-dues-parameter/div[1]/app-billing-states/div/div/div/div/table/tbody/tr[1]/td[2]/input").click()
        ahorradorPostFactu = driver.find_element_by_xpath("/html/body/app-root/app-pages/div/div/div[2]/div[2]/div/app-dues-parameter/div[1]/app-billing-states/div/div/div/div/table/tbody/tr[1]/td[3]/input").click()
        adjudiFactu = driver.find_element_by_xpath("/html/body/app-root/app-pages/div/div/div[2]/div[2]/div/app-dues-parameter/div[1]/app-billing-states/div/div/div/div/table/tbody/tr[2]/td[2]/input").click()
        adjudiPostFactu = driver.find_element_by_xpath("/html/body/app-root/app-pages/div/div/div[2]/div[2]/div/app-dues-parameter/div[1]/app-billing-states/div/div/div/div/table/tbody/tr[2]/td[3]/input").click()
        ganadoresFactu = driver.find_element_by_xpath("/html/body/app-root/app-pages/div/div/div[2]/div[2]/div/app-dues-parameter/div[1]/app-billing-states/div/div/div/div/table/tbody/tr[3]/td[2]/input").click()
        ganadoPostresFactu = driver.find_element_by_xpath("/html/body/app-root/app-pages/div/div/div[2]/div[2]/div/app-dues-parameter/div[1]/app-billing-states/div/div/div/div/table/tbody/tr[3]/td[3]/input").click()
        driver.find_element_by_xpath("/html/body/app-root/app-pages/div/div/div[2]/div[2]/div/app-dues-parameter/div[2]/app-accounts-register/div[1]/label").click()
        #cancelarAccion = driver.find_element_by_xpath("/html/body/app-root/app-pages/div/div/div[2]/div[2]/div/app-dues-parameter/a").click()
        vigentesActivos = driver.find_element_by_name("vigentes-activos")
        vigentesActivos.clear()
        vigentesActivos.send_keys("0000000000-00000")
        vigentesDesistentes = driver.find_element_by_name("vigentes-desistentes")
        vigentesDesistentes.clear()
        vigentesDesistentes.send_keys("0000000000-00000")
        terminadosActivos = driver.find_element_by_name("terminados-activos")
        terminadosActivos.clear()
        terminadosActivos.send_keys("0000000000-00000")
        terminadosDesistentes = driver.find_element_by_name("terminados-desistentes")
        terminadosDesistentes.clear()
        terminadosDesistentes.send_keys("0000000000-00000")
        ivaActivos = driver.find_element_by_name("iva-activos")
        ivaActivos.clear()
        ivaActivos.send_keys("0000000000-00000")
        driver.find_element_by_id("nav-ganadores-tab").click()
        vigentesFacturacion = driver.find_element_by_name("vigentes-facturacion")
        vigentesFacturacion.clear()
        vigentesFacturacion.send_keys("0000000000-00000")
        vigentesRecaudacion = driver.find_element_by_name("vigentes-recaudacion")
        vigentesRecaudacion.clear()
        vigentesRecaudacion.send_keys("0000000000-00000")
        vigentesEntregados = driver.find_element_by_name("vigentes-entregados")
        vigentesEntregados.clear()
        vigentesEntregados.send_keys("0000000000-00000")
        terminadosFacturacion = driver.find_element_by_name("terminados-facturacion")
        terminadosFacturacion.clear()
        terminadosFacturacion.send_keys("0000000000-00000")
        terminadosRecaudacion = driver.find_element_by_name("terminados-recaudacion")
        terminadosRecaudacion.clear()
        terminadosRecaudacion.send_keys("0000000000-00000")
        terminadosEntregados = driver.find_element_by_name("terminados-entregados")
        terminadosEntregados.clear()
        terminadosEntregados.send_keys("0000000000-00000")
        ivaFacturacion = driver.find_element_by_name("iva-facturacion")
        ivaFacturacion.clear()
        ivaFacturacion.send_keys("0000000000-00000")
        ivaRecaudacion = driver.find_element_by_name("iva-recaudacion")
        ivaRecaudacion.clear()
        ivaRecaudacion.send_keys("0000000000-00000")
        create = driver.find_element_by_xpath("/html/body/app-root/app-pages/div/div/div[2]/div[2]/div/app-dues-parameter/button").click()

    # TestCase: Edit parameter
    def est_0004(self):
        driver = self.driver
        time.sleep(2)
        #aumentar 1 numero el TR en el PATH para tomar el parametro creado del caso anterior.
        Edit = driver.find_element_by_xpath("/html/body/app-root/app-pages/div/div/div[2]/div[2]/div/app-dues-parameter-list/div[2]/div/table/tbody/tr[10]/td[5]/a").click()
        time.sleep(2)
        driver.find_element_by_id("name").send_keys("   TEST Automatico JSVS Actualizacion")
        driver.find_element_by_xpath("/html/body/app-root/app-pages/div/div/div[2]/div[2]/div/app-dues-parameter/app-general-values/div/div/div[2]/div[1]/input").send_keys("#cf1b1b")
        driver.find_element_by_xpath("/html/body/app-root/app-pages/div/div/div[2]/div[2]/div/app-dues-parameter/app-general-values/div/div/div[2]/div[2]/input").send_keys("JSVQA")
        parameterType = Select(self.driver.find_element_by_xpath("/html/body/app-root/app-pages/div/div/div[2]/div[2]/div/app-dues-parameter/app-general-values/div/div/div[2]/div[3]/select"))
        parameterType.select_by_index(0)
        parameterType.select_by_index(1)
        parameterType.select_by_index(2)
        parameterType.select_by_index(3)
        #cuotaBruta = driver.find_element_by_xpath("//*[@id='grossQuota']").click()
        #cuotaBruta = driver.find_element_by_xpath("//*[@id='grossQuota']").click()
        applicationType2 = driver.find_element_by_xpath("/html/body/app-root/app-pages/div/div/div[2]/div[2]/div/app-dues-parameter/app-general-values/div/div/div[3]/div/div[2]/label/input")
        applicationType2.click()
        applicationType1 = driver.find_element_by_xpath("/html/body/app-root/app-pages/div/div/div[2]/div[2]/div/app-dues-parameter/app-general-values/div/div/div[3]/div/div[1]/label/input")
        applicationType1.click()
        applicationType3 = driver.find_element_by_xpath("/html/body/app-root/app-pages/div/div/div[2]/div[2]/div/app-dues-parameter/app-general-values/div/div/div[3]/div/div[3]/label/input")
        applicationType3.click()
        ValueType_2 = driver.find_element_by_xpath("//*[@id='2']")
        ValueType_2.click()
        ValueType_1 = driver.find_element_by_xpath("//*[@id='1']")
        ValueType_1.click()
        ivaType_3 = driver.find_element_by_xpath('//*[@id="3" and @name="ivaType"]').click()
        ivaType_2 = driver.find_element_by_xpath('//*[@id="2" and @name="ivaType"]').click()
        ivaType_1 = driver.find_element_by_xpath('//*[@id="1" and @name="ivaType"]').click()        
        fixedValue_1 = driver.find_element_by_xpath("/html/body/app-root/app-pages/div/div/div[2]/div[2]/div/app-dues-parameter/app-general-values/div/div/div[7]/div/div[1]/label/input").click()
        fixedValue_2 = driver.find_element_by_xpath("/html/body/app-root/app-pages/div/div/div[2]/div[2]/div/app-dues-parameter/app-general-values/div/div/div[7]/div/div[2]/label/input").click()
        driver.find_element_by_xpath("/html/body/app-root/app-pages/div/div/div[2]/div[2]/div/app-dues-parameter/app-general-values/div/div/div[7]/div/div[3]/div/input").send_keys("2000000")
        optradioMora_2 = driver.find_element_by_xpath("/html/body/app-root/app-pages/div/div/div[2]/div[2]/div/app-dues-parameter/app-general-values/div/div/div[8]/div/div[1]/div/div/label/input").click()
        optradioMora_1 = driver.find_element_by_xpath("/html/body/app-root/app-pages/div/div/div[2]/div[2]/div/app-dues-parameter/app-general-values/div/div/div[8]/div/div[2]/div[1]/div/label/input").click()
        driver.find_element_by_name("overdueInitialDay").send_keys("5")
        driver.find_element_by_name("overdueFinalDay").send_keys("20")
        #driver.find_element_by_xpath('/html/body/app-root/app-pages/div/div/div[2]/div[2]/div/app-dues-parameter/app-general-values/div/div/div[5]/div/input').send_keys('(X + Y / Z)')
        checkTerceros = driver.find_element_by_xpath("/html/body/app-root/app-pages/div/div/div[2]/div[2]/div/app-dues-parameter/app-general-values/div/div/div[9]/div/div[1]/label/input").click()
        checkExclusiva = driver.find_element_by_xpath("/html/body/app-root/app-pages/div/div/div[2]/div[2]/div/app-dues-parameter/app-general-values/div/div/div[9]/div/div[2]/label/input").click()
        checkVisible = driver.find_element_by_xpath("/html/body/app-root/app-pages/div/div/div[2]/div[2]/div/app-dues-parameter/app-general-values/div/div/div[9]/div/div[3]/label/input").click()
        driver.find_element_by_xpath("/html/body/app-root/app-pages/div/div/div[2]/div[2]/div/app-dues-parameter/app-general-values/div/div/div[10]/div/textarea").send_keys("Cuañtos caracteres recibe este campo 1234567890°!''$%&/()=?¡*¨[_:;,-.}{+\")   actualizacióóóóóóóóóóóóón")
        ahorradorPostFactu = driver.find_element_by_xpath("/html/body/app-root/app-pages/div/div/div[2]/div[2]/div/app-dues-parameter/div[1]/app-billing-states/div/div/div/div/table/tbody/tr[1]/td[3]/input").click()
        ahorradorFactu = driver.find_element_by_xpath("/html/body/app-root/app-pages/div/div/div[2]/div[2]/div/app-dues-parameter/div[1]/app-billing-states/div/div/div/div/table/tbody/tr[1]/td[2]/input").click()
        adjudiPostFactu = driver.find_element_by_xpath("/html/body/app-root/app-pages/div/div/div[2]/div[2]/div/app-dues-parameter/div[1]/app-billing-states/div/div/div/div/table/tbody/tr[2]/td[3]/input").click()
        adjudiFactu = driver.find_element_by_xpath("/html/body/app-root/app-pages/div/div/div[2]/div[2]/div/app-dues-parameter/div[1]/app-billing-states/div/div/div/div/table/tbody/tr[2]/td[2]/input").click()
        ganadoPostresFactu = driver.find_element_by_xpath("/html/body/app-root/app-pages/div/div/div[2]/div[2]/div/app-dues-parameter/div[1]/app-billing-states/div/div/div/div/table/tbody/tr[3]/td[3]/input").click()
        ganadoresFactu = driver.find_element_by_xpath("/html/body/app-root/app-pages/div/div/div[2]/div[2]/div/app-dues-parameter/div[1]/app-billing-states/div/div/div/div/table/tbody/tr[3]/td[2]/input").click()
        driver.find_element_by_xpath("/html/body/app-root/app-pages/div/div/div[2]/div[2]/div/app-dues-parameter/div[2]/app-accounts-register/div[1]/label").click()
        vigentesActivos = driver.find_element_by_name("vigentes-activos")
        vigentesActivos.clear()
        vigentesActivos.send_keys("0123456789-12369")
        vigentesDesistentes = driver.find_element_by_name("vigentes-desistentes")
        vigentesDesistentes.clear()
        vigentesDesistentes.send_keys("0123456789-12369")
        terminadosActivos = driver.find_element_by_name("terminados-activos")
        terminadosActivos.clear()
        terminadosActivos.send_keys("0123456789-12369")
        terminadosDesistentes = driver.find_element_by_name("terminados-desistentes")
        terminadosDesistentes.clear()
        terminadosDesistentes.send_keys("0123456789-12369")
        ivaActivos = driver.find_element_by_name("iva-activos")
        ivaActivos.clear()
        ivaActivos.send_keys("0123456789-12369")
        driver.find_element_by_id("nav-ganadores-tab").click()
        vigentesFacturacion = driver.find_element_by_name("vigentes-facturacion")
        vigentesFacturacion.clear()
        vigentesFacturacion.send_keys("0123456789-12369")
        vigentesRecaudacion = driver.find_element_by_name("vigentes-recaudacion")
        vigentesRecaudacion.clear()
        vigentesRecaudacion.send_keys("0123456789-12369")
        vigentesEntregados = driver.find_element_by_name("vigentes-entregados")
        vigentesEntregados.clear()
        vigentesEntregados.send_keys("0123456789-12369")
        terminadosFacturacion = driver.find_element_by_name("terminados-facturacion")
        terminadosFacturacion.clear()
        terminadosFacturacion.send_keys("0123456789-12369")
        terminadosRecaudacion = driver.find_element_by_name("terminados-recaudacion")
        terminadosRecaudacion.clear()
        terminadosRecaudacion.send_keys("0123456789-12369")
        terminadosEntregados = driver.find_element_by_name("terminados-entregados")
        terminadosEntregados.clear()
        terminadosEntregados.send_keys("0123456789-12369")
        ivaFacturacion = driver.find_element_by_name("iva-facturacion")
        ivaFacturacion.clear()
        ivaFacturacion.send_keys("0123456789-12369")
        ivaRecaudacion = driver.find_element_by_name("iva-recaudacion")
        ivaRecaudacion.clear()
        ivaRecaudacion.send_keys("0123456789-12369")
        editParameter = driver.find_element_by_xpath("/html/body/app-root/app-pages/div/div/div[2]/div[2]/div/app-dues-parameter/button").click()
        #cancelarAccion = driver.find_element_by_xpath("/html/body/app-root/app-pages/div/div/div[2]/div[2]/div/app-dues-parameter/a").click()
        time.sleep(3)

    # TestCase: Navigate to Settings / Create system parameter
    def est_0005(self):
        time.sleep(3)
        driver = self.driver
        wait = WebDriverWait(driver, 15)
        setting = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/app-root/app-pages/div/div/div[1]/app-bar-nav/ul/li/div/div/app-menu/ul/li[2]/div[1]/button')))
        setting.click()
        parameterSystem = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="submenu505"]')))
        parameterSystem.click()
        time.sleep(3)

    # TestCase: Create editable system parameter
    def est_0006(self):
        time.sleep(3)
        driver = self.driver
        create_parameter = driver.find_element_by_xpath("/html/body/app-root/app-pages/div/div/div[2]/div[2]/div/parameter-config-list/div[1]/div/button")
        create_parameter.click()
        time.sleep(3)
        code = driver.find_element_by_id("code").send_keys("TestAutoOne")
        name = driver.find_element_by_id("name").send_keys("Test Automático editable ñ")
        value = driver.find_element_by_id("value").send_keys("20")
        save = driver.find_element_by_xpath("/html/body/app-root/app-pages/div/div/div[2]/div[2]/div/parameter-config-form/div/div/form/button").click()
        time.sleep(2)

    # TestCase: Edit system parameter
    def est_0007(self):
        time.sleep(3)
        driver = self.driver
        #aumentar 1 numero el TR en el PATH para tomar el parametro creado del caso anterior.        
        Edit = driver.find_element_by_xpath("/html/body/app-root/app-pages/div/div/div[2]/div[2]/div/parameter-config-list/div[2]/div/table/tbody/tr[4]/td[5]/a").click()
        time.sleep(3)
        code = driver.find_element_by_id("code")
        code.clear()
        code.send_keys("TestAutoOneModified")
        name = driver.find_element_by_id("name")
        name.clear()
        name.send_keys("Test Automático editable ñ modified")
        value = driver.find_element_by_id("value")
        value.clear()
        value.send_keys("18.6")
        save = driver.find_element_by_xpath("/html/body/app-root/app-pages/div/div/div[2]/div[2]/div/parameter-config-form/div/div/form/button").click()
        time.sleep(2)

    # TestCase: Create non-editable system parameter
    def est_0008(self):
        time.sleep(3)
        driver = self.driver
        create_parameter = driver.find_element_by_xpath("/html/body/app-root/app-pages/div/div/div[2]/div[2]/div/parameter-config-list/div[1]/div/button")
        create_parameter.click()
        time.sleep(3)
        code = driver.find_element_by_id("code").send_keys("TestAutoTwo")
        name = driver.find_element_by_id("name").send_keys("Test Automático no-editable ñ")
        value = driver.find_element_by_id("value").send_keys("25")
        modified = driver.find_element_by_xpath("/html/body/app-root/app-pages/div/div/div[2]/div[2]/div/parameter-config-form/div/div/form/div[2]/div[2]/div/label").click()
        save = driver.find_element_by_xpath("/html/body/app-root/app-pages/div/div/div[2]/div[2]/div/parameter-config-form/div/div/form/button").click()
        time.sleep(2)

    # TestCase: Edit non-editable system parameter
    def est_0009(self):
        time.sleep(3)
        driver = self.driver
        #aumentar 1 numero el TR en el PATH para tomar el parametro creado del caso anterior.
        Edit = driver.find_element_by_xpath("/html/body/app-root/app-pages/div/div/div[2]/div[2]/div/parameter-config-list/div[2]/div/table/tbody/tr[5]/td[5]/a").click()
        time.sleep(3)
        code = driver.find_element_by_id("code")
        code.clear()
        code.send_keys("TestAutoOneModifiedTwo")
        name = driver.find_element_by_id("name")
        name.clear()
        name.send_keys("Test Automático No-editable ñ modified")
        value = driver.find_element_by_id("value")
        value.clear()
        value.send_keys("19.1a")
        save = driver.find_element_by_xpath("/html/body/app-root/app-pages/div/div/div[2]/div[2]/div/parameter-config-form/div/div/form/button").click()
        time.sleep(2)

    # TestCase: Navigate to Cuotas / Cuota profile
    def test_0010(self):
        time.sleep(3)
        driver = self.driver
        wait = WebDriverWait(driver, 15)
        cuotas = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/app-root/app-pages/div/div/div[1]/app-bar-nav/ul/li/div/div/app-menu/ul/li[3]/div[1]/button')))
        cuotas.click()
        cuotaProfile= wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="submenu501"]')))
        cuotaProfile.click()
        time.sleep(3)

    # TestCase: Create Cuota Profile
    def test_0011(self):
        time.sleep(2)
        driver = self.driver
        driver.find_element_by_xpath("/html/body/app-root/app-pages/div/div/div[2]/div[2]/div/app-dues-profiles-list/div[2]/div/table/tbody/tr[1]/td[3]/a").click()
        time.sleep(4)
        driver.find_element_by_xpath("/html/body/ngb-modal-window/div/div/div[3]/div/button").click()
        time.sleep(2)
        createProfile = driver.find_element_by_xpath("/html/body/app-root/app-pages/div/div/div[2]/div[2]/div/app-dues-profiles-list/div[1]/div/button").click()
        time.sleep(3)
        name = driver.find_element_by_xpath("/html/body/app-root/app-pages/div/div/div[2]/div[2]/div/app-dues-profiles/div[2]/div[1]/app-general-values-dues-profiles/div/div/form/div[1]/div/input").send_keys("TestAutomático ñ")
        date = driver.find_element_by_name("dp").send_keys("2021-12-31")
        term = Select(self.driver.find_element_by_xpath("/html/body/app-root/app-pages/div/div/div[2]/div[2]/div/app-dues-profiles/div[2]/div[1]/app-general-values-dues-profiles/div/div/form/div[2]/div[2]/select"))
        term.select_by_index(1)
        term.select_by_index(2)
        term.select_by_index(3)
        term.select_by_index(4)
        term.select_by_index(0)
        observ = driver.find_element_by_xpath("/html/body/app-root/app-pages/div/div/div[2]/div[2]/div/app-dues-profiles/div[2]/div[1]/app-general-values-dues-profiles/div/div/form/div[3]/div/textarea").send_keys("$%&1234567890.,-_:;][*¨¨¨¨''''&/()(0') ññ pruebas automatizadas")
        visible = driver.find_element_by_xpath("/html/body/app-root/app-pages/div/div/div[2]/div[2]/div/app-dues-profiles/div[2]/div[1]/app-general-values-dues-profiles/div/div/form/div[4]/div[2]/label").click()
        browse = driver.find_element_by_id("exampleFormControlFile1").send_keys('/home/sistemas/Downloads/Disponibilidad 2021.pdf')
        time.sleep(2)
        deleteFile = driver.find_element_by_xpath("/html/body/app-root/app-pages/div/div/div[2]/div[2]/div/app-dues-profiles/div[2]/div[1]/app-general-values-dues-profiles/div/div/form/div[5]/div/div/div/span[3]").click()
        time.sleep(2)
        browse = driver.find_element_by_id("exampleFormControlFile1").send_keys('/home/sistemas/Downloads/Disponibilidad 2021.pdf')
        driver.find_element_by_id("1").click()
        driver.find_element_by_id("3").click()
        driver.find_element_by_id("5").click()
        associateParameters = driver.find_element_by_xpath("/html/body/app-root/app-pages/div/div/div[2]/div[2]/div/app-dues-profiles/div[2]/div[3]/button").click()
        time.sleep(3)
        addDelete = driver.find_element_by_xpath("/html/body/app-root/app-pages/div/div/div[2]/div[2]/div/app-dues-profiles/div[2]/div[2]/button").click()
        time.sleep(2)
        driver.find_element_by_id("4").click()
        time.sleep(1)
        descartar = driver.find_element_by_xpath("/html/body/div/div[2]/div/mat-dialog-container/app-dialog-associated-parameters/mat-dialog-actions/div[1]/button").click()
        time.sleep(2)
        addDelete = driver.find_element_by_xpath("/html/body/app-root/app-pages/div/div/div[2]/div[2]/div/app-dues-profiles/div[2]/div[2]/button").click()
        time.sleep(2)
        saveChances = driver.find_element_by_xpath("/html/body/div/div[2]/div/mat-dialog-container/app-dialog-associated-parameters/mat-dialog-actions/div[3]/button").click()
        time.sleep(2)









    # TestCase: Navigate to Bank Payments / Calculator
    def est_0015(self):
        time.sleep(3)
        driver = self.driver
        wait = WebDriverWait(driver, 15)
        bankPayments = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/app-root/app-pages/div/div/div[1]/app-bar-nav/ul/li/div/div/app-menu/ul/li[4]/div[1]/button')))
        bankPayments.click()
        calculator = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="submenu503"]')))
        calculator.click()
        time.sleep(3)
    
    # TestCase: Navigate to Bank Payments / Banking Transactions
    def est_0020(self):
        time.sleep(3)
        driver = self.driver
        wait = WebDriverWait(driver, 15)
        bankPayment = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/app-root/app-pages/div/div/div[1]/app-bar-nav/ul/li/div/div/app-menu/ul/li[4]/div[1]/button')))
        bankPayment.click()
        bankingTransactions = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="submenu504"]')))
        bankingTransactions.click()
        time.sleep(3)

    # TestCase: Navigate to Subscribers / Subscriber Search
    def est_0025(self):
        time.sleep(3)
        driver = self.driver
        wait = WebDriverWait(driver, 15)
        subscribers = wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/app-root/app-pages/div/div/div[1]/app-bar-nav/ul/li/div/div/app-menu/ul/li[6]/div[1]/button')))
        subscribers.click()
        subscriberSearch = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="submenu502"]')))
        subscriberSearch.click()
        time.sleep(3)

     # TestCase: Close browser
    def est_0012(self):
        time.sleep(5)
        self.driver.quit()

#if __name__ == '__main__':
  #  unittest.main()



