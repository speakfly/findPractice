import sendEmail


message = '<html><body><a href="www.baidu.com">百度</a></body></html>'
mode = "html"
sendEmail.send_mail(message, mode)
