from flask import Blueprint, render_template,request
from bson import json_util
from app import mongo

mod_main = Blueprint('main', __name__)



@mod_main.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        return render_template('indexii.html')
    elif request.method == 'POST':
        data = request.form.to_dict()
        return json_util.dumps(data)
    else:
        return 'bad request'



@mod_main.route('/<string:id>', methods=['GET'])
def get_doc(id)

    db = mongo.db.arkep

    if request.method='GET':
		doc=db.find({"_id":ObjectId(id)})
		print doc
		return "You requested a document with the id:" + id
	else:
		return 'bad request'		  

    #db=mongo.db.arkep.insert({"emri":"ipko"})
 	
   
