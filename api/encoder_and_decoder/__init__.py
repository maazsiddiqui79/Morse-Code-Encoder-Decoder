# api/encoder_and_decoder/__init__.py

from .encoder import Encoder
from .decoder import Decoder

class ENC_AND_DEC:
    def __init__(self):
        self.encoder = Encoder()
        self.decoder = Decoder()

    def encrypt(self, text, shift):
        return self.encoder.encrypt(text, shift)

    def decrypt(self, text, shift):
        return self.decoder.decrypt(text, shift)
