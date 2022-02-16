import json, csv
import os
import re
import pandas as pd

class Person:
    def __init__(self, gender=None,	name=None,	title=None,	first=None,	last=None,	location=None,	street=None,	number=None, city=None,	state=None,	country=None,	postcode=None,	coordinates=None,	latitude=None,	longitude=None,	timezone=None,	offset=None,	description=None,	email=None,	login=None,	uuid=None,	dob=None,	date=None,	age=None,	registered=None,	phone=None):
        pass
# this is a mess
def parseJson(data):
    NewPerson = Person()
    NewPerson.gender = data['results']['gender']
    NewPerson.name = data['name']
    NewPerson.title = data['title']
    NewPerson.first = data['first']
    NewPerson.last = data['last']
    NewPerson.location = data['location']
    NewPerson.street = data['street']
    NewPerson.number = data['number']
    NewPerson.city = data['city']
    NewPerson.state = data['state']
    NewPerson.country = data['country']
    NewPerson.postcode = data['postcode']
    NewPerson.coordinates = data['coordinates']
    NewPerson.latitude = data['latitude']
    NewPerson.longitude = data['longitude']
    NewPerson.timezone = data['timezone']
    NewPerson.offset = data['offset']
    NewPerson.description = data['description']
    NewPerson.email = data['email']
    NewPerson.login = data['login']
    NewPerson.uuid = data['uuid']
    NewPerson.dob = data['dob']
    NewPerson.date = data['date']
    NewPerson.age = data['age']
    NewPerson.registered = data['registered']
    NewPerson.phone = data['phone']

fieldnames = ['gender',	'name',	'title',	'first',	'last',	'location',	'street',	'number',	'city',	'state',	'country',	'postcode',	'coordinates',	'latitude',	'longitude',	'timezone',	'offset',	'description',	'email',	'login',	'uuid',	'dob',	'date',	'age',	'registered',	'phone']

if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open("output.csv","w") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=fieldnames,delimiter='\t')
        writer.writeheader()
        for filename in os.listdir(dir_path):
            f = os.path.join(dir_path, filename)
            # checking if it is a file
            if filename.endswith('.json'):
                with open(filename,'r') as f:
                    person = json.loads(f.read())
                    nextPerson = parseJson(person)
                    writer.writerow({'gender':nextPerson.gender,	'name':nextPerson.name,	'title':nextPerson.title,	'first':nextPerson.first,	'last':nextPerson.last,	'location':nextPerson.location,	'street':nextPerson.street,	'number':nextPerson.number,	'city':nextPerson.city,	'state':nextPerson.state,	'country':nextPerson.country,	'postcode':nextPerson.postcode,	'coordinates':nextPerson.coordinates,	'latitude':nextPerson.latitude,	'longitude':nextPerson.longitude,	'timezone':nextPerson.timezone,	'offset':nextPerson.offset,	'description':nextPerson.description,	'email':nextPerson.email,	'login':nextPerson.login,	'uuid':nextPerson.uuid,	'dob':nextPerson.dob,	'date':nextPerson.date,	'age':nextPerson.age,	'registered':nextPerson.registered,	'phone':nextPerson.phone})