import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(sender_email, sender_password, receiver_email, subject, message):
    # Создание объекта MIMEMultipart
    email = MIMEMultipart()

    # Установка параметров письма
    email["From"] = sender_email
    email["To"] = receiver_email
    email["Subject"] = subject

    # Добавление текста письма
    email.attach(MIMEText(message, "plain"))

    # Создание SMTP-соединения
    smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
    smtp_server.starttls()
    smtp_server.login(sender_email, sender_password)

    # Отправка письма
    smtp_server.send_message(email)
    smtp_server.quit()


# Пример использования
sender_email = "your_email@gmail.com"
sender_password = "your_password"
receiver_email = "recipient@example.com"
subject = "Тема письма"
message = "Текст письма"

send_email(sender_email, sender_password, receiver_email, subject, message)