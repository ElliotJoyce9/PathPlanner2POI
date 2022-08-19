from flask import Flask, render_template, request
app = Flask(__name__)

Path = []

@app.route("/", methods = ['GET', 'POST'])
def twopoints():
    if request.method == 'POST':
        if request.form.get('action1') == 'Right Side of Engine':
            Path.append('S1')
        elif request.form.get('action2') == 'Left Side of Engine':
            Path.append('S2')
        elif request.form.get('action3') == 'POI A':
            Path.append('A')
        elif request.form.get('action4') == 'POI B':
            Path.append('B')
        elif request.form.get('submit') == 'SUBMIT':
            with open('path.txt', 'a') as f:
                f.write(str(Path) + '\n')
        else:
            Path.append('NA')
    elif request.method == 'GET':
        return render_template('twopoints.html')

    return render_template("twopoints.html")

app.run(debug = True)

