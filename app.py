from flask import Flask, jsonify, Response
  
app = Flask(__name__)

@app.route("/payments/pix", methods=["POST"])
def create_payment_pix() -> Response:
    """
    Crée un paiement via Pix.

    Retourne une réponse HTTP indiquant le succès ou l'échec du paiement.
    
    Returns:
        Response: La réponse HTTP après la création du paiement.
    """
    return jsonify({ "message": "The payment has been cretated" })


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
