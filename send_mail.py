import smtplib
from email.mime.text import MIMEText

def send_mail(customer, dealer, rating, comments):
    port = 587
    smtp_server = 'smtp.gmail.com'
    login = 'son.goku93288@gmail.com'
    password = 'hrvy hhms ztxv jgqw'
    message = f"<h3>New Feedback Submission</h3><ul><li>Customer: {customer}</li><li>Dealer: {dealer}</li><li>Rating: {rating}</li><li>Comments: {comments}</li></ul>"

    sender_email = 'son.goku93288@gmail.com'
    receiver_email = 'son.goku93288@gmail.com'
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
