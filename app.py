from flask import Flask, url_for, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from base64 import b64decode
import uuid
import io
from PIL import Image
# import facespoof

app = Flask(__name__)
CORS(app)


UPLOAD_FOLDER = 'upload_images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
  username = db.Column(db.String(200), primary_key=True)
  def __repr__(self):
    return '<User %r>' % self.username


@app.route('/register', methods=['POST'])
@cross_origin()
def signup():
  username = request.json['username']
  user = User.query.filter_by(username=username).first()
  if user == None:
    return jsonify({ 'user': username })
  else:
    return  jsonify({ 'user': '' })


@app.route('/login', methods=['POST'])
@cross_origin()
def login():
  username = request.json['username']
  user = User.query.filter_by(username=username).first()
  if user == None:
    return jsonify({ 'user': '' })
  else:
    return jsonify({ 'user': username })
  

@app.route('/test-image-register', methods=['POST'])
def checkImage():
  # just for checking purpose
  # filename = f'{uuid.uuid4().hex}.jpeg'
  # message = request.get_json(force=True) # user input here
  # encoded = message
  # decoded = b64decode(encoded)
  # image = Image.open(io.BytesIO(decoded)) 
  return jsonify({'verified': False})
  # user = message['username'] #this via input json
  # foundUser = User.query.filter_by(username=user).first()
#   # if user is not fount, add to the database directory
#   print('user: ', foundUser)
#   print('filename outer: ', filename)
  # if foundUser == None:
#     # user came via signup
    # new_user = User(username=user)
#     try:
#       print('got user: ', user)
#       if reg_res == 'User was successfully registered':
#         db.session.add(new_user)
#         db.session.commit()
#         #add_data(filename,user)
#         print('filename inner: ', filename)
#         #os.remove(filename)
#         print('Registration Response : ', reg_res)
#         response = { 'result': reg_res }
#     except:
#       response = { 'result': 'same username exist' }
#       return jsonify(response)
#   else:
#     # user came via login
#     log_res = log(image, user)
#     if (type(log_res) == str):
#       print('Login Response: ', log_res)
#       response = { 'result': log_res }
#     else:
#       response = { 'result': 'Successfully logged in' }
#     return jsonify(response)


if __name__ == '__main__':
  app.run(debug=True)