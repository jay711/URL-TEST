import time

date = time.strftime('%y-%m-%d', time.localtime())  # 获取当地时间
img1_path = r'C:/wen he/data/img/%s/direct/' % date + '1.png'
img2_path = r'C:/wen he/data/img/%s/dcs-proxy/' % date + '2.png'
print(img1_path,img2_path)