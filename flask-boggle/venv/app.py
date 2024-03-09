from boggle import Boggle
from flask import Flask,render_template,redirect,request,session,flash,jsonify

app=Flask(__name__)
app.config['SECRET_KEY'] = "lasjdfkashjfalkfhjalfhjlkahj"
app.config["TESTING"] = True




game=Boggle()
@app.route("/")
def home_page():
    ''' start page'''
    session['Times_play']=0
    session['Score']=0
    return render_template("home.html")

@app.route("/game")
def game():
    '''make the board'''
    game=Boggle()
    board=game.make_board()
    session['Board']=board
    plays=session['Times_play']
    score=session['Score']
    board=session["Board"]
    return render_template("game.html",board=board,plays=plays,score=score)

@app.route("/check")
def check_for_word():
    '''check if the word is valid'''
    game=Boggle()
    word=request.args['word']
    board=session["Board"]
    check=game.check_valid_word(board,word)
    return jsonify({'result': check})

@app.route("/score")
def update_score():
    '''handle the score at the end of the game'''
    score=int(request.args['score'])
    plays=int(request.args['times'])
    session['Times_play']+=plays
    max_score=session['Score']
    if score>max_score:
        session['Score']=score
    
    return jsonify({'score': score})
   
        
        
    


