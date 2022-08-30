# Art Exhibition API

A test API that gather art exhibitions and wether forcast for the venues

## Description

This *Flask* API is getting a list of current exhibitions daily at 08.00am from the [Harvard Art Museums API](https://github.com/harvardartmuseums/api-docs). It keeps only the first venue of each exhibition and geocode the location of of the venues that have a full address availble in the USA using the following [geocoding API](https://geocoding.geo.census.gov/geocoder/Geocoding_Services_API.html).  
For each venue with a successfully geocoded location, the weather forecast for the next 2 days (daytime forcast only) is retreived every 2 hours from the [api.weather.gov weather API](https://weather-gov.github.io/api/gridpoints).  
All actions are run right after the API start up.  
The downloaded data is stored in a MongoDB and accessible through the `/exhibitions` endpoint.

## Installation

Build the Docker image and run it with an available MongoDB and supplying all necessary variables.
```bash
docker build -t art_exhibition_api:0.0.0 .
```

### Variables

The following varaibles are necessary for the app to work.

| Variable | Example Value |
| -------- | ------------- |
| **MONGO_URI** | mongodb://testuser:testpass@localhost:27017/test |
| **HARVARD_MUSEUM_API_KEY** | Key obtained from this [form](https://docs.google.com/forms/d/1Fe1H4nOhFkrLpaeBpLAnSrIMYvcAxnYWm0IU9a6IkFA/viewform). |

### Docker Compose

The `docker-compose.yml` file can be used to start both the API and the MongoDB. An example setup script for the DB is located `db_setup/mongo-init.js`.
