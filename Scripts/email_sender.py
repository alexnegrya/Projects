def send_email(sender, recipients, subject, sender_name, html_file_path=None, html=None):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    # Data verification
    if type(sender) != str:
        raise TypeError('parameter sender must be str type')
    if type(recipients) not in (list, str):
        raise TypeError('recipients must be in the list or in string if recipient is only one')
    if type(subject) != str:
        raise TypeError('subject must be in str type')
    if type(sender_name) != str:
        raise TypeError('sender name nust be in str type')
    if html_file_path == None and html == None:
        raise ValueError('you must specify one of html file path or html as a string')
    elif html_file_path != None and html != None:
        raise ValueError('you only ane argument: html file name or html')
    if html_file_path != None and type(html_file_path) != str:
        raise TypeError('html file path name must be a str')
    if html != None and type(html) != str:
        raise TypeError('html must be in the str type')

    # Config
    server = 'smtp.mail.ru'
    password = 'rYZwqKKw8OBlXJFt2oGB'

    # Getting message text from html file
    if html_file_path != None:
        with open(html_file_path, 'r') as file:
            html_text = file.read()

    # Creating message body
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = f'{sender_name} <{sender}>'
    msg['To'] = recipients[0]
    msg['Reply-To'] = sender
    msg['Return-Path'] = sender

    # Part text
    if html_file_path != None:
        part_html = MIMEText(html_text, 'html')
    elif html != None:
        part_html = MIMEText(html, 'html')

    # Attach
    msg.attach(part_html)

    # Send message with SMTP
    mail = smtplib.SMTP_SSL(server)
    mail.login(sender, password)
    mail.sendmail(sender, recipients, msg.as_string())
    mail.quit()


print('This module for view only')
