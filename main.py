import random
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1>Hello, World!</h1> <a href="/random_fact">View a random fact!</a>'

@app.route("/about") #http:127.0.0.1:5000/
def about():
    return """
    <html>
        <head>
            <title>About Us</title>
        </head>
        <body>
            <h1>Tentang Kami</h1>
            <p>Ini adalah halaman tentang kami. Kami adalah tim yang fantastis!</p>
        </body>
    </html>
    """
facts_list = ["Elon Musk mengklaim bahwa jejaring sosial dirancang untuk membuat kita tetap berada di dalam platform, sehingga kita menghabiskan waktu sebanyak mungkin untuk melihat konten.", 
            "Menurut sebuah penelitian yang dilakukan pada tahun 2018, lebih dari 50% orang berusia 18 hingga 34 tahun menganggap diri mereka ketergantungan pada ponsel pintar mereka.", 
            "Jejaring sosial memiliki sisi positif dan negatif, dan kita harus menyadari keduanya saat menggunakan platform ini.", 
            "Studi tentang kecanduan teknologi adalah salah satu bidang penelitian ilmiah modern yang paling relevan."]
@app.route("/random_fact")
def facts():
    return f'<p>{random.choice(facts_list)}</p>'

rekomendasi_game = ['mobile legend','freefire','roblox','honor of king','pubg mobile','minecraft','valorant','codm mobile']
@app.route("/rekomendasi_game")
def rekom_game():
    return f'<p>{(rekomendasi_game)}</p>'

app.run(debug=True)