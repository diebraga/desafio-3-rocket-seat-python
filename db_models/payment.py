from repository.db import db

class Payment(db.Model):
    # id, val, payed, bank_payment_id, qr_code, exp_date
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Float)
    paid = db.Column(db.Boolean, default=False)
    bank_payment_id = db.Column(db.Integer, nullable=True)
    qr_code = db.Column(db.String(100), nullable=True)
    exp_date = db.Column(db.DateTime)

