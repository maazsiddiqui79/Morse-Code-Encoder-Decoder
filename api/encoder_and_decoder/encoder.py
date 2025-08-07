# api/encoder_and_decoder/encoder.py

class Encoder:
    lst = [
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
        "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", 
        "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "{", "}", "|", ":", "\"", "<", ">", "?", "~", "-", " "
    ]

    def encrypt(self, og_txt, shift):
        cipher_text = ""
        for i in og_txt:
            shifted_position = self.lst.index(i) + int(shift)
            shifted_position %= len(self.lst)
            cipher_text += self.lst[shifted_position]
        return cipher_text
