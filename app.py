from flask import Flask, jsonify, Response, request
from repository.db import db
from sqlalchemy import inspect
from db_models.payment import Payment
from datetime import datetime, timedelta

app = Flask(__name__)

# start db 
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.db"
app.config["SECRET_KEY"] = "SECRET_KEY_WEBSOCKET"
db.init_app(app)

@app.route("/payments/pix", methods=["POST"])
def create_payment_pix() -> Response:
    """
    Crée un paiement via Pix.

    Retourne une réponse HTTP indiquant le succès ou l'échec du paiement.
    
    Returns:
        Response: La réponse HTTP après la création du paiement.
    """
    data: Payment = request.get_json()

    if "value" not in data:
        return jsonify({ "message": "Value is required!" }), 404
    # Si expire_date est présent, le convertir en objet datetime
    expire_date_str = data.get("expire_date", None)

    if expire_date_str:
        try:
            expire_date = datetime.fromisoformat(expire_date_str)
        except ValueError:
            return jsonify({"message": "Invalid date format for expire_date!"}), 400
    else:
        expire_date = datetime.utcnow()  # Utiliser la date actuelle si expire_date n'est pas fourni

    expiration_date = datetime.now() + timedelta(minutes=30)

    new_payment = Payment(
        value=data["value"],
    )
    print(new_payment)

    db.session.add(new_payment)
    db.session.commit()

    return jsonify({ "message": "The payment has been cretated", "payment": new_payment.to_dict() })


@app.route("/payments/pix/confirmation", methods=["POST"])
def confirmation_payment_pix() -> Response:
    """
    Crée un paiement confirmation du Pix.

    Retourne une réponse HTTP indiquant le succès ou l'échec du paiement.
    
    Returns:
        Response: La réponse HTTP après la confirmation du paiement.
    """
    return jsonify({ "message": "The payment has been confirmated" })


@app.route("/payments/pix/<int:payment_id>", methods=["GET"])
def payment_pix_page(payment_id) -> Response:
    """
    Returns:
        Retiurne une page html avec le paiment pour id
    """
    return "pix payment"


if __name__ == "__main__":
    app.run(debug=True)
