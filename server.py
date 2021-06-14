from flask import Flask, render_template
app = Flask(__name__)   

@app.route('/')          
def create_board():
    isCustom = False
    return render_template("index.html",isCustom = isCustom)

@app.route('/custom/<int:x>/<int:y>')          
def create_custom_board(x, y):
    isCustom = True
    return render_template("index.html", isCustom = isCustom, x = x, y = y) 

if __name__=="__main__":   
    app.run(debug=True)