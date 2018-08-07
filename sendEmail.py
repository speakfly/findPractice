from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib


from_addr = "1090384046@qq.com"
password = ""
# to_addr = "1090384046@qq.com"
smtp_server = 'smtp.qq.com'
smtp_port = 25
# mode = 'plain'    # 'plain', 'html'
# message = 'hello, send by Python...'

def _format_addr(s):
    """格式化 发送接收的地址"""
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

def send_mail(to_addr, message, mode):

    msg = MIMEText(message, mode, 'utf-8')
    msg['From'] = _format_addr('ming <%s>' % from_addr)
    msg['To'] = _format_addr('用户 <%s>' % to_addr)
    msg['Subject'] = Header('提醒信息', 'utf-8').encode()

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()
