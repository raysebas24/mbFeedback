# https://www.youtube.com/watch?v=w25ea_I89iM
# Minute: 38

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy    # need for DB
from send_mail import send_mail


app = Flask(__name__)    # points to the root directory


ENV = 'dev'
#ENV = 'prod'# With an HEROKU access, this would be activated !!!


if ENV == 'dev':
    app.debug = True
    # connection to the DB. Database://usename:password@server/db
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost/feedback_mercedes'
    print("Connected to db")
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''# the URL for the HEROKU access would go here. But i dont have an HEROKU access !!!


# track modifications of objects
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# addressing a database. Mapping between DB and Python-Object
db = SQLAlchemy(app)


class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(200), unique=True)
    dealer = db.Column(db.String(200))
    rating = db.Column(db.Integer)
    vehicle = db.Column(db.String(200))
    comments = db.Column(db.Text())
    print("Database tables prepared")

    def __init__(self, customer, dealer, rating, vehicle, comments):
        self.customer = customer
        self.dealer = dealer
        self.rating = rating
        self.vehicle = vehicle
        self.comments = comments
        print("initialization done")


with app.app_context():
    # creates all tables
    db.create_all()
    print("Tables createt")


@app.route('/')
def index():
    print("Render template 'index.html'")
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        customer = request.form['customer']
        dealer = request.form['dealer']
        rating = request.form['rating']
        vehicle = request.form['vehicle']
        comments = request.form['comments']
        print("customer:",customer, ", dealer:", dealer, ", rating:", rating, ", vehicle: ", vehicle, ", comments:", comments)
        if customer == "" or dealer == "":
            print("ERROR: Input customer or dealer is missing")
            return render_template('index.html', message='Please enter required fields <h3>Hallo Welt</h3>')    # 'message' references to 'class="message"' in index.html
        if db.session.query(Feedback).filter(Feedback.customer == customer).count() == 0:    # if customer is 0, customer not exist => add data to db
            data = Feedback(customer, dealer, rating, vehicle, comments)
            db.session.add(data)
            db.session.commit()
            # calls 'send_mail' application
            print("Data commited to DB.")
            send_mail(customer, dealer, rating, vehicle, comments)
            print("Send email.")
            return render_template('success.html')
        else:
            print("ERROR: You have already submitted feedback")
            return render_template('index.html', message='You have already submitted feedback')


if __name__ == '__main__':
    print("Run Application...")
    app.run()
