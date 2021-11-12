# Problem 1
Create an API which allows applications to find breweries by state or by type.
The API should interface with Open Brewery DB. While the API should have at least two endpoints, it does not have to be limited to just state and type.

# API User Guide
The API runs on `localhost:5000`. This can be changed by modifying the `host` and `port` variables in the constants.py file

The API has the following endpoints:
- `GET /Breweries`
    - Returns a list of all breweries
- `GET Breweries/Type/<brewery_type>`
    - Returns a list of all breweries of the type specified
    - Possible types: Same as the Open Brewery DB API by_type filter: 'micro','nano','regional','brewpub','large','planning','bar','contract','proprietor','closed'
- `GET Breweries/State/<state>`
    - Returns a list of all breweries from the state specified
    - Possible states: All us states, use the full state name and replace spaces with underscores

Only the first 50 results are returned. use the 'page' key to get further results

Response format:
```json
{
    "id": "swine-city-brewing-company-fairfield",
    "name": "Swine City Brewing Company",
    "brewery_type": "micro",
    "street": "4614 Industry Dr",
    "address_2": null,
    "address_3": null,
    "city": "Fairfield",
    "state": "Ohio",
    "county_province": null,
    "postal_code": "45014-1923",
    "country": "United States",
    "longitude": "-84.53106178",
    "latitude": "39.34895418",
    "phone": "7045601214",
    "website_url": "http://www.swinecitybrewing.com",
    "updated_at": "2021-10-23T02:24:55.243Z",
    "created_at": "2021-10-23T02:24:55.243Z"
},
```


# Solution and Comments
Since I'm most familiar with the Python language, I will be using it to develop the API

I see 2 parts to this problem:
- Define and Create the API
- Call the Open Brewery DB API to get the required data

I will find online examples for each of these 2 parts and try to combine them togheter to obtain a functional app

## Define and create the API

I'll use Flask framework to build the web application
There is a flask example that uses flask-restful to create a simple restful API and good documentation.

We'll simply return the same brewery data as the Open Brewery DB API

## Call the Open Brewery DB API

I see that there is a python library called `requests` that allows sendings URL requests.
I will use `requests.get` to call the Open Brewery DB API

In the open brewery DB projects section, there is a python OPC wrapper for the API that uses the `requests` API.
This will be a good example to use as reference

When testing get requests to the open brewery DB, I see that only the first 50 breweries are returned.
Further results can be retrieved using the `page` attribute in the get request.
In my API, I will have to extract the `page` key and its value to use it when sending the GET request to the Open Brewery DB API