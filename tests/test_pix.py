import sys
sys.path.append("../")

import pytest
import os
from payments.pix import Pix

def test_pix_create_payment():
    pix_instance = Pix()

    # create a payment
    paymennt_info = pix_instance.create_payment(base_dir="../")

    assert "bank_payment_id" in paymennt_info
    assert "qr_code_path" in paymennt_info

    qr_code_path = paymennt_info["qr_code_path"]
    assert os.path.isfile(f"../static/img/{qr_code_path}.png")
