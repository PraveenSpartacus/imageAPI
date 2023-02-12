from flask import Flask, send_file
import random,os
from randimage import get_random_image, show_array
import matplotlib
import datetime
from random import randint
  
app = Flask(__name__) #creating the Flask class object   

PRODUCTION = True

IMG_DESTINATION = ''
if PRODUCTION:
    IMG_DESTINATION = './imageAPI/static/IMG'
else:
    IMG_DESTINATION = './static/IMG'


@app.route('/') #decorator drfines the   
def home():  
    return "Home page"

@app.route('/image')
def send_image():
    img_size = (128,128)
    img = get_random_image(img_size)  #returns numpy array
    
    filename = "{}-{}.png".format(str(datetime.datetime.now().timestamp()),str(randint(0, 10000)))
    imagePath = "{}/{}".format(IMG_DESTINATION,filename)
    matplotlib.image.imsave(imagePath, img)

    JSON = {}
    JSON['filename'] = imagePath
    return JSON

    # return send_file(imagePath, mimetype='image/gif')
  
if __name__ =='__main__':  
    app.run(debug = True)  