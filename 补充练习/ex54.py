#coding:utf-8

# boss 直聘爬虫
# 导入requests
import requests
from lxml import etree
import io

# 翻页
# for page in range(10):

# 网址
url = 'https://www.zhipin.com/job_detail/?query=%E7%AE%A1%E7%90%86%E5%92%A8%E8%AF%A2&scity=101270100&industry=&position='

# 反爬
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
    
# requests.get 请求数据
r = requests.get(url, headers = header)

# 网页初始化
html = etree.HTML(r.text)
# Xpath text()选择文本
names = html.xpath('//h3[@class="name"]//text()')

# 保存文件
f = io.open('dates.txt', 'a',encoding='utf-8')

for dat in names:
    f.write(dat+'\n')

f.write()

f.close()

print names
# 输出结果
'''
print r
print r.text
'''