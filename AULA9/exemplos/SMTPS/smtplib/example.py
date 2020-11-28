import smtplib as smtp

email = "me@example.com"
password = "password"

server = smtp.SMTP_SSL('smtp.yandex.com')
server.set_debuglevel(1)
server.ehlo(email)
server.login(email, password)
server.auth_plain()
# server.get_and_print_your_inbox_magic_method()
server.quit()


