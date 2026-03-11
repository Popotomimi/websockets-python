import uuid
import qrcode

class Pix:
    def __init__(self):
        pass

    def create_payment(self):
        # criar o pagamento fake
        bank_payment_id = str(uuid.uuid4())

        # codigo copia e cola fake
        hash_payment = f'hash_payment_{bank_payment_id}'

        # qr code fake
        img = qrcode.make(hash_payment)
        img.save(f'static/img/qr_code_payment_{bank_payment_id}.png')


        return {"bank_payment_id": bank_payment_id, "qr_code_path": f"qr_code_payment_{bank_payment_id}"}