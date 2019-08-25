# coding = utf-8
from selenium import webdriver
import time
import pic_cmp
from proxy import openProxy
from excel import readExcel, writeExcel
import os
import shutil
from display import windows


def get_urls(urllist):
    '''
    因为从excel读出的url前面缺少'http://',这个函数用来加上协议头
    :param urllist: 从excel中读出的url列表
    :return: 加上'http://'协议头后的ul列表
    '''
    urls = [''] * len(urllist)
    for i in range(len(urllist)):
        urls[i] = 'http://' + urllist[i]
    return urls


def openBrower():
    '''
    打开直连的浏览器
    :return: 浏览器页面
    '''
    webdriver_handle = webdriver.Chrome()
    return webdriver_handle


def loadUrl(handle, url):
    '''
    打开网页
    :return: 输入url后的页面
    '''
    handle.get(url)
    # handle.maximize_window()


def direct_test(url, count):
    '''
    直连模式访问url
    :return:
    '''
    browser1 = openBrower()
    loadUrl(browser1, url)
    browser1.get_screenshot_as_file(img1_path+count+'1.png')
    time.sleep(2)
    browser1.quit()


def proxy_test(url, count):
    '''
    proxy模式下访问url
    :return:
    '''
    browser2 = openProxy()
    loadUrl(browser2, url)
    browser2.get_screenshot_as_file(img2_path+count+'2.png')
    time.sleep(2)
    browser2.quit()


def checkResult(similary, url):
    '''
    测试URL是否符合要求并返回结果
    :param similary: 两种模式下测试截图的相似度
    :param url: 测试的url
    :return: 三个结果中的一个,分别是'符合要求','不符合要求','发生异常'
    '''
    if similary == 1:
        print('图片相似度为%s,两种模式都能访问,%s不符合要求' % (similary, url))
        shutil.copyfile(img1_path + count + '1.png', img_error_path + count + '1.png') # 复制有问题的图片到error文件夹
        shutil.copyfile(img2_path + count + '2.png', img_error_path + count + '2.png')  # 复制有问题的图片到error文件夹
        return '不符合要求'
    elif similary < 0.8:
        print('图片相似度为%s,只有代理模式能访问,%s符合要求' % (similary, url))
        return '符合要求'
    else:
        print('图片相似度为%s,可能出现异常,%s不符合要求' % (similary, url))
        shutil.copyfile(img1_path + count + '1.png', img_error_path + count + '1.png')  # 复制有问题的图片到error文件夹
        shutil.copyfile(img2_path + count + '2.png', img_error_path + count + '2.png')  # 复制有问题的图片到error文件夹
        return '出现异常'


def url_test(photo1_path, photo2_path, url, count):
    '''
    单个url的测试
    :param photo1_path: 直连模式下截图的路径
    :param photo2_path: 代理模式下截图的路径
    :param url: 测试的url
    :param count: 用来区分不同的截图
    :return: 单个url测试的结果
    '''
    direct_test(url, count)
    proxy_test(url, count)
    similary = pic_cmp.phash_img_similarity(photo1_path, photo2_path)
    result = checkResult(similary, url)
    return result


def urls_test():
    '''
    多个url测试
    :return: 生成一个测试报告
    '''
    global count
    url_list = readExcel(excel_read_path)  # 从excel中读取URL表
    urls = get_urls(url_list)  # 给读出的列表元素加上'http://'协议头
    index = 0
    excel_output = []
    for url in urls:
        count = url_list[index]  # 改变截图保存的名称
        excel_output.append(url_test(img1_path + count + '1.png', img2_path + count + '2.png', url, count))
        index += 1
    writeExcel(excel_write_path, url_list, excel_output)


def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


if __name__ == '__main__':

    date = time.strftime('%y-%m-%d', time.localtime())  #获取当地时间
    img1_path = r'C:/data/img/%s/direct/' % date
    img2_path = r'C:/data/img/%s/dcs-proxy/' % date
    img_error_path = r'C:/data/img/%s/error/' % date
    create_folder(img1_path)
    create_folder(img2_path)
    create_folder(img_error_path)

    # excel_read_path = r'C:/wen he/hw_selenium1/txt/%s-block.xlsx' % date
    # excel_write_path = r'C:/wen he/hw_selenium1/txt/%s-result.xls' % date
    excel_read_path, excel_write_path = windows()

    urls_test()

