from flask import Flask, send_file, Response, request, jsonify, render_template
import random,os
from randimage import get_random_image, show_array
import matplotlib
import datetime
from random import randint
import json
  
app = Flask(__name__) #creating the Flask class object   

PRODUCTION = True

IMG_DESTINATION = ''
if PRODUCTION:
    IMG_DESTINATION = './imageAPI/static/IMG'
    HISTORY_JSON = './imageAPI/history.json'
else:
    IMG_DESTINATION = './static/IMG'
    HISTORY_JSON = './history.json'


def getAlertHistory():
    file = open(HISTORY_JSON, 'r')
    s = file.read()
    file.close()
    JSON = json.loads(s)
    return JSON


def setAlertHistory(JSON):
    file = open(HISTORY_JSON, 'w')
    file.write(json.dumps(JSON, indent=4))
    file.close()



@app.route('/', methods=['GET', 'POST']) #decorator drfines the
def home():
    JSON = {
        "status": "This is a GET request",
    }
    if request.method == 'POST':
        try:
            host, host_url = request.host, request.host_url
            data = request.json
            JSON = getAlertHistory()
            date = str(datetime.datetime.now())
            JSON.insert(0,{'date':date, 'content':data, 'host':host, 'host_url':host_url})
            setAlertHistory(JSON)
            return {"status": "SUCCESS"}
        except Exception as e:
            JSON.insert(0,{'date':date, 'content':str(e), 'host':host, 'host_url':host_url})
            setAlertHistory(JSON)
            return {"status": "ERROR"}
    JSON = getAlertHistory()
    JSON.insert(0,{'date':"now!", 'content':"GET REQUEST"})
    setAlertHistory(JSON)
    return JSON

@app.route('/view-alerts', methods=['GET'])
def view_alerts():
    JSON = getAlertHistory()
    return render_template('view_alerts.html', alerts=JSON)

@app.route('/image')
def send_image():
    img_size = (300,300)
    img = get_random_image(img_size)  #returns numpy array
    
    filename = "{}-{}.png".format(str(datetime.datetime.now().timestamp()),str(randint(0, 10000)))
    imagePath = "{}/{}".format(IMG_DESTINATION,filename)
    matplotlib.image.imsave(imagePath, img)
    base_url = "/".join(request.base_url.split('/')[:3])
    JSON = {}
    JSON['filename'] = "{}{}".format(base_url,imagePath[1:])
    # JSON = jsonify(JSON)
    # return JSON
    response = Response(response=JSON['filename'])
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response
    # return send_file(imagePath, mimetype='image/gif')
  
if __name__ =='__main__':  
    app.run(debug = True)  