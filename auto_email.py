# -*- coding:utf-8 -*-
import unittest, HTMLTestRunner, os, time, datatime
import smtplib
from email.mine.text import MIMEText
from email.header import Header

def sentmail(file_new):
    mail_from = '1053372550@qq.com'
    mail_to = '113067169@qq.com'
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    msg = MIMEText(mail_body, _subtype = 'html', _charset = 'utf-8')
    msg['Subject'] = u'测试报告'
    msg['data'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')
    smtp = smtplib.SMTP()
    smtp.connect('smtp.qq.com')
    smtp.login('1053372550@qq.com', 'lanlan315')
    smtp.sendmail(mail_from, mail_to, msg.as_string())
    smtp.quit()
    print 'email has send out!'

def sendreport():
    result_dir = 'D:\\selenium_python\\report'
    lists = os.listdir(result_dir)
    lists.sort(key = lambda fn:os.path.getmtime(result_dir + '\\' +fn) if not os.path.isdir(result_dir + '\\' + fn) else 0)
    print (u'最新测试生成的报告：' + lists[-1])
    file_new = os.path.join(result_dir, lists[-1])
    print file_new
    sentmail(file_new)

if __name__ == '__main__':
    runner.run(alltestnames)
    sendreport()
