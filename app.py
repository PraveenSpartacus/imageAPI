from flask import Flask, send_file
import random,os
  
app = Flask(__name__) #creating the Flask class object   
 
@app.route('/') #decorator drfines the   
def home():  
    return "Home page"

@app.route('/image')
def send_image():
    arr = os.listdir('./static/IMG')
    image_file = arr[random.randint(0,len(arr)-1)]
    imagePath = './static/IMG/' + image_file
    return send_file(imagePath, mimetype='image/gif')
  
if __name__ =='__main__':  
    app.run(debug = True)  