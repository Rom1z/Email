
#Импортируем необходимые библиотеки
import smtplib
import os
from email.mime.text import MIMEText
#Их внешнего файла импортируем наш логин и пароль
from login_password import login, password