from flask import Flask, jsonify
from pygita import Bhagvadgita
from flask_cors import CORS

app = Flask (__name__)
CORS(app)

############################################
# Index 
############################################

@app.route ('/', methods=['GET'])
def index_route () :
    return jsonify({
		'author' : 'Tarun Verma',
		'author_url' : 'http://github.com/ta-verma',
		'base_url' : 'gita-api.herokuapp.com',
	    'project_name' : 'Bhagvadgita API',
		'project_url' : 'http://ta-verma.github.io/Bhagvadgita-API'
	})


############################################
# Bhagvadgita
###########################################

#Gita
@app.route ('/gita/chapter/<ch_num>/verse/<ver_num>', methods=['GET'])
def get_sloak (ch_num, ver_num) :
	result = dict(Bhagvadgita.get_by_chapter_and_verse(ch_num, ver_num))
	return jsonify (sanskrit=result['sloak'],
			english=result['english'],
			hindi=result['hindi'],
			hindi_meaning=result['wrd_mean'])


###########################################
#Start Flask
###########################################

if __name__ == "__main__":
	app.run()
