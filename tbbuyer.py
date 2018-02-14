import os
from selenium import webdriver
import datetime
import time
from selenium.webdriver.common.action_chains import ActionChains
chromedriver = "/Users/luozepeng/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)

def login():
    driver.get("https://login.taobao.com/member/login.jhtml?from=taobaoindex&f=top&style=&sub=true&redirect_url=https%3A%2F%2Fi.taobao.com%2Fmy_taobao.htm%3Fspm%3Da21bo.2017.1997525045.1.472068c2SyCupd")
    # # if driver.find_element_by_link_text("亲，请登录"):
    # #     driver.find_element_by_link_text("亲，请登录").click();
    # time.sleep(5)
    # if driver.find_element_by_link_text("密码登录"):
    #     driver.find_element_by_link_text("密码登录").click();
    # time.sleep(5)
    # if driver.find_element_by_name("TPL_username"):
    #     driver.find_element_by_id("TPL_username_1").clear()
    #     driver.find_element_by_name("TPL_username").send_keys(uname);
    # time.sleep(5)
    # if driver.find_element_by_name("TPL_password"):
    #     driver.find_element_by_id("TPL_password_1").clear()
    #     driver.find_element_by_name("TPL_password").send_keys(pwd);
    # time.sleep(5)
    # source=driver.find_element_by_xpath("//*[@id='nc_1_n1z']")  

    # #定义鼠标拖放动作
    # ActionChains(driver).drag_and_drop_by_offset(source,400,0).perform()
    # #等待JS认证运行,如果不等待容易报错
    # time.sleep(5)
    # if driver.find_element_by_id("J_SubmitStatic"):
    #     driver.find_element_by_id("J_SubmitStatic").click();

    time.sleep(3)

    flag=True
    while flag==True:
        for i in range(60):            # 循环60次，从0至59
            if i >= 59 :               # 当i大于等于59时，打印提示时间超时
                print("timeout")    
                break
            try:                       # try代码块中出现找不到特定元素的异常会执行except中的代码
                if driver.find_element_by_id("mc-menu-hd"): # 如果能查找到特定的元素id就提前退出循环
                    driver.find_element_by_id("mc-menu-hd").click()
                    time.sleep(5)
                if driver.find_element_by_id("J_SelectAll1"):
                    driver.find_element_by_id("J_SelectAll1").click()
                time.sleep(3)
                if driver.find_element_by_link_text("结 算"):
                    driver.find_element_by_link_text("结 算").click();
                now = datetime.datetime.now()
                print('login success:', now.strftime('%Y-%m-%d %H:%M:%S'))
                flag=False
                break
            except:                    # 上面try代码块中出现异常，except中的代码会执行打印提示会继续尝试查找特定的元素id
                print("wait for find element")
            time.sleep(1)
        

def buy_on_time(buytime):
    while True:
        now = datetime.datetime.now()
        print(now)
        if now.strftime('%Y-%m-%d %H:%M:%S') == buytime:
            while True:
                try:
                    driver.find_element_by_link_text('提交订单').click()
                except:
                    time.sleep(0.1)
        time.sleep(0.01)
login()
buy_on_time('2018-02-04 11:14:08')