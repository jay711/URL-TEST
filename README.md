# URL-TEST
## 一、  项目背景

DDWI是一款安全软件产品，以代理的方式部署在用户电脑上，用户部署后发现一些bug，访问一些URL的时候会被禁止访问，为此，开发人员对于这些禁止访问的URL，暂时采取了一种方法，就是让其通过dcs-proxy代理来访问。同时，编写了一个程序用来专门爬取这些禁止DDWI访问的URL，URL-TEST工具就是用来测试这个程序是否正确执行的小工具。

 

## 二、  项目要求

总体来说，测试很简单，就是开发人员提供一个测试环境，在浏览器上部署了两种模式，一种是“Direct”模式，这种模式设置AWS为代理；一种是“dcs-proxy”模式，这种模式设置“dcs”为代理。开发人员开发的程序每天会生成一个URL的txt文档，测试txt文档里的URL在这两种模式下的访问情况，一般会有三种情况：

- “direct”模式下禁止访问，“dcs-proxy”模式下正常访问，此时URL符合要求；
- 两种模式下都能访问，此时URL不符合要求；
- 两种模式下都不能访问，或者其他的情况，都归于异常情况，并截图说明情况。

最终把所有URL的测试情况以Excel表的形式发给开发人员，并总结Excel表的内容，如“共测试URL：20，符合要求：16， 不符合要求：3，异常：1， 异常说明：两种模式都不能访问，正确率：16/20。”

 

## 三、手动测试

​      每天会从开发人员那里收到两份txt文档，我们主要测试“block.txt”的URL。

以[www.rivamiami.com](http://www.rivamiami.com)为例，在“direct”模式下访问如图1所示：

![1](E:\git_jay711\URL-TEST\img\1.png)

​                              图1  “direct”模式下访问情况

 

在“dcs-proxy”模式下访问情况如图2所示：（注意红色箭头所指按钮，通过点击该按钮来切换模式）

![2](E:\git_jay711\URL-TEST\img\2.png)

图2 “dcs-proxy”模式下访问情况

“direct”模式下禁止访问，“dcs-proxy”模式下正常访问，此时URL符合要求；接下来访问下一个URL，依次重复。

## 四、  自动测试

通过自己编写的小工具，来实现所有的测试步骤自动化，只要导入需要测试的excel表，便能自动生成测试结果的excel表，该工具如图3所示。

![3](E:\git_jay711\URL-TEST\img\3.png)

![3（1）](E:\git_jay711\URL-TEST\img\3（1）.png)

​                                  图3 URL-TEST工具

测试流程如下：

（1） 生成需要测试的Excel表，将txt导入到Excel文档中（记得一定要从第一栏开始导入！），如图4所示。

![4](E:\git_jay711\URL-TEST\img\4.png)

​                   图4 需要测试的Excel表（从第一栏开始导入）

（2） 打开URL-TEST，导入要测试的Excel表，并填写输出的文件路径以及文件名（文件名后缀须为“.xls”！）

![5](E:\git_jay711\URL-TEST\img\5.png)

![5（1）](E:\git_jay711\URL-TEST\img\5（1）.png)

​                                  图5  导入Excel表

（3） 开始测试，程序会自动执行对URL的测试，测试完成之后，会生成测试结果的Excel表，如图6所示。

![6](E:\git_jay711\URL-TEST\img\6.png)

​                          图6  生成的Excel测试报告

（4） 对测试文件进行检查并总结，所有URL的测试结果都会进行截图，保存在如下路径：

C:/data/img/%s/direct/ ，“Direct”模式下的测试截图；

C:/data/img/%s/dcs-proxy/，“dcs”模式下的测试截图；

C:/data/img/%s/error/ ，所有发生异常和不符合要求情况的截图。

（5） 发送结果给开发人员。

## 五、  工具生成过程中的技术总结

本次主要使用Python来编写脚本以及生成可执行文件，在编写过程中涉及的包以及技术如下：

-  **selenium**中的**webdriver**模块，主要实现对web浏览器的控制，实现自动访问URL。在Pycharm中要导入selenium包以及下载谷歌浏览器的driver驱动。
- 导入**functools**和**PIL**包，编写图片比较的算法，本次主要使用计算图片的哈希值来对图片的相似度进行比较，这还得提到webdriver里的**get_screenshot_as_file（）**函数了，将访问的结果截图保存在设定的路径下，取出图片进行比较，得到图片的相似度然后做后续的判断。
- 导入**xlrd**及**xlsxWriter**包，主要实现对Excel文档的处理。
- 导入**tkinter**包，来实现python的可视化编程，生成窗口，我们这里主要用到的是**filedialog**方法。同时还用到了time模块，os模块的部分函数。
- 安装pyinstall，将png文件转换为ico文件，将.py生成带图标的exe文件。