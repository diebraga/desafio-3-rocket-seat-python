from repository.db import db
from datetime import datetime, timezone


class Payment(db.Model):
    # id, val, paid, bank_payment_id, qr_code, exp_date
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Float)
    paid = db.Column(db.Boolean, default=False)
    bank_payment_id = db.Column(db.Integer, nullable=True)
    qr_code = db.Column(db.String(100), nullable=True)
    expire_date = db.Column(db.DateTime, default=datetime.utcnow)


    def to_dict(self):
        return {
            "id": self.id,
            "value": self.value,
            "paid": self.paid,
            "bank_payment_id": self.bank_payment_id,
            "qr_code": self.qr_code,
            "expire_date": self.expire_date
        }