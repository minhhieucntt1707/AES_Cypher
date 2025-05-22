from flask import Flask, render_template, request, send_file
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os
import io

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        key_text = request.form.get("key")
        action = request.form.get("action")
        file = request.files.get("file")

        if not file or not key_text:
            return "Vui lòng chọn file và nhập khóa.", 400

        key = key_text.encode("utf-8")
        if len(key) < 16:
            key = key.ljust(16, b"\0")
        elif len(key) > 16:
            key = key[:16]

        file_data = file.read()
        filename = file.filename
        output = io.BytesIO()

        if action == "encrypt":
            cipher = AES.new(key, AES.MODE_CBC)
            ciphertext = cipher.encrypt(pad(file_data, AES.block_size))
            output.write(cipher.iv + ciphertext)
            output.seek(0)
            return send_file(output, as_attachment=True, download_name=filename + ".aes")

        elif action == "decrypt":
            iv = file_data[:16]
            ciphertext = file_data[16:]
            cipher = AES.new(key, AES.MODE_CBC, iv)
            try:
                plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
            except ValueError:
                return "Sai khóa hoặc file không hợp lệ.", 400
            output.write(plaintext)
            output.seek(0)
            return send_file(output, as_attachment=True, download_name="decrypted_" + filename)

    return render_template("index.html")
