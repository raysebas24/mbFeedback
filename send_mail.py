import smtplib
from email.mime.text import MIMEText

def send_mail(customer, dealer, rating, comments):
    port = 587
    emailName = '???' # default DragonBall Mail Adress
    smtp_server = 'smtp.gmail.com'
    login = emailName
    password = '???' # default DragonBall Mail PassWD
    message = f"<h3>New Feedback Submission</h3><ul><li>Customer: {customer}</li><li>Dealer: {dealer}</li><li>Rating: {rating}</li><li>Comments: {comments}</li></ul>"

    sender_email = emailName
    receiver_email = emailName
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Mercedes Feedback'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
