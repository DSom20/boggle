from flask import Flask, render_template, session, request, jsonify
import pdb
from flask_debugtoolbar import DebugToolbarExtension

from boggle import Boggle

boggle_game = Boggle()

app = Flask(__name__)
app.config["SECRET_KEY"] = "whatever"

debug = DebugToolbarExtension(app)


@app.route("/")
def root_get():
    session["boggle_board"] = boggle_game.make_board()
    session["guess_list"] = []

    if "number_plays" not in session:
        session['number_plays'] = 1
    if "highest_score" not in session:
        session['highest_score'] = 0
    # print(session['number_plays'])

    return render_template("index.html", boggle_board=session["boggle_board"])


@app.route("/", methods=["POST"])
def guess_submission():
    request_body = request.get_json()
    word_guess = request_body["guess"]
    validation_string = boggle_game.check_valid_word(
        session["boggle_board"], word_guess)
    if validation_string == "ok":
        if word_guess in session["guess_list"]:
            validation_string = "You've already guessed that word"
        else:
            temp_guess_list = session["guess_list"]
            temp_guess_list.append(word_guess)
            session["guess_list"] = temp_guess_list
    return jsonify({"result": validation_string})


@app.route("/endgame", methods=["POST"])
def endgame():
    session['number_plays'] += 1

    current_score = request.get_json()['currentScore']

    if current_score > session['highest_score']:
        session['highest_score'] = current_score

    return
