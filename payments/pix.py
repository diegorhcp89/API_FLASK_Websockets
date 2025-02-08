import uuid
import qrcode

class Pix:
    def __init__(self):
        pass

    def create_payment(self):
        # criar o pagamento na instituição financeira
        bank_payment_id = uuid.uuid4()

        # codigo_copia_e_cola_123
        hash_payment = f'hash_payement_{bank_payment_id}'

        # qr code
        img = qrcode.make(hash_payment)

        #salvar a imagem como arquivo PNG
        img.save(f"static/img/qr_code_payment_{bank_payment_id}.png")

        return {"bank_payment_id": bank_payment_id, "qr_code_path": "qr_code_payment_{bank_payment_id}.png"}