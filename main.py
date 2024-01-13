from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from configs.Configs import Config


class AutoSignIn:
    def __init__(self, driver, base_config):
        self.driver = driver
        self.base_url = base_config.base_url
        self.username = base_config.username
        self.password = base_config.password

        self.login_url = self.base_url + '/auth/login'
        self.login_value = ['ant-input-lg', 'verify-code', 'commonButton']

        self.signin_url = self.base_url + '/center/work/problem'
        self.signin_value = ['auth-header-sign', 'sign-footer']

        self.timeout = 20

    def login(self):
        # 调用 WebDriver 对象的 get 方法, 可以让浏览器打开指定的网址
        self.driver.get(self.login_url)
        # 等待页面元素加载完成
        WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located((By.CLASS_NAME, self.login_value[0])))
        # 获取全部输入框
        inputElements = self.driver.find_elements(by=By.CLASS_NAME, value=self.login_value[0])
        # 输入账号和密码
        inputElements[0].send_keys(self.username)
        inputElements[1].send_keys(self.password)

        # 获取页面中验证码的文本数据
        verifyElement = self.driver.find_element(by=By.CLASS_NAME, value=self.login_value[1])
        # 计算验证码的值
        expression = ""
        for item in verifyElement.text.replace('×', '*'):
            if item != '=':
                expression += item
            else:
                break
        inputElements[2].send_keys(str(eval(expression)))
        # 点击登录按钮
        buttonElement = WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located((By.CLASS_NAME, self.login_value[2])))
        sleep(2)
        buttonElement.click()

    def signIn(self):  #
        self.driver.get(self.signin_url)

        addElement = WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "global-nav-auth-btn")))
        ActionChains(driver).move_to_element(addElement).perform()

        iconElement = WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located((By.CLASS_NAME, self.signin_value[0])))
        iconElement.click()

        WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located((By.CLASS_NAME, self.signin_value[1])))

        signElements = self.driver.find_elements(by=By.CLASS_NAME, value=self.signin_value[1])

        for item in signElements:
            item.click()

        print(len(signElements))


if __name__ == '__main__':
    # 配置
    options = Options()
    options.add_argument("--headless")
    options.add_argument('--window-size=1920,1080')

    # 创建 WebDriver.Edge 对象
    driver = webdriver.Edge(service=Service(r'driver/msedgedriver'), options=options)

    autoSignIn = AutoSignIn(driver, Config())

    # 登录
    autoSignIn.login()
    sleep(2)

    # 签到
    autoSignIn.signIn()

