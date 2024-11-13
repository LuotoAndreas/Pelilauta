from flask import Flask, render_template, request

app = Flask(__name__)

# template-tiedostojen automaattinen lataus
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Asetetaan ruudukon minimikoko ja maksimikoko
MIN_SIZE = 8
MAX_SIZE = 16

@app.route("/", methods=["GET", "POST"])
def index():
    # Alustetaan oletusarvot
    board_size = MIN_SIZE
    player1 = "Pelaaja 1"
    player2 = "Pelaaja 2"
    error_message = ""

    if request.method == "GET":

        # laudan koko talteen linkistä
        try:            
            size_input = request.args.get("koko", str(MIN_SIZE))
            board_size = int(size_input)

            if board_size < MIN_SIZE or board_size > MAX_SIZE:
                raise ValueError("Koko liian pieni tai liian suuri")
        
        except ValueError as e:
            board_size = MIN_SIZE
            error_message = f"Virheellinen syöte: {str(e)}"
        
        # pelaajien nimet talteen linkistä
        try:
            player1 = request.args.get("p1", "Pelaaja 1")
            player2 = request.args.get("p2", "Pelaaja 2")
            
            if not player1 or not player2:
                raise ValueError("Pelaajien nimet puuttuvat")
        except ValueError as e:
            error_message = f"Virheellinen syöte: {str(e)}"

    if request.method == "POST":
        # käyttäjän syötteet        
        size_input = request.form.get("size", str(MIN_SIZE))  

        # katsotaan onko käyttäjän syöttämän kentän koko kelvollinen
        try: 
            board_size = int(size_input)            
            if board_size < MIN_SIZE or board_size > MAX_SIZE:
                raise ValueError("Koko liian pieni tai liian suuri")
        
        # asetetaan minimikoko kentälle jos syöte oli epäkelpo
        except ValueError as e:
            board_size = MIN_SIZE
            error_message = f"Virheellinen syöte: {str(e)}"
        
        # katsotaan onko syötettyjen pelaajien nimet kelvolliset
        try:
            player1 = request.form.get("player1", "Pelaaja 1")
            player2 = request.form.get("player2", "Pelaaja 2")

            if not player1 or not player2:
                raise ValueError("Pelaajien nimet puuttuvat")
        # jos nimiä ei ole tai ne ovat kelvottomat niin asetetaan oikea virheviesti
        except ValueError as e:
            error_message = f"Virheellinen syöte: {str(e)}"

    return render_template("pohja.xhtml", board_size = board_size, player1 = player1, player2 = player2, error_message = error_message)

if __name__ == "__main__":
    app.run(debug=True)
