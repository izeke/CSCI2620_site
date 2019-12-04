from flask import Flask, render_template, json, request, url_for
from pprint import pprint
from os import listdir
import cv2
import glitch
import numpy as np

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

# @app.route('/shiftSubsetV')
# def shiftSubsetV():
#     img = cv2.imread(url_for('static', filename="img/out.jpg")[1:], -1)
#     # img = glitch.shiftSubsetV(img, 5, 200, 1)
#     img = glitch.shiftSubsetV(img, 4000, 500, 500)
#     cv2.imwrite(url_for('static', filename="img/")[1:] + "out.jpg", img)
#     return json.dumps(True)

# @app.route('/shiftSubsetH')
# def shiftSubsetH():
#     img = cv2.imread(url_for('static', filename="img/out.jpg")[1:], -1)
#     img = glitch.shiftSubsetH(img, 5, 200, 1)
#     cv2.imwrite(url_for('static', filename="img/")[1:] + "out.jpg", img)
#     return json.dumps(True)

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

@app.route('/shiftColor', methods=['POST'])
def shiftColor():
    directionDict = {"up": {"x":0, "y": -1}, "down": {"x": 0, "y": 1}, "left": {"x": -1, "y": 0}, "right": {"x": 1, "y": 0}}
    color = request.json['params']['color']
    direction = directionDict[request.json['params']['direction']]
    step = int(request.json['params']['step'])

    img = cv2.imread(url_for('static', filename="img/out.jpg")[1:], -1)
    if color == 'red':
        img = glitch.shiftRed(img, direction['x'] * step, direction['y'] * step)
    elif color == 'green':
        img = glitch.shiftGreen(img, direction['x'] * step, direction['y'] * step)
    elif color == 'blue':
        img = glitch.shiftBlue(img, direction['x'] * step, direction['y'] * step)

    cv2.imwrite(url_for('static', filename="img/")[1:] + "out.jpg", img)
    return json.dumps(True)

@app.route('/shiftSubsetV', methods=['POST'])
def shiftSubsetV():
    leftBound = int(request.json['params']['leftBound'])
    width = int(request.json['params']['width'])
    distance = int(request.json['params']['distance'])
    direction = -1 if request.json['params']['direction'] == 'up' else 1
    img = cv2.imread(url_for('static', filename="img/out.jpg")[1:], -1)
    img = glitch.shiftSubsetV(img, leftBound, width, distance * direction)
    cv2.imwrite(url_for('static', filename="img/")[1:] + "out.jpg", img)
    return json.dumps(True)

@app.route('/shiftSubsetH', methods=['POST'])
def shiftSubsetH():
    topBound = int(request.json['params']['topBound'])
    width = int(request.json['params']['width'])
    distance = int(request.json['params']['distance'])
    direction = -1 if request.json['params']['direction'] == 'left' else 1
    img = cv2.imread(url_for('static', filename="img/out.jpg")[1:], -1)
    img = glitch.shiftSubsetH(img, topBound, width, distance * direction)
    cv2.imwrite(url_for('static', filename="img/")[1:] + "out.jpg", img)
    return json.dumps(True)

@app.route('/sharpen')
def sharpen():
    img = cv2.imread(url_for('static', filename="img/out.jpg")[1:], -1)

    sharpen = np.array([[-0.25,-0.25,-0.25],
                       [-0.25, 3,-0.25],
                       [-0.25,-0.25,-0.25]])
    img = cv2.filter2D(img, -1, sharpen)

    # sharpen = np.array([[-3, 0, -7],
    #                     [1, 4, 1],
    #                     [2, -1, 3]])
    # img = cv2.filter2D(img, -1, sharpen)

    cv2.imwrite(url_for('static', filename="img/")[1:] + "out.jpg", img)
    return json.dumps(True)

@app.route('/blur', methods=['POST'])
def blur():
    kernelSize = int(request.json['params']['kernelSize'])

    img = cv2.imread(url_for('static', filename="img/out.jpg")[1:], -1)
    blur = np.ones((kernelSize,kernelSize)) / (kernelSize*kernelSize)

    img = cv2.filter2D(img, -1, blur)

    cv2.imwrite(url_for('static', filename="img/")[1:] + "out.jpg", img)
    return json.dumps(True)

@app.route('/gaussianBlur', methods=['POST'])
def gaussianBlur():
    kernelSize = int(request.json['params']['kernelSize']) - 1

    img = cv2.imread(url_for('static', filename="img/out.jpg")[1:], -1)
    kernel = np.matmul(np.rot90(pascal(kernelSize), 1), pascal(kernelSize))
    blur = kernel / np.sum(kernel)

    img = cv2.filter2D(img, -1, blur)

    cv2.imwrite(url_for('static', filename="img/")[1:] + "out.jpg", img)
    return json.dumps(True)

@app.route('/edgeDetect', methods=['POST'])
def edgeDetect():
    img = cv2.imread(url_for('static', filename="img/out.jpg")[1:], -1)

    if (request.json['params']['format'] == "gray"):
        img = cv2.cvtColor(cv2.Canny(img, 100, 100), cv2.COLOR_GRAY2BGR)
    elif (request.json['params']['format'] == "color"):
        img = cv2.bitwise_and(img, cv2.cvtColor(cv2.Canny(img, 100, 100), cv2.COLOR_GRAY2BGR))

    cv2.imwrite(url_for('static', filename="img/")[1:] + "out.jpg", img)
    return json.dumps(True)

@app.route('/test', methods=['POST'])
def test():
    #weird blur
    # img = cv2.imread(url_for('static', filename="img/out.jpg")[1:], -1)
    # sharpen = np.zeros((100,100))
    # total = 0
    # for x in range(0, 99):
    #     for y in range(0, 99):
    #         if x == 0 or y % x == 0 or x % (y + 2) == 0:
    #             sharpen[x][y] = 1
    #             total += 1
    # sharpen = sharpen / total
    # img = cv2.filter2D(img, -1, sharpen)
    # cv2.imwrite(url_for('static', filename="img/")[1:] + "out.jpg", img)


    #vcr lines
    # img = cv2.imread(url_for('static', filename="img/out.jpg")[1:], -1)
    # height, width, x = img.shape
    # imgTest = cv2.imread(url_for('static', filename="img/glitch2.jpg")[1:], -1)
    # imgTest = cv2.resize(imgTest, (width, height))
    # img = cv2.addWeighted(img, 0.75, imgTest, 0.25, 0.0)
    # cv2.imwrite(url_for('static', filename="img/")[1:] + "out.jpg", img)

    #vcr border
    # img = cv2.imread(url_for('static', filename="img/out.jpg")[1:], -1)
    # height, width, x = img.shape
    # imgTest = cv2.imread(url_for('static', filename="img/glitch2.jpg")[1:], -1)
    # imgTest = cv2.resize(imgTest, (width, height))
    # img = img + imgTest
    # cv2.imwrite(url_for('static', filename="img/")[1:] + "out.jpg", img)

    #wavy
    img = cv2.imread(url_for('static', filename="img/out.jpg")[1:], -1)
    img = glitch.wavy(img)
    cv2.imwrite(url_for('static', filename="img/")[1:] + "out.jpg", img)

    return json.dumps(True)



def pascal(n):
    line = [1]
    for k in range(n):
        line.append(line[k] * (n-k) / (k+1))
    return [line]

if __name__ == "__main__":
    app.run(debug=True)
