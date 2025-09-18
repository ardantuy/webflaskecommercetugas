import midtransclient
# Create Snap API instance
snap = midtransclient.Snap(
    is_production=False,
    server_key='Mid-server-7j3y9yQxFicv3QvKQVc8_Ebl'
)
# Prepare parameter
def create_transaction(order_id, amount):
    transaction = snap.create_transaction({
        "transaction_details": {
        "order_id": order_id,
        "gross_amount": amount
    }, "credit_card":{
        "secure" : True
    }
    })
    return transaction
transaction = create_transaction("order12", 123123123)
transaction_redirect_url = transaction['redirect_url']
