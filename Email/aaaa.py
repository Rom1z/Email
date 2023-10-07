import smtplib
from email.mime.text import MIMEText
#Их внешнего файла импортируем наш логин и пароль
from login_password import login, password

def send_email(message, subject, recipient):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    try:
        server.login(login, password)
        msg = MIMEText(message)
        msg["Subject"] = subject
        server.sendmail(login, recipient, msg.as_string())
    except:
        print("Ошибка не удалось отправить письмо")

if __name__ == "__main__":
    message = input("Введите текст сообщения\n>>>")
    subject = input("Введите тему сообщения\n>>>")
    recipients = input("Введите получателей сообщения через запятую\n>>>").split(",")
    for recipient in recipients:
        send_email(message, subject, recipient)