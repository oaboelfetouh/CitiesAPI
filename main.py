from fastapi import FastAPI
from pydantic import BaseModel
# use requests to get data from other API-s
import requests

app = FastAPI()

# simple in-memory database
cities = [{'name' : 'Cairo', 'timezone': 'Eastern European Standard Time'}]
class City(BaseModel):
	name : str
	timezone : str

#welcoming
@app.get('/')
def index ():
	return "Hello to the Cities api :))"

#get all the cities
@app.get('/cities')
def get_cities():
	result = []
	for c in cities:
		r = requests.get(f'http://worldtimeapi.org/api/timezone/{c["timezone"]}')
		current_time = r.json()['datetime']
		result.append({'name' : city['name'], 'timezone': city['timezone'], 'current_time': current_time})
	return result

#get a particular city
@app.get('/cities/{city_id}')
def get_city(city_id : int):
	c = cities[city_id]
	r = requests.get(f'http://worldtimeapi.org/api/timezone/{city["timezone"]}')
	current_time = r.json()['datetime']
	return {'name' : c['name'], 'timezone' : c['timezone'], 'currenttime' : current_time }

#let the user add a city
@app.post('/cities')
def create_city(city : City):
	cities.append(city.dict())
	return cities[-1] # return the last item

#delete a city from the database
@app.delete('/cities/{city_id}')
def delete_city(city_id : int):
	cities.pop(city_id)
	return {}
