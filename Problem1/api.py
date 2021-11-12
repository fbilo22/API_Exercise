from flask import Flask, request
from flask_restful import Resource, Api
import requests
import constants as csts

# Function to format the parameters for the Open Brewery DB API request
def _format_request_params(state=None, brewery_type=None, page=1, per_page=50):

    params = {'by_state': state,
              'by_type': brewery_type,
              'page':page,
              'per_page':per_page
              }

    return params

# Function to send a get request to the Open Brewery DB API. Returns the reply in json
def getjsonfromOpenBreweryDBAPI(state=None,brewery_type=None,page=1):
    
    params = _format_request_params(state=state, brewery_type=brewery_type, page=page, per_page=50)
    
    return requests.get(csts.base_url, params).json()


### Flask API
app = Flask(__name__)
api = Api(app)

class Breweries(Resource):
    def get(self):
        page = request.args.get("page", 1, type=int) #process the "page" key
        return getjsonfromOpenBreweryDBAPI(page=page)

class State(Resource):
    def get(self, state):
        page = request.args.get("page", 1, type=int) #process the "page" key
        return getjsonfromOpenBreweryDBAPI(state=state, page=page)

class Type(Resource):
    def get(self, brewery_type):
        page = request.args.get("page", 1, type=int) #process the "page" key
        return getjsonfromOpenBreweryDBAPI(brewery_type=brewery_type, page=page)

api.add_resource(Breweries, '/Breweries')
api.add_resource(State, '/Breweries/State/<string:state>')
api.add_resource(Type, '/Breweries/Type/<string:brewery_type>')

if __name__ == '__main__':
    app.run(host=csts.host, port=csts.port)