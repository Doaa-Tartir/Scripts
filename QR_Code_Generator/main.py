from flask import Flask, render_template, request
from base64 import b64encode
import qrcode
from io import BytesIO

app=Flask(__name__)

@app.route('/')
def mainPage():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def generateQR():
    memory=BytesIO()
    data=request.form.get('url')
    image=qrcode.make(data)
    image.save(memory)
    memory.seek(0) #read the beginning of the image code
    base64img= "data:image/png;base64,"+\
        b64encode(memory.getvalue()).decode('ascii')
    return render_template('index.html', data=base64img)


if __name__=='__main__':
    app.run(debug=True) #Hot reloading  
