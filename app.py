from flask import Flask

app = Flask(__name__)

# ================= HOME =================
@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Home</title>
    </head>
    <body>
        <h1>HOME</h1>
        <p>Selamat datang di website sederhana menggunakan Python.</p>
        <a href="/">Home</a> |
        <a href="/about">About Us</a> |
        <a href="/harga">Harga</a>
    </body>
    </html>
    """

# ================= ABOUT US =================
@app.route("/about")
def about():
    return """
    <html>
    <head>
        <title>About Us</title>
    </head>
    <body>
        <h1>ABOUT US</h1>
        <p>Website ini dibuat menggunakan bahasa pemrograman Python dengan framework Flask.</p>
        <a href="/about">About Us</a> |
        <a href="/harga">Harga</a>
    </body>
    </html>
    """

# ================= HARGA =================
@app.route("/harga")
def harga():
    return """
    <html>
    <head>
        <title>Harga</title>
    </head>
    <body>
        <h1>HARGA LAYANAN</h1>
        <ul>
            <li>Paket Basic : Rp 100.000</li>
            <li>Paket Standard : Rp 250.000</li>
            <li>Paket Premium : Rp 500.000</li>
        </ul>
        <a href="/">Home</a> |
        <a href="/about">About Us</a> |
        <a href="/harga">Harga</a>
    </body>
    </html>
    """

# ================= RUN =================
if __name__ == "__main__":
    app.run(debug=True)