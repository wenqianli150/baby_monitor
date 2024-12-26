"""
File:   capture.py
Desc:   web service that returns an image file
Date:   3/2/24
"""

from time import sleep
from flask import Flask, request, Response, jsonify, send_file

# Flask constructor
app = Flask(__name__)
app.config['DEBUG'] = True

# create a route using GET method to return the image file 
# cpatured by the USB camera
# http://ip-address-of-rpi:1200/cam
@app.route('/cam', methods=['GET'])
def snapshot():
    return send_file('/home/pi/Desktop//project/RPIcamera/image.jpg', mimetype='image/gif')


if __name__ == '__main__':
    app.run(port=1200, host='0.0.0.0')



