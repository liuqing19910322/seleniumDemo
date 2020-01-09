import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import random

class TestDefaultSuite():
    def setup_method(self, method):
        options = webdriver.ChromeOptions()
        options.debugger_address = '127.0.0.1:9000'
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

# testcase1：打开testerhome首页，然后搜索社团，点击第一个帖子
    def test_searchtest(self):
        self.driver.get("https://testerhome.com/")
        self.driver.find_element(By.CSS_SELECTOR, '#main-nav-menu > ul > li:nth-child(4) > a').click()
        self.driver.find_element(By.CSS_SELECTOR, '#hot_teams > div.panel-body > div > div:nth-child(1) > div > div.media-body > div.media-heading > a').click()
        self.driver.find_element(By.CSS_SELECTOR, '#main > div > div.col-md-8 > div > div.panel-body > div.topic.media.topic-21848 > div.infos.media-body > div.title.media-heading > a').click()

# testcase02: 企业微信自动添加成员，需要复用已经登录的chrome，需要debugger address
    def test_addpartner(self):
        url = 'https://work.weixin.qq.com/wework_admin/frame#contacts'
        self.driver.get(url)

        # 通过cookie登录
        cookies = {
            "wwrtx.vst": "bSwvqnvSpnN2uENJ8Xb3ZEqrkw7Omzx_VXiXWrmrWahdQvmhWMazZJ9iswGFXohewurgONuvcwW_Ur5FADGPVjykm584AlqytGZDvpszGXbroxdP4DBLUvEjTXoBjR8qEq_o0-7jBe9QQsDWinwXOFH9TdS7bSPTFJ7mbx6fig6bXcH_bHpSCRP9TMZLn4UrxovVC4wOUB8U2o1MqkziTCW0wCfiglffp-J-X9eRytNPvklOJGKsazC-vX31ASw4V7O0agkgNHR97RpU23eMJg",
            "wwrtx.d2st": "a140387",
            "wwrtx.sid": "fqanLJoh8Z1qSPy991xQyxZTzDyNs8AqNiokEOp_pITuBawZhzdpWB1XjnuVIdL5",
            "wwrtx.ltype": "1",
            "wxpay.corpid": "1970325002096061",
            "wxpay.vid": "1688852666103698",
        }
        for k, v in cookies.items():
            self.driver.add_cookie({"name": k, "value": v})
        self.driver.get(url)

        # 点击"添加联系人"
        self.driver.find_element(By.CSS_SELECTOR, 'div > div.member_colRight > div > div.js_party_info > div.js_has_member > div.js_operationBar_footer.ww_operationBar > a.qui_btn.ww_btn.js_add_member').click()

        # 点击姓名输入框
        self.driver.find_element(By.CSS_SELECTOR, '#username')

        # 输入姓名
        memberName = "测试"+ str(random.randint(1000,99999))
        self.driver.find_element(By.CSS_SELECTOR, '#username').send_keys(memberName)

        # 输入别名
        otherName = str(random.randint(10000000,99999999))
        self.driver.find_element(By.CSS_SELECTOR, '#memberAdd_acctid').send_keys(otherName)

        # 输入手机号
        mobile = str(random.randint(18000000000,18099999999))
        self.driver.find_element(By.XPATH, '//*[@id="memberAdd_phone"]').send_keys(mobile)

        # 滑动到页面底部
        js = "window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js)

        # 点击保存
        self.driver.find_element(By.CSS_SELECTOR, 'div > div.member_colRight > div > div:nth-child(4) > div > form > div:nth-child(3) > a.qui_btn.ww_btn.ww_btn_Blue.js_btn_continue').click()
