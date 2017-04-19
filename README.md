# Thermostat Service
A thermostat web service for home automation


This service is a simple python application running with an in-memory database
it supports the general crud functionality of managing thermostats in a home.
The application is wrapped in a docker container for portablity

Tested with python version 3.6 and pip version 9.0.1

The requirements.txt file lists all library dependencies


## Run
easiest way to run is with docker-compose
```bash
docker-compose up
```
you will see that it's listening on http://localhost:8080

alternatively you can create a virtual env and run the following in a tty-terminal 
```bash
python manage.py
```


## Test
tests are ran using the py.test framework.
- using docker
   ```bash
      docker run -it --rm -v `pwd`:/app drankinn/therm-service python manage.py test
   ```
- using a virtual env
   ```bash
      python manage.py test
   ```
   
## API
There is a postman config file at tests/thermostat.postman_collection.json
Load this into postman to test the available endpoints.