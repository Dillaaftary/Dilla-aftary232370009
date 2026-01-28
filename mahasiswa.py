from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# Data mahasiswa
data_mahasiswa = [
    {
        "no": 1,
        "nama": "Ahmad Hasyim Arifin",
        "nis": "0001",
        "ttl": "Blora, 16-09-2001",
        "nama_ortu": "Nur Hasyim",
        "alamat": "Banjarejo"
    },
    {
        "no": 2,
        "nama": "Ahmad Koirul Amin",
        "nis": "0002",
        "ttl": "Blora, 25-08-2002",
        "nama_ortu": "Sugiyo",
        "alamat": "Kunduran"
    },
    {
        "no": 3,
        "nama": "Alvin Rahmad V",
        "nis": "0003",
        "ttl": "Bojonegoro, 01-06-2002",
        "nama_ortu": "Suwito",
        "alamat": "Tambakrejo"
    },
    {
        "no": 4,
        "nama": "Alvina Nur Santi",
        "nis": "0004",
        "ttl": "Blora, 21-10-2001",
        "nama_ortu": "Sunari",
        "alamat": "Todanan"
    },
    {
        "no": 5,
        "nama": "Angga Putra",
        "nis": "0005",
        "ttl": "Grobogan, 31-03-2002",
        "nama_ortu": "Saryono",
        "alamat": "Ngaringan"
    },
    {
        "no": 6,
        "nama": "Indah Astriana",
        "nis": "0006",
        "ttl": "Blora, 02-01-2002",
        "nama_ortu": "Sumito",
        "alamat": "Kunduran"
    }
]

class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        # HALAMAN TABEL
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()

            rows = ""
            for mhs in data_mahasiswa:
                rows += f"""
                <tr>
                    <td>{mhs['no']}</td>
                    <td>{mhs['nama']}</td>
                    <td>{mhs['nis']}</td>
                    <td>{mhs['ttl']}</td>
                    <td>{mhs['nama_ortu']}</td>
                    <td>{mhs['alamat']}</td>
                </tr>
                """

            html = f"""
            <html>
            <head>
                <title>Data Mahasiswa</title>
                <style>
                    body {{ font-family: Arial; }}
                    table {{ border-collapse: collapse; width: 100%; }}
                    th, td {{ border: 1px solid black; padding: 8px; text-align: center; }}
                    th {{ background-color: #f2f2f2; }}
                </style>
            </head>
            <body>
                <h2 align="center">DATA MAHASISWA KELAS XII TKJ</h2>
                <table>
                    <tr>
                        <th>No</th>
                        <th>Nama</th>
                        <th>NIS</th>
                        <th>TTL</th>
                        <th>Nama Ortu</th>
                        <th>Alamat</th>
                    </tr>
                    {rows}
                </table>
                <p align="center">
                    <a href="/api/mahasiswa">Lihat API (JSON)</a>
                </p>
            </body>
            </html>
            """

            self.wfile.write(html.encode())

        # API JSON
        elif self.path == "/api/mahasiswa":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data_mahasiswa).encode())

        # NOT FOUND
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"404 - Halaman tidak ditemukan")

# Menjalankan server
server = HTTPServer(("localhost", 8000), RequestHandler)
print("Server berjalan:")
print("Tabel   : http://localhost:8000")
print("API     : http://localhost:8000/api/mahasiswa")
server.serve_forever()