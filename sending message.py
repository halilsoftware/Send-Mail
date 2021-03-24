from smtplib import SMTP
import  app
try
    subject = Test
    message =bu bir test mesajıdır
    content = subject {0}nn{1}.format(subject,message)

    myMailAdress ='example mail'
    password='examplepassoword'

    sendTo= 'example@gmail.com'

    mail = SMTP(smtp.gmail.com,587)

    mail.ehlo()
    mail.starttls()
    mail.login(myMailAdress,password)

    mail.sendmail(myMailAdress,sendTo,content.encode(utf-8))
    print(mail gönderme işlemi başarılı)
except Exception as ex
    print(hata oluştun {0}.format(ex))