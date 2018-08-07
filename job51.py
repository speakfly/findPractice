import requests
import urllib.parse
from pyquery import PyQuery as pq
import time
import re
import sendEmail

# 根据 地点 职位 薪资 查询内容
# conditions = ['广州', '实习 java', 3000]
class Job:

    def __init__(self, sql_tuple):
        self.num, self.email, self.title, self.addr, self.salary = sql_tuple

        # 构造url
        base_url = 'https://search.51job.com/list/030000,000000,0000,00,9,99,'
        str_conditions = " ".join([self.addr, self.title])
        param = urllib.parse.quote(str_conditions) + ',2,1.html/?ord_field=1'
        self.url = base_url + param

    # 获取主页
    def get_one_page(self, url):
        html = requests.get(url)
        html.encoding = 'GBK'
        return html

    # 解析
    def parse_one_page(self, html):
        doc = pq(html.text)
        items = doc('.dw_wp .el').items()
        for item in items:
            position = item('.t1 span a').attr['title']
            comp = item('.t2 a').attr['title']
            addr = item('.t3').text()
            salary = item('.t4').text()
            plu_date = item('.t5').text()
            pos_url = item('.t1 span a').attr['href']
            if position != None and not self.isEqualToday(plu_date):
                return;
            if position != None and self.addr in addr and self.isRange(salary):
                pos_item = {}
                pos_item['postion'] = position
                pos_item['comp'] = comp
                pos_item['addr'] = addr
                pos_item['salary'] = salary
                pos_item['plu_date'] = plu_date
                pos_item['pos_url'] = pos_url
                yield pos_item

        # 解析下一页
        url = re.search('<li class="bk">.*?<a.*?href="(.*?)"', html.text, re.S).group(1)
        html = self.get_one_page(url)
        self.parse_one_page(html)


# 调度 并发送邮件
    def main(self):
        html = self.get_one_page(self.url)
        message = '<table border="1" cellpadding="10"><tr><td>职位</td><td>公司</td><td>地点</td><td>薪资</td></tr>'
        for item in self.parse_one_page(html):
            message1 = ('<tr><td><a href="%s">%s</a></td><td>%s</td><td>%s</td><td>%s</td></tr>'%
            (item['pos_url'], item['postion'], item['comp'], item['addr'], item['salary']))
            message = message + message1
        message = message + '</table>'
        sendEmail.send_mail(self.email, message, "html")

    def isEqualToday(self, strDate):
        return time.strftime("%m-%d") == strDate

    def isRange(self, strRange):
        """
        2-4千/月
        120元/天
        一个常识 通常实习价格3000左右 如果超过4500的公司大多数是培训公司 这里把他们过滤掉
        """
        MAX = self.salary
        if "千" in strRange:
            expr1 = "(.*?)-(.*?)千"
            num1 = re.search(expr1, strRange)
            if float(num1.group(2)) <= (MAX + 1500)/1000:
                return True
        elif "元" in strRange:
            expr2 = "(.*?)元"
            num2 = re.search(expr2, strRange)
            if int(num2.group(1)) * 30 <= MAX + 1500:
                return True
        return False

if __name__ == "__main__":
    sql_tuple = (1, '1090384046@qq.com', '实习 java', '广州', 3000)
    job1 = Job(sql_tuple)
    job1.main()


# 类就如同一个小型的数据库 能很方便的提供接口， 并能在一定的范围内对数据进行操作
