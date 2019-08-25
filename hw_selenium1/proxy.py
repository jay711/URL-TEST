from selenium import webdriver


def openProxy():
    '''
    打开设置dsc代理模式的浏览器
    :return:浏览器页面
    '''
    chromeOptions = webdriver.ChromeOptions()

    # 设置代理
    chromeOptions.add_argument("--proxy-server=http://ics-stg-proxy.sdi.trendmicro.com:3333")
    # 一定要注意，=两边不能有空格，不能是这样--proxy-server = http://202.20.16.82:10152
    webdriver_handle = webdriver.Chrome(chrome_options=chromeOptions)
    return webdriver_handle


# if __name__ == '__main__':
#    browser = openProxy()
#    browser.get('http://fujita-kazuhide.jp')