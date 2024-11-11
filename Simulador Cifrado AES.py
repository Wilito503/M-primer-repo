from flask import Flask, request, render_template_string
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os

app = Flask(__name__)

def encrypt_aes_cbc(key, plaintext):
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_plaintext = padder.update(plaintext) + padder.finalize()
    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()
    return iv + ciphertext

def decrypt_aes_cbc(key, encrypted_data):
    iv = encrypted_data[:16]
    ciphertext = encrypted_data[16:]
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()
    return plaintext

@app.route('/')
def index():
    return render_template_string('''
        <h1>Cifrar/Descifrar Mensaje</h1>
        <form action="/encrypt" method="post">
            <h2>Cifrar Mensaje</h2>
            <label>Clave (32 bytes en hexadecimal):</label><br>
            <input type="text" name="key" required><br>
            <label>Mensaje:</label><br>
            <textarea name="message" required></textarea><br>
            <input type="submit" value="Cifrar">
        </form>
        <form action="/decrypt" method="post">
            <h2>Descifrar Mensaje</h2>
            <label>Clave (32 bytes en hexadecimal):</label><br>
            <input type="text" name="key" required><br>
            <label>Mensaje cifrado (en hexadecimal):</label><br>
            <textarea name="encrypted_message" required></textarea><br>
            <input type="submit" value="Descifrar">
        </form>
    ''')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    key_hex = request.form['key']
    message = request.form['message'].encode()

    key = bytes.fromhex(key_hex)
    encrypted_data = encrypt_aes_cbc(key, message)
    encrypted_data_hex = encrypted_data.hex()

    return f'<h1>Mensaje Cifrado:</h1><p>{encrypted_data_hex}</p><a href="/">Volver</a>'

@app.route('/decrypt', methods=['POST'])
def decrypt():
    key_hex = request.form['key']
    encrypted_data_hex = request.form['encrypted_message']

    key = bytes.fromhex(key_hex)
    encrypted_data = bytes.fromhex(encrypted_data_hex)

    try:
        decrypted_data = decrypt_aes_cbc(key, encrypted_data)
        decrypted_message = decrypted_data.decode()
        return f'<h1>Mensaje Descifrado:</h1><p>{decrypted_message}</p><a href="/">Volver</a>'
    except Exception as e:
        return f'<h1>Error:</h1><p>{str(e)}</p><a href="/">Volver</a>'

if __name__ == '__main__':
    app.run(debug=True)
