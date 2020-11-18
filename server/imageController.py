from flask import Flask, Blueprint, request, jsonify

imageController = Blueprint('ImageController', __name__)

db = {}

@imageController.route('/image', methods=["GET", "POST"])
def handleImage():
    if request.method == 'POST':
        data = request.get_json()

        imgData = data['imgData']
        imgName = data['imgName']

        print(imgData)
        print(imgName)

        return {"msg": "request successful"}

@imageController.route('/image/test', methods=['GET'])
def testRoute():
    return "Image Controller is working"