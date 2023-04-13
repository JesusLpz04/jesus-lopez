from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/user/name")

def greet(name):
    return f"<p> hello, {name}</p>"

def readDetails(filename):
    with open(filename, 'r') as f:
        return [line for line in f]

@app.route("/")
def homeInfo():
    name= "my name"
    details= readDetails('static\details.txt')
    # title = "Welcome To My Awsome Website CACHOWWW!!!!!"
    # details = "I am a cs major at UTRGV. I Lift some heavy ass weight. PR or ER babyyyyy!!!! "
    # imgDis = "I want to grow up to be just like bernie, super old"
    # social= "please enter your SSN its for a raffle, nothing sketch, TRUST ME"
    # return render_template("base2.html", infoA=title, infoB=details, infoC=imgDis,infoD=social)
    return render_template('base2.html', name=name , aboutMe=details)

@app.route('/form',methods=['GET','POST'])
def formDemo():
    name=None
    if request.method=='POST':
        name=request.form['name']
        #return render_template('base2.html', name=name , aboutMe=[])

    return render_template('form.html', name=name)


if __name__ == "__main__":
    app.run(debug=True)