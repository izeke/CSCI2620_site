from flask import Flask, render_template, json, request, url_for
from pprint import pprint
from os import listdir
import cv2
import glitch

app = Flask(__name__, static_url_path='/static')


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/testband')
def testband():
    my_dict = { "title": "The Midnight", "genre": "Synthwave"}
    return json.dumps(my_dict)

@app.route('/testalbums', methods=['POST'])
def testalbums():
    band = request.json['params']['band'];
    if band == "Gunship":
    	albums = ["Gunship", "Dark All Day"]
    elif band == "The Midnight":
    	albums = ["Days of Thunder", "Endless Summer", "Nocturnal", "Kids"]

    print(albums)
    return json.dumps(albums)

@app.route('/getInputImageFilenames')
def getInputImageFilenames():
    return json.dumps(listdir(app.root_path + "/static/img/input"))

@app.route('/loadImage', methods=['POST'])
def loadImage():
    imgUrl = url_for('static', filename="img/input/" + request.json['params']['image'])[1:]
    img = cv2.imread(imgUrl, -1)
    cv2.imwrite(url_for('static', filename="img/")[1:] + "out.jpg", img)
    return json.dumps(True)

@app.route('/addVLine')
def addVLine():
    img = cv2.imread(url_for('static', filename="img/out.jpg")[1:], -1)
    img = glitch.addVLines(img, 5, 200, 1)
    cv2.imwrite(url_for('static', filename="img/")[1:] + "out.jpg", img)
    return json.dumps(True)

@app.route('/addHLine')
def addHLine():
    img = cv2.imread(url_for('static', filename="img/out.jpg")[1:], -1)
    img = glitch.addHLines(img, 5, 200, 1)
    cv2.imwrite(url_for('static', filename="img/")[1:] + "out.jpg", img)
    return json.dumps(True)

@app.route('/shiftSubsetV')
def shiftSubsetV():
    img = cv2.imread(url_for('static', filename="img/out.jpg")[1:], -1)
    img = glitch.shiftSubsetV(img, 5, 200, 1)
    cv2.imwrite(url_for('static', filename="img/")[1:] + "out.jpg", img)
    return json.dumps(True)

@app.route('/shiftSubsetH')
def shiftSubsetH():
    img = cv2.imread(url_for('static', filename="img/out.jpg")[1:], -1)
    img = glitch.shiftSubsetH(img, 5, 200, 1)
    cv2.imwrite(url_for('static', filename="img/")[1:] + "out.jpg", img)
    return json.dumps(True)

@app.route('/fuzzify')
def fuzzify():
    img = cv2.imread(url_for('static', filename="img/out.jpg")[1:], -1)
    img = glitch.fuzzify(img)
    cv2.imwrite(url_for('static', filename="img/")[1:] + "out.jpg", img)
    return json.dumps(True)

@app.route('/scanlineify')
def scanlineify():
    img = cv2.imread(url_for('static', filename="img/out.jpg")[1:], -1)
    img = glitch.scanlineify(img, 4)
    cv2.imwrite(url_for('static', filename="img/")[1:] + "out.jpg", img)
    return json.dumps(True)

@app.route('/bitify')
def bitify():
    img = cv2.imread(url_for('static', filename="img/out.jpg")[1:], -1)
    img = glitch.bitify(img, 4)
    cv2.imwrite(url_for('static', filename="img/")[1:] + "out.jpg", img)
    return json.dumps(True)

@app.route('/splitColors')
def splitColors():
    img = cv2.imread(url_for('static', filename="img/out.jpg")[1:], -1)
    img = glitch.shiftBlue(img, 10, 10)
    img = glitch.shiftRed(img, -10, -10)
    cv2.imwrite(url_for('static', filename="img/")[1:] + "out.jpg", img)
    return json.dumps(True)

if __name__ == "__main__":
    app.run(debug=True)
