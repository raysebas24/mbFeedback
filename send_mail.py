import smtplib
from email.mime.text import MIMEText

def send_mail(customer, dealer, rating, vehicle,  comments):
    port = 587
    emailName = 'son.goku93288@gmail.com' # default DragonBall Mail Adress
    smtp_server = 'smtp.gmail.com'
    login = 'son.goku93288@gmail.com'
    password = 'ibqxjokvcufystfu'#'hrvy hhms ztxv jgqw' # default DragonBall Mail PassWD
    message = f"<h3>New Feedback Submission</h3>\
        <ul><li>Customer: {customer}</li>\
        <li>Dealer: {dealer}</li>\
        <li>Rating: {rating}</li>\
        <li>Vehicle Type: {vehicle}\
        <li>Comments: {comments}</li>\</ul>"

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
