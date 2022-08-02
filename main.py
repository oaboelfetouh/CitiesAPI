from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# simple in-memory database
cities = [{'Cairo' : '+2'}]
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
	return cities

#get a particular city
@app.get('/cities/{city_id}')
def get_city(city_id : int):
	return cities[city_id]

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
