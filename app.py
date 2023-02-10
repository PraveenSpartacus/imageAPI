from flask import Flask, send_file
  
app = Flask(__name__) #creating the Flask class object   
 
@app.route('/') #decorator drfines the   
def home():  
    return "Home page"

@app.route('/image')
def send_image():
    imagePath = './static/IMG/img.png'
    return send_file(imagePath, mimetype='image/gif')
  
if __name__ =='__main__':  
    app.run(debug = True)  