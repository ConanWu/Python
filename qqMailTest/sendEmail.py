import os
import smtplib
import unittest
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from HTMLTestRunner import HTMLTestRunner

# smtpserver = 'smtp.qq.com'
# user = '457907449@qq.com'
# password = 'ohlqrzezvtmicadd'
# sender = '457907449@qq.com'
# receiver = '457907449@qq.com'
# subject = 'Python send email test'
# # sendfile = open('E:\\moving\GIT\\Python\\qqMailTest\\test_project\\report\\2017_08_27 11_26_44result.html', 'rb').read()
# result_dir = 'E:\\moving\GIT\\Python\\qqMailTest\\test_project\\report'
#
# lists = os.listdir(result_dir)      #获取该目录下的所有文件和文件夹
#
# lists.sort(key=lambda fn: os.path.getmtime(result_dir+"\\"+fn))
# print(('最新的文件是: ' + lists[-1]))
# file = os.path.join(result_dir, lists[-1])
#
#
# msg = MIMEText('<html><h1>hello!</h1></html>', 'html', 'utf-8')
# msg['subject'] = Header(subject, 'utf-8')
# att = MIMEText(file, 'base64', 'utf-8')
# att['Content-Type'] = 'application/octet-stream'
# att['Content-Disposition'] = 'attachment; filename="2017_08_27 11_26_44result.html"'
#
# msgRoot = MIMEMultipart('related')
# msgRoot['Subject'] = subject
# msgRoot.attach(att)


def send_email(file_new):
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()

    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['subject'] = Header("自动化测试报告", 'utf-8')
    sendfile = open(file_new, 'rb').read()

    # sendfile = open('E:\\moving\GIT\\Python\\qqMailTest\\test_project\\report\\2017-09-06_01_28_22result.html', 'rb').read()
    att = MIMEText(sendfile, 'base64', 'utf-8')
    att['Content-Type'] = 'application/octet-stream'
    att['Content-Disposition'] = 'attachment; filename="123.html"'

    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = 'this is subject'
    msgRoot.attach(att)

    smtp = smtplib.SMTP_SSL("smtp.qq.com", 465)
    # smtp.connect("smtp.qq.com")
    smtp.login("457907449@qq.com", "ohlqrzezvtmicadd")

    # smtp.sendmail("457907449@qq.com", "457907449@qq.com", msg.as_string())
    smtp.sendmail("457907449@qq.com", "457907449@qq.com", msgRoot.as_string())
    smtp.quit()
    print('email has send out !')

# 查找测试报告目录 找到最新生成的测试报告文件
def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport + "\\" + fn))
    file_new = os.path.join(testreport, lists[-1])
    print(file_new)
    return file_new

if __name__ == '__main__':
    test_dir = 'E:\\moving\\GIT\Python\\qqMailTest\\test_project\\test_case'
    test_report = 'E:\\moving\GIT\\Python\\qqMailTest\\test_project\\report'

    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')
    now = time.strftime("%Y-%m-%d_%H_%M_%S")
    filename = test_report + '\\' + now + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title= '测试报告', description='用例执行情况：')
    runner.run(discover)
    fp.close()

    new_report = new_report(test_report)
    send_email(new_report)  # 发送测试报告
# try:
#     smtp = smtplib.SMTP_SSL("smtp.qq.com", 465)
#     smtp.login(user, password)
#     # smtp.sendmail(sender, receiver, msg.as_string())
#     smtp.sendmail(sender, receiver, msgRoot.as_string())
#     smtp.quit()
#     print("successful!")
# except smtplib.SMTPException:
#     print(smtplib.SMTPException)
