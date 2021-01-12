from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [{
    'city': 'Pune',
    'food': [
        {
            'misal': 'vaishali',
            'mastani': 'sujata'
        }
    ]
},
    {
        'city': 'mumbai',
        'food':
            [
                {
                    'vadapav': 'xyz-vadapav',
                    'panipuri': 'chaupati'
                }
            ]
    }
]


@app.route('/')
def home():
    return "hii from first api"


'''
@app.route('/store/<string:name>')
def get_store_name(name):
    for store in stores:
        if(store['city'] == name):
            return jsonify(store)
    return jsonify({'message': 'store not found'})

'''


@app.route('/store/<string:ser_city>')
def get_store_city(ser_city):
    for city1 in stores:
        if city1['city'] == ser_city:
            return jsonify(city1)
    return jsonify({'message': 'City not found'})


@app.route('/store', methods=['POST'])
def create_store():
    return_data = request.get_json()
    new_city = {
        'city': return_data['city'],
        'food': []
    }
    stores.append(new_city)
    return jsonify(new_city)


@app.route('/store/<string:city_name>/food_item', methods=['POST'])
def create_food_item(city_name):
    request_data = request.get_json()
    for city in stores:
        if city['city'] == city_name:
            new_food = {
                'paavbhaji': 'JMCorner',
                'Lunch': 'paalvi'
            }
            city['food'].append(new_food)
            return jsonify(new_food)

app.run(port=8000)

# app.route('/store',methods=['POST'])

