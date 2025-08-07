from flask import render_template, redirect, url_for, Flask, request




class ENC_AND_DEC:
    lst = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
    "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", 
    "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "{", "}", "|", ":", "\"", "<", ">", "?", "~", "-", " "
]

    def encrypt(self,og_txt, shift):
        cipher_text = ""
        
        for i in og_txt:
                shifted_position = self.lst.index(i) + int(shift)
                shifted_position %= len(self.lst)
                cipher_text += self.lst[shifted_position]
        
        return(cipher_text)

    def decrypt(self,og_txt, shift):
        cipher_text = ""
        
        for i in og_txt:
            
            
                shifted_position = self.lst.index(i) - int(shift)
                shifted_position %= len(self.lst)
                cipher_text += self.lst[shifted_position]
        
        return(cipher_text)
        

app = Flask(__name__)
cipher = ENC_AND_DEC()

MORSE_CODE = {
    # Letters
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.',     'F': '..-.',
    'G': '--.',   'H': '....',  'I': '..',    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',   'P': '.--.',  'Q': '--.-',  'R': '.-.',
    'S': '...',   'T': '-',     'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',
    ' ': '/',

    # Numbers
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
}

TEXT_CODE = {
    '.-': 'A',    '-...': 'B',    '-.-.': 'C',    '-..': 'D',    '.': 'E',    '..-.': 'F',
    '--.': 'G',    '....': 'H',    '..': 'I',    '.---': 'J',    '-.-': 'K',    '.-..': 'L',
    '--': 'M',    '-.': 'N',    '---': 'O',    '.--.': 'P',    '--.-': 'Q',    '.-.': 'R',
    '...': 'S',    '-': 'T',    '..-': 'U',    '...-': 'V',    '.--': 'W',    '-..-': 'X',
    '-.--': 'Y',    '--..': 'Z',
    '/': ' ',

    '-----': '0',    '.----': '1',    '..---': '2',    '...--': '3',    '....-': '4',    '.....': '5',
    '-....': '6',    '--...': '7',    '---..': '8',    '----.': '9'
}

@app.route('/')
def homepage():
    return render_template('home_page.html')


@app.route('/text-to-morse', methods=['GET', 'POST'])
def text_to_morse():
    MORES_TEXT_LST = []
    MORES_TEXT = ''
    if request.method == 'POST':
        text = request.form.get('plaintext') or ''
        print(text)
        for i in text:
            for k, v in MORSE_CODE.items():
                if k.upper() == i.upper():
                    MORES_TEXT_LST.append(v)
                    MORES_TEXT_LST.append(' ')
        MORES_TEXT = ''.join(MORES_TEXT_LST)
        if len(MORES_TEXT) == 0:
            MORES_TEXT = 'INVAILD CHARACTERS'

        return render_template('text_to_morse.html', morse_text=MORES_TEXT)

    return render_template('text_to_morse.html')


@app.route('/morse-to-text', methods=['GET', 'POST'])
def morse_to_text():
    if request.method == 'POST':
        TEXT_LST = []
        TEXT = ''
        morse_code = request.form.get('morsetext') or ''
        morse_code = morse_code.split(' ')
        for i in morse_code:
            for k, v in TEXT_CODE.items():
                if i == k:
                    TEXT_LST.append(v)

        TEXT = ''.join(TEXT_LST)
        if len(TEXT) == 0:
            TEXT = 'INVAILD CHARACTERS'
        return render_template('morse_to_text.html', morse_text=TEXT)

    return render_template('morse_to_text.html')


@app.route('/text-shifter', methods=['GET', 'POST'])
def text_shifter():
    code = 'encode'
    
    return render_template('txt_shifter.html',code=code)

@app.route('/text-shifter-encooder', methods=['GET', 'POST'])
def text_shifter_encode():
    code = 'encode'
    if request.method == 'POST':
        text = request.form.get('plain-text')
        shifter = request.form.get('num')
        enc_code =cipher.encrypt(og_txt=text,shift=shifter)
        print(enc_code)
        
        return render_template('txt_shifter.html',code=code , enc_code=enc_code)
        
    
    return render_template('txt_shifter.html',code=code)

@app.route('/text-shifter-decoder', methods=['GET', 'POST'])
def text_shifter_decode():
    code = 'decode'
    if request.method == 'POST':
        text = request.form.get('plain-text')
        shifter = request.form.get('num')
        enc_code =cipher.decrypt(og_txt=text,shift=shifter)
        print(enc_code)
        
        return render_template('txt_shifter.html',code=code , enc_code=enc_code)
    
    
    return render_template('txt_shifter.html',code=code)




if __name__ == '__main__':
    app.run(debug=True)
